import os
from textual.app import App
from textual.containers import Container
from textual.reactive import reactive

from card import Card
from width_indicator import WidthIndicator

os.environ["COLORTERM"] = "truecolor"

class Pulse(App):
    CSS = """
    Screen {
        background: rgb(25, 25, 25);
        padding: 1 2;
    }

    .cards {
        layout: grid;
        grid-size: 2;
        grid-gutter: 1 4;
        height: auto;
    }

    .CPU, .Processes {
        column-span: 2;
    }

    .Memory {
        row-span: 3;
    }

    .width-indicator {
        column-span: 2;
    }

    .cards.stacked {
        grid-size: 1; 
    }

    .cards.stacked .CPU, 
    .cards.stacked .Processes,
    .cards.stacked .width-indicator {
        column-span: 1;
    }

    .cards.stacked .Memory {
        row-span: 1;
    }
    """

    narrow = reactive(False)

    def compose(self):
        with Container(classes = "cards"):
            yield Card(classes = "CPU")
            yield Card(classes = "Memory")
            yield Card(classes = "Network")
            yield Card(classes = "Battery")
            yield Card(classes = "Storage")
            yield Card(classes = "Processes")
            yield WidthIndicator(classes = "width-indicator")

    def on_mount(self):
        self.call_after_refresh(self.screen.scroll_home, animate = False)

    def on_resize(self, event):
        self.narrow = event.size.width < 110

    def watch_narrow(self, narrow):
        self.query_one(".cards").set_class(narrow, "stacked")

if __name__ == "__main__":
    app = Pulse()
    app.run()