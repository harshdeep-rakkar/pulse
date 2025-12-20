import os
from textual.app import App
from textual.containers import Container

from card import Card

os.environ["COLORTERM"] = "truecolor"

class Pulse(App):
    CSS = """
    Screen {
        background: rgb(25, 25, 25);
        padding: 1 2;
    }

    .row {
        layout: horizontal;
        height: auto;
    }

    .column {
        height: auto;
    }
    """

    def compose(self):
        with Container(classes = "row"):
            
            with Container(classes = "column"):
                yield Card("CPU")
                yield Card("Processes")
            
            with Container(classes = "column"):
                yield Card("Memory")
                yield Card("Battery")
                yield Card("Storage")
                yield Card("Network")

if __name__ == "__main__":
    app = Pulse()
    app.run()