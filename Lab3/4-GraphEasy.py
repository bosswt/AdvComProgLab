import matplotlib.pyplot as plt
import numpy as np

x = [i for i in np.arange(-5, 6, 0.1)]
y1 = [3 * x1 * x1 * x1 + 2 * x1 * x1 - x1 + 5 for x1 in x]
y2 = [2 * x2 * x2 - 1.5 * x2 - 10 for x2 in x]

diff = []
for i in range(0, len(x)):
    a = 3 * x[i] * x[i] * x[i] + 2 * x[i] * x[i] - x[i] + 5
    b = 2 * x[i] * x[i] - 1.5 * x[i] - 10
    diff.append([abs(a - b), i])
print(x[sorted(diff)[0][1]])
plt.plot(x, y1, "b")
plt.plot(x, y2, "y")
plt.show()
