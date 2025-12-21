from textual.widgets import DataTable
from textual.containers import Container
from psutil import process_iter
from datetime import datetime

class Processes(Container):
    DEFAULT_CSS = """
    Processes {
        height: auto;
        align: center middle;
    }

    #process-table {
        width: auto;
        max-width: 100%;
        background: rgb(25, 25, 25);
        border: hidden;
        padding-left: 1;
        padding-right: 1;
        background-tint: transparent 0%;
    }

    #process-table > .datatable--header {
        background: rgb(35, 35, 35);
        background-tint: transparent 0%;
        text-style: none;
    }
    """

    def compose(self):
        yield DataTable(cursor_type = "none", id = "process-table")

    def on_mount(self):
        table = self.query_one("#process-table")
        table.add_columns(
            "Process ID",
            "Process name",
            "Owner",
            "Status",
            "CPU utilization",
            "Memory (MB)",
            "Threads",
            "Creation time",
        )

        self.update_data()
        self.set_interval(5.0, self.update_data)

    def update_data(self):
        table = self.query_one("#process-table")

        scroll_x = table.scroll_x
        scroll_y = table.scroll_y

        table.clear()
        
        for process in process_iter(["pid", "name", "username", "status", "cpu_percent", "memory_info", "num_threads", "create_time"]):
            table.add_row(
                process.info["pid"],
                process.info["name"],
                process.info["username"],
                process.info["status"],
                process.info["cpu_percent"],
                round(process.info["memory_info"].rss / (1024 * 1024), 2),
                process.info["num_threads"],
                datetime.fromtimestamp(process.info["create_time"]).strftime("%Y-%m-%d %H:%M:%S"),
            )

        table.scroll_x = scroll_x
        table.scroll_y = scroll_y