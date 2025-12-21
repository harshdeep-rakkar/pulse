from textual.containers import Container
from sections import cpu, battery, network, storage, processes

class Card(Container):
    DEFAULT_CSS = """
    Card {
        border: white;
        height: auto;
        margin: 1 3;
        padding: 1 4;
        border-title-align: center;
    }
    """

    def __init__(self, title):
        super().__init__()
        self.border_title = title

    def compose(self):
        match self.border_title:
            case "CPU":
                yield cpu.CPU()
            case "Memory":
                pass
            case "Network":
                yield network.Network()
            case "Storage":
                yield storage.Storage()
            case "Battery":
                yield battery.Battery()
            case "Processes":
                yield processes.Processes()
                