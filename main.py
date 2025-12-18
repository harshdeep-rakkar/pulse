import os
from textual.app import App
from textual.containers import VerticalScroll, Horizontal, Vertical
from components.card import Card
from fetch import get_data

os.environ["COLORTERM"] = "truecolor"

class Pulse(App):
    CSS = """
    Screen {
        background: rgb(35, 35, 35);
        padding: 1 2;
    }
    """

    def compose(self):
        data = get_data()
        
        with VerticalScroll():
            with Horizontal():
                with Vertical():
                    yield Card("CPU", data["CPU"])
                    yield Card("Network", data["Network"])
                
                with Vertical():
                    yield Card("Memory", data["Memory"])
                    yield Card("Battery", data["Battery"])
                    yield Card("Storage", data["Storage"])

if __name__ == "__main__":
    app = Pulse()
    app.run()