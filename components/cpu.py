from textual.containers import Container
from textual.widgets import Label, Static
from psutil import cpu_count, cpu_freq, cpu_percent
from textual_plotext import PlotextPlot
from textual import work

class CPU(Container):
    DEFAULT_CSS = """
    .row {
        layout: horizontal;
        height: auto;
        margin-top: 1;
    }

    .spacer {
        width: 1fr;
    }

    .usage-plot {
        width: 100%;
        height: 11;
        border: none;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = [0] * 60

    def on_mount(self):
        plot_widget = self.query_one(PlotextPlot)
        plot = plot_widget.plt
        plot.title("Usage (last 60 seconds)")
        plot.ylim(0, 100)
        plot.xlim(0, 60)
        plot.yticks([0, 50, 100])
        plot.xticks([0, 30, 60])
        plot.frame(True)   

        x = list(range(len(self.data)))
        plot.plot(x, self.data, color = "rgb(80, 120, 210)", marker = "braille", fillx = True)
        plot_widget.refresh()

        self.set_interval(1.0, self.update)

    @work(thread = True)
    def update(self):
        current_usage = cpu_percent(interval = None)
        self.query_one("#frequency", Label).update(f"Frequency: {round(cpu_freq().current, 2)}")

        self.data.append(current_usage)
        self.data = self.data[-61:]

        plot_widget = self.query_one(PlotextPlot)
        plot = plot_widget.plt
        plot.clear_data()

        x = list(range(len(self.data)))
        plot.plot(x, self.data, color = "rgb(80, 120, 210)", marker = "braille", fillx = True)
        
        plot_widget.refresh()
    
    def compose(self):
        yield PlotextPlot(classes = "usage-plot")

        with Container(classes = "row"):
            yield Label(f"Cores: {cpu_count()}", id = "cores")
            yield Static(classes = "spacer")
            yield Label(f"Frequency: {round(cpu_freq().current, 2)}", id = "frequency")