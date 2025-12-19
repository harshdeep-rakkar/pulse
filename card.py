from textual.containers import Container
from textual.widgets import Label
from components.cpu import CPU

class Card(Container):
    DEFAULT_CSS = """
    Card {
        background: rgb(30, 30, 30);
        border: none;
        height: auto;
        margin: 1 2;
        padding: 1 4;
    }

    .card-title {
        width: 100%;
        content-align: center middle;
        background: rgb(25, 25, 25);
        padding-top: 1;
        padding-bottom: 1;
    }

    .row {
        layout: horizontal;
        height: auto;
    }

    .card-body {
        height: auto;
        padding-top: 1;
    }
    """

    def __init__(self, title):
        super().__init__()
        self.title = title

    def compose(self):
        yield Label(self.title, classes = "card-title")

        match self.title:
            case "CPU":
                yield CPU(classes = "card-body")
            case "Memory":
                pass
            case "Network":
                pass
            case "Storage":
                pass
            case "Battery":
                pass
            case "System Processes":
                pass