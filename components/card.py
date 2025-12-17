from textual.containers import Container
from textual.widgets import Label, Static, ProgressBar

class Card(Container):
    DEFAULT_CSS = """
    Card {
        background: rgb(30, 30, 30);
        border: none;
    }

    .card-header {
        text-align: center;
    }

    ProgressBar {
        margin-bottom: 1;
    }
    
    .gauge-label {
        margin-top: 1;
    }
    """

    def __init__(self, title, data, id=None):
        super().__init__(id=id)
        self.card_title = title
        self.data = data
        self.static_widgets = {}
        self.gauge_widgets = {}

    def compose(self):
        yield Static(self.card_title, classes = "card-header")

        for key, value in self.data.get("statics", {}).items():
            static_widget = Label(f"{key}: {value}")
            self.static_widgets[key] = static_widget
            yield static_widget

        for key, info in self.data.get("gauges", {}).items():
            yield Label(f"{key} ({info["current"]} / {info["total"]} {info["unit"]})", classes = "gauge-label", id = f"label-{key}")

            bar = ProgressBar(
                total = info["total"], 
                show_eta = False, 
                show_percentage = True,
                id = f"bar-{key}"
            )

            bar.progress = info["current"]
            self.gauge_widgets[key] = bar
            yield bar

    def update_data(self, new_data):
        for key, value in new_data.get("statics", {}).items():
            if key in self.static_widgets:
                self.static_widgets[key].update(f"{key}: {value}")

        for key, info in new_data.get("gauges", {}).items():
            if key in self.gauge_widgets:
                bar = self.gauge_widgets[key]
                bar.update(total = info["total"], progress = info["current"])
                
                label_id = f"#label-{key}"
                if self.query(label_id):
                    self.query_one(label_id, Label).update(
                        f"{key} ({info["current"]} / {info["total"]} {info["unit"]})"
                    )