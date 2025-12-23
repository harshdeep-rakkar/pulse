from textual.widgets import Static
from textual.reactive import reactive

class WidthIndicator(Static):
    DEFAULT_CSS = """
    WidthIndicator {
        content-align: center middle;
    }
    """

    width_value = reactive(0)
    
    def on_mount(self):
        self.update_width()
    
    def on_resize(self):
        self.update_width()
    
    def update_width(self):
        self.width_value = self.app.size.width
    
    def watch_width_value(self, width):
        self.update(f"Screen Width: {width}")