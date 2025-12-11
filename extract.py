import psutil

def get_details():
    bytes_in_gb = 1024 ** 3
    cpu_frequency = psutil.cpu_freq()
    virtual_memory = psutil.virtual_memory()
    swap_memory = psutil.swap_memory()

    details = {
        "cpu": {
            "cpu_cores": psutil.cpu_count(),
            "minimum_cpu_frequency": cpu_frequency.min,
            "maximum_cpu_frequency": cpu_frequency.max,
            "current_cpu_frequency": cpu_frequency.current
        },

        "memory": {
            "used_virtual_memory": virtual_memory.used / bytes_in_gb,
            "total_virtual_memory": virtual_memory.total / bytes_in_gb,
            "used_swap_memory": swap_memory.used / bytes_in_gb,
            "total_swap_memory": swap_memory.total / bytes_in_gb
        }
    }

    return details

if __name__ == "__main__":
    details = get_details()
    cpu_details = details["cpu"]
    memory_details = details["memory"]

    print(f"""
    > CPU
    CPU cores: {cpu_details["cpu_cores"]}
    Minimum CPU frequency: {cpu_details["minimum_cpu_frequency"]:.2f}
    Maximim CPU frequency: {cpu_details["maximum_cpu_frequency"]:.2f}
    Current CPU frequency: {cpu_details["current_cpu_frequency"]:.2f}

    > Memory
    Used virtual memory: {memory_details["used_virtual_memory"]:.2f}
    Total virtual memory: {memory_details["total_virtual_memory"]:.2f}
    Used swap memory: {memory_details["used_swap_memory"]:.2f}
    Total swap memory: {memory_details["total_swap_memory"]:.2f}
    """)
