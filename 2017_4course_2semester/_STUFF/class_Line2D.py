import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
line = plt.Line2D([0, 1], [0, 2], color = "red")
ax.add_line(line)

plt.show()