from textual.containers import Container
from textual.widgets import Label, ProgressBar, Static
from psutil import disk_partitions, disk_usage

class Storage(Container):
    DEFAULT_CSS = """
    Storage {
        height: auto;
    }

    .row {
        layout: horizontal;
        height: auto;
        margin-top: 1;
    }

    .spacer {
        width: 1fr;
        min-width: 4;
    }

    #storage-bar Bar {
        width: 1fr;
    }

    #storage-bar Bar > .bar--bar, #storage-bar Bar > .bar--complete {
        color: rgb(50, 140, 220);
        background: rgb(20, 50, 100);
    }
    """

    def on_mount(self):
        partitions = disk_partitions(all = False)
    
        total = 0
        used = 0

        for partition in partitions:
            usage = disk_usage(partition.mountpoint)
            total += usage.total
            used += usage.used

        bar = self.query_one("#storage-bar", ProgressBar)
        bar.update(progress = (used / total) * 100)

        self.query_one("#used", Label).update(f"Used: {(used / 1024 ** 3):.2f} GB")
        self.query_one("#total", Label).update(f"Total: {(total / 1024 ** 3):.2f} GB")

    def compose(self):
        yield ProgressBar(
            total = 100,
            show_percentage = True,
            show_eta = False,
            id = "storage-bar"
        )

        with Container(classes = "row"):
            yield Label(id = "used")
            yield Static(classes = "spacer")
            yield Label(id = "total")