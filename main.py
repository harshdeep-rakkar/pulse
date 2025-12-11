from textual.app import App
from textual.widgets import Header, Footer, Static
from extract import get_details

class Pulse(App):
    CSS = """
    Screen {
        layout: vertical;
        align: center middle;
    }
    #data-display {
        width: 80%;
        height: auto;
        padding: 2;
        border: solid dodgerblue;
        content-align: center middle;
    }
    .key {
        color: green;
        font-weight: bold;
    }
    .value {
        color: yellow;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit")
    ]

    def compose(self):
        yield Header()
        yield Footer()
        yield Static("Initializing data...", id="data-display")

    def on_mount(self) -> None:
        self.set_interval(1.0, self.update_data)

    def update_data(self) -> None:
        data = get_details()
        data_widget = self.query_one("#data-display", Static)
        display_lines = []
        for key, value in data.items():
            line = (
                f"[class=key]{key}:[/class] "
                f"[class=value]{value}[/class]"
            )
            display_lines.append(line)

        data_widget.update("\n".join(display_lines))


if __name__ == "__main__":
    app = Pulse()
    app.run()
