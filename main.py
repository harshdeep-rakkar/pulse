import os
from textual.app import App
from textual.containers import Horizontal, Vertical
from components.card import Card
from fetch import get_data

os.environ["COLORTERM"] = "truecolor"

class Pulse(App):
    CSS = """
    Screen {
        background: rgb(35, 35, 35)
    }
    """

    def compose(self):
        data = get_data()
        
        with Vertical():
            with Horizontal():
                yield Card("CPU", data["CPU"], id = "cpu-card")
                yield Card("Memory", data["Memory"], id = "memory-card")
            
            with Horizontal():
                yield Card("Network", data["Network"], id = "network-card")
                yield Card("Storage", data["Storage"], id = "storage-card")

    def on_mount(self):
        self.set_interval(1.0, self.update)

    def update(self):
        data = get_data()

        self.query_one("#cpu-card", Card).update(data["cpu"])
        self.query_one("#memory-card", Card).update(data["memory"])
        self.query_one("#network-card", Card).update(data["cpu"])
        self.query_one("#storage-card", Card).update(data["memory"])

if __name__ == "__main__":
    app = Pulse()
    app.run()