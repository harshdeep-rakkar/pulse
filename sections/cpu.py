from textual.containers import Container, Grid
from textual.widgets import Label, Static, ProgressBar
from psutil import cpu_count, cpu_freq, cpu_percent, cpu_times_percent

class CPU(Container):
    DEFAULT_CSS = """
    CPU {
        height: auto;
    }

    .row {
        layout: horizontal;
        height: auto;
        margin-top: 1;
    }

    .spacer {
        width: 1fr;
        min-width: 4;
    }
    
    .per-core-usage {
        grid-size: 4;
        grid-gutter: 1 4;
        height: auto;
    }
    
    .core-info {
        layout: horizontal;
        height: auto;
    }

    .core-bar Bar > .bar--bar, .core-bar Bar > .bar--complete {
        color: rgb(220, 140, 220);
        background: rgb(80, 30, 80);
    }
    """

    def on_mount(self):
        self.update_data()
        self.set_interval(1.0, self.update_data)

    def update_data(self):
        cpu_times = cpu_times_percent()
        
        self.query_one("#cpu-usage", Label).update(f"Usage: {cpu_percent()}%")
        self.query_one("#user", Label).update(f"User mode: {cpu_times.user}%")
        self.query_one("#system", Label).update(f"Kernel mode: {cpu_times.system}%")
        self.query_one("#idle", Label).update(f"Idle: {cpu_times.idle}%")
        self.query_one("#frequency", Label).update(f"Frequency: {cpu_freq().current:.2f} MHz")
        
        core_usage = cpu_percent(percpu = True)
        
        for i, usage in enumerate(core_usage):
            self.query_one(f"#core-bar-{i + 1}", ProgressBar).update(progress = usage)
    
    def compose(self):
        with Grid(classes = "per-core-usage"):
            for i in range(cpu_count()):
                with Container(classes = "core-info"):
                    yield Label(f"Core {i + 1}  ", classes = "core-label")
                    yield ProgressBar(total = 100, show_eta = False, show_percentage = True, id = f"core-bar-{i + 1}", classes = "core-bar")

        with Container(classes = "row"):
            yield Label(id = "cpu-usage")
            yield Static(classes = "spacer")
            yield Label(id = "user")
            yield Static(classes = "spacer")
            yield Label(id = "system")
            yield Static(classes = "spacer")
            yield Label(id = "idle")
            yield Static(classes = "spacer")
            yield Label(id = "frequency")