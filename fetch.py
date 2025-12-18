import psutil
import json
import time
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers = 2)

def get_network_activity():
    net1 = psutil.net_io_counters()
    time.sleep(1)
    net2 = psutil.net_io_counters()

    sent = net2.bytes_sent - net1.bytes_sent
    received = net2.bytes_recv - net1.bytes_recv

    return sent, received

def get_cpu_usage():
    return psutil.cpu_percent(interval = 1)

def get_storage_info():
    partitions = psutil.disk_partitions(all = False)
    
    total = 0
    used = 0

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        total += usage.total
        used += usage.used

    return used, total

def get_processes(bytes_in_mb):
    processes = []
    
    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_info"]):
        info = process.info
        memory = info["memory_info"]

        readable_info = {
            "Process ID": info["pid"],
            "Process name": info["name"],
            "CPU utilization": info["cpu_percent"],
            "Memory": round(memory.rss / bytes_in_mb, 2)
        }
        
        processes.append(readable_info)

    return processes

def get_data():
    bytes_in_mb = 1024 ** 2
    bytes_in_gb = 1024 ** 3
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()
    outgoing, incoming = pool.submit(get_network_activity).result()
    battery = psutil.sensors_battery()
    time_remaining = battery.secsleft
    processes = get_processes(bytes_in_mb)

    return {
        "CPU": {
            "Cores": psutil.cpu_count(),
            "Usage": pool.submit(get_cpu_usage).result(),
        },

        "Memory": {
            "Used": round(virtual_memory.used / bytes_in_gb, 2),
            "Total": round(virtual_memory.total / bytes_in_gb, 2),
            "Swap used": round(swap_memory.used / bytes_in_gb, 2),
            "Swap total": round(swap_memory.total / bytes_in_gb, 2),
        },

        "Network": {
            "Outgoing": round(outgoing / bytes_in_mb, 2),
            "Incoming": round(incoming / bytes_in_mb, 2)
        },

        "Storage": {
            "Used": round(get_storage_info()[0] / bytes_in_gb, 2),
            "Total": round(get_storage_info()[1] / bytes_in_gb, 2)
        },

        "Battery": {
            "Percent": round(battery.percent, 2),
            "Plugged": battery.power_plugged,
            "Time remaining": [time_remaining // 3600, (time_remaining // 60) - (time_remaining // 3600) * 60]
        },

        "System Process": {
            "Processes": processes
        }
    }

if __name__ == "__main__":
    print(json.dumps(get_data(), indent = 4))