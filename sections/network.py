from psutil import net_io_counters
from textual.containers import Container
from textual.widgets import Label, Static

class Network(Container):
    DEFAULT_CSS = """
    Network {
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
    
    def __init__(self):
        super().__init__()
        self.previous_recv = 0
        self.previous_sent = 0
    
    def on_mount(self):
        self.update_data()
        self.set_interval(1.0, self.update_data)
    
    def update_data(self):
        counters = net_io_counters()

        sent_rate = (counters.bytes_sent - self.previous_sent) / (1024 * 1024)
        recv_rate = (counters.bytes_recv - self.previous_recv) / (1024 * 1024)

        self.previous_sent = counters.bytes_sent
        self.previous_recv = counters.bytes_recv
        
        self.query_one("#outgoing", Label).update(f"[rgb(50, 140, 220)]▲[/rgb(50, 140, 220)] {sent_rate:.2f} MB/s")
        self.query_one("#incoming", Label).update(f"[rgb(50, 140, 220)]▼[/rgb(50, 140, 220)] {recv_rate:.2f} MB/s")
    
    def compose(self):
        with Container(classes = "row"):
            yield Label(id = "outgoing")
            yield Static(classes = "spacer")
            yield Label(id = "incoming")