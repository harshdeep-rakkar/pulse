import random
import plotext
from rich.text import Text

count = 60
start = 0
end = 100

numbers = [random.randint(start, end) for _ in range(count)]

plotext.plot(numbers, marker = "braille", fillx = True, color = (220, 60, 100))
plotext.title("Memory Usage (GB)")
plotext.ylim(0, end)
plotext.yticks([0, round(end / 2, 2), end])
plotext.xticks([0, 30, 60])
plotext.canvas_color((25, 25, 25))
plotext.ticks_color((255, 255, 255))
plotext.axes_color((25, 25, 25))

print(Text.from_ansi(plotext.build()))