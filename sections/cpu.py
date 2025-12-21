from textual.containers import Container
from textual.widgets import Label, Static
from psutil import cpu_count, cpu_freq

class CPU(Container):
    DEFAULT_CSS = """
    CPU {
        height: auto;
    }

    .row {
        layout: horizontal;
        height: auto;
    }

    .spacer {
        width: 1fr;
        min-width: 4;
    }
    """

    def on_mount(self):
        self.update_data()
        self.query_one("#cores", Label).update(f"Cores: {cpu_count()}")
        self.set_interval(1.0, self.update_data)

    def update_data(self):
        self.query_one("#frequency", Label).update(f"Frequency: {cpu_freq().current:.2f} MHz")
    
    def compose(self):
        with Container(classes = "row"):
            yield Label(id = "cores")
            yield Static(classes = "spacer")
            yield Label(id = "frequency")