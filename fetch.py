import psutil

def get_data():
    bytes_in_gb = 1024 ** 3
    cpu_frequency = psutil.cpu_freq()
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()

    return {
        "CPU": {
            "Cores": psutil.cpu_count(),
            "Current CPU frequency": round(cpu_frequency.current, 2),
            "Maximum CPU frequency": round(cpu_frequency.max, 2),
        },

        "Memory": {
            "Used virtual memory": round(virtual_memory.used / bytes_in_gb, 2),
            "Total virtual memory": round(virtual_memory.total / bytes_in_gb, 2),
            "Used swap memory": round(swap_memory.used / bytes_in_gb, 2),
            "Total swap memory": round(swap_memory.total / bytes_in_gb, 2),
        }
    }

if __name__ == "__main__":
    print(get_data())