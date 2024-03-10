import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
fig = plt.figure()

ax = plt.axes()
x = np.linspace(0, 100, 1000)
ax.plot(x, np.sin(x))
plt.show()
