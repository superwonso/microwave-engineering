# Problem : Draw ar = 2 circle on a Smith chart.
import matplotlib.pyplot as plt
import numpy as np
ar = 2
r = np.linspace(0, ar, 100)
theta = np.linspace(0, 2*np.pi, 100)
x = r*np.cos(theta)
y = r*np.sin(theta)
plt.plot(x, y)
plt.show()