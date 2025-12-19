import os
from textual.app import App
from textual.containers import Container

from card import Card

os.environ["COLORTERM"] = "truecolor"

class Pulse(App):
    CSS = """
    Screen {
        background: rgb(35, 35, 35);
        padding: 1 2;
    }

    .system-info {
        layout: grid;
        grid-size: 2;
        height: auto;
    }

    .column {
        height: auto;
    }
    """

    def compose(self):
        with Container(classes = "system-info"):
            
            with Container(classes = "column"):
                yield Card("CPU")
                yield Card("Network")
            
            with Container(classes = "column"):
                yield Card("Memory")
                yield Card("Battery")
                yield Card("Storage")

        yield Card("Processes")

if __name__ == "__main__":
    app = Pulse()
    app.run()