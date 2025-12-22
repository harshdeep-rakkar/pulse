from psutil import virtual_memory, swap_memory
from textual.containers import Container
from textual.widgets import Label

from plot import Plot

class Memory(Container):
    DEFAULT_CSS = """
    Memory {
        height: auto;
    }

    #virtual-memory-plot {
        height: 12;
    }

    .labels {
        margin-top: 2;
        layout: grid;
        grid-size: 2;
        grid-gutter: 1 0;
        height: auto;
    }

    .labels > .column1 {
        content-align: left middle;
        width: 1fr;
    }

    .labels > .column2 {
        content-align: right middle;
        width: 1fr;
    }
    """

    def __init__(self):
        super().__init__()
        self.history: list[float] = [0.0] * 60

    def compose(self):
        yield Plot(id = "virtual-memory-plot")

        with Container(classes = "labels"):
            yield Label(id = "used-memory", classes = "column1")
            yield Label(id = "used-swap", classes = "column2")
            yield Label(id = "total-memory", classes = "column1")
            yield Label(id = "total-swap", classes = "column2")
    
    def on_mount(self):
        self.update_data()
        self.set_interval(1.0, self.update_data)

    def update_data(self):
        virtual_memory_info = virtual_memory()
        swap_memory_info = swap_memory()

        used_virtual_memory = round(virtual_memory_info.used / (1024 ** 3), 2)
        total_virtual_memory = round(virtual_memory_info.total / (1024 ** 3), 2)

        used_swap_memory = round(swap_memory_info.used / (1024 ** 3), 2)
        total_swap_memory = round(swap_memory_info.total / (1024 ** 3), 2)

        self.query_one("#used-memory", Label).update(f"Used memory: {used_virtual_memory} GB")
        self.query_one("#total-memory", Label).update(f"Total memory: {total_virtual_memory} GB")

        self.query_one("#used-swap", Label).update(f"Used swap memory: {used_swap_memory} GB")
        self.query_one("#total-swap", Label).update(f"Total swap memory: {total_swap_memory} GB")

        self.history.append(used_virtual_memory)
        self.history.pop(0)

        plot_widget = self.query_one("#virtual-memory-plot", Plot)
        graph = plot_widget.plt

        graph.clear_figure()
        
        graph.plot(self.history, marker = "braille", fillx = True, color = "red")
        graph.ylim(0, total_virtual_memory)
        graph.title("Virtual Memory Usage (GB)")
        graph.xlabel("Seconds")
        graph.yticks([0, round(total_virtual_memory / 2, 2), total_virtual_memory])
        graph.xticks([0, 30, 60])
        graph.canvas_color((25, 25, 25))
        graph.ticks_color((255, 255, 255))
        graph.axes_color((25, 25, 25))
        plot_widget.refresh()