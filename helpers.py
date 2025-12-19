import psutil
import time

bytes_in_mb = 1024 ** 2
bytes_in_gb = 1024 ** 3

def get_cpu_data(instant = False):
    if (instant):
        return {
            "cores": psutil.cpu_count(),
            "frequency": round(psutil.cpu_freq().current, 2)
        }
    
    else:
        return {
            "usage": psutil.cpu_percent(interval = 1)
        }

def get_memory_data():
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()

    return {
        "Used": round(virtual_memory.used / bytes_in_gb, 2),
        "Total": round(virtual_memory.total / bytes_in_gb, 2),
        "Used swap": round(swap_memory.used / bytes_in_gb, 2),
        "Total swap": round(swap_memory.total / bytes_in_gb, 2)
    }

def get_network_data():
    network_io_1 = psutil.net_io_counters()
    time.sleep(1)
    network_io_2 = psutil.net_io_counters()

    outgoing = network_io_2.bytes_sent - network_io_1.bytes_sent
    incoming = network_io_2.bytes_recv - network_io_1.bytes_recv

    return {
        "Outgoing": round(outgoing / bytes_in_mb, 2),
        "Incoming": round(incoming / bytes_in_mb, 2)
    }

def get_storage_data():
    partitions = psutil.disk_partitions(all = False)
    
    total = 0
    used = 0

    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        total += usage.total
        used += usage.used

    return {
        "Used": round(used / bytes_in_gb, 2),
        "Total": round(total / bytes_in_gb, 2)
    }

def get_battery_data():
    battery = psutil.sensors_battery()
    time_remaining = battery.secsleft

    return {
        "Percent": round(battery.percent, 2),
        "Plugged": battery.power_plugged,
        "Time remaining": [time_remaining // 3600, (time_remaining // 60) - (time_remaining // 3600) * 60]
    }

def get_processes():
    processes = []
    
    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_info"]):
        info = process.info
        memory = info["memory_info"]

        readable_info = {
            "Process ID": info["pid"],
            "Process name": info["name"],
            "CPU utilization": info["cpu_percent"],
            "Memory": round(memory.rss / bytes_in_mb, 2),
        }
        
        processes.append(readable_info)

    return processes

if __name__ == "__main__":
    print(get_cpu_data())
    print(get_memory_data())
    print(get_network_data())
    print(get_storage_data())
    print(get_battery_data())
    print(get_processes())