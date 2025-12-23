from textual.containers import Container
from sections import cpu, battery, network, storage, processes, memory

class Card(Container):
    DEFAULT_CSS = """
    Card {
        border: round rgb(255, 255, 255);
        height: auto;
        padding: 1 4;
        border-title-align: center;
    }
    """

    def __init__(self, classes = None):
        super().__init__(classes = classes)
        self.border_title = classes

    def compose(self):
        match self.border_title:
            case "CPU":
                yield cpu.CPU()
            case "Memory":
                yield memory.Memory()
            case "Network":
                yield network.Network()
            case "Storage":
                yield storage.Storage()
            case "Battery":
                yield battery.Battery()
            case "Processes":
                yield processes.Processes()
                