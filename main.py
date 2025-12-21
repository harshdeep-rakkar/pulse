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

    def on_mount(self) -> None:
        self.call_after_refresh(self.screen.scroll_home, animate = False)

    def compose(self):
        yield Card("CPU")

        with Container(classes = "row"):
            with Container(classes = "column"):
                yield Card("Memory")
            
            with Container(classes = "column"):
                yield Card("Network")
                yield Card("Battery")
                yield Card("Storage")
        
        yield Card("Processes")

if __name__ == "__main__":
    app = Pulse()
    app.run()