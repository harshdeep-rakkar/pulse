from textual.containers import Container
from textual.widgets import Label, ProgressBar
from psutil import sensors_battery

class Battery(Container):
    DEFAULT_CSS = """
    Battery {
        height: auto;
    }

    .row {
        layout: horizontal;
        height: auto;
        margin-top: 1;
    }

    #charging, #time-remaining {
        width: 1fr;
    }

    #battery-bar Bar {
        width: 1fr;
    }

    #battery-bar Bar > .bar--bar {
        color: green;
        background: red;
    }
    """

    def on_mount(self):
        self.update_data()
        self.set_interval(10.0, self.update_data)

    def update_data(self):
        battery = sensors_battery()
        hours_remaining = battery.secsleft // 3600
        minutes_remaining = (battery.secsleft // 60) - (hours_remaining * 60)

        if hours_remaining != 0:
            self.query_one("#time-remaining", Label).update(f"Time remaining: {hours_remaining} hr {minutes_remaining} min")
        else:
            self.query_one("#time-remaining", Label).update(f"Time remaining: {minutes_remaining} min")

        bar = self.query_one("#battery-bar", ProgressBar)
        bar.update(progress = battery.percent)

        self.query_one("#charging", Label).update(f"Charging: {battery.power_plugged}")

    def compose(self):
        yield ProgressBar(
            total = 100,
            show_percentage = True,
            show_eta = False,
            id = "battery-bar"
        )

        with Container(classes = "row"):
            yield Label(id = "charging")
            yield Label(id = "time-remaining")