from textual.widgets import Static
from rich.text import Text
import plotext as plt

class Plot(Static):
    @property
    def plt(self):
        return plt
    
    def on_resize(self):
        self.refresh()
    
    def render(self):
        width = self.size.width
        height = self.size.height  
        plt.plotsize(width, height)
        output = plt.build()

        return Text.from_ansi(output)