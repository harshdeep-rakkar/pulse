from textual.containers import Container
from textual.widgets import Label
from cpu import CPU
from memory import Memory
from network import Network
from storage import Storage
from battery import Battery
from process_table import ProcessTable

class Card(Container):
    DEFAULT_CSS = """
    Card {
        background: rgb(30, 30, 30);
        border: none;
        height: auto;
        margin: 1 2;
        padding: 1 2;
    }

    .card-title {
        content-align: center middle;
        height: auto;
    }

    .card-body {
        content-align: center middle;
        height: auto;
    }
    """

    def __init__(self, title, data):
        super().__init__()
        self.card_title = title
        self.data = data

    def compose(self):
        with Container(classes = "card-title"):
            yield Label(self.card_title)

        with Container(classes = "card-body"):
            match self.title:
                case "CPU":
                    yield CPU()
                case "Memory":
                    yield Memory()
                case "Network":
                    yield Network()
                case "Storage":
                    yield Storage()
                case "Battery":
                    yield Battery()
                case "System Processes":
                    yield ProcessTable()