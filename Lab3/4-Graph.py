import matplotlib.pyplot as plt
import numpy as np

x = [i for i in np.arange(-5, 6, 0.1)]
y1 = [3 * x1 * x1 * x1 + 2 * x1 * x1 - x1 + 5 for x1 in x]
y2 = [2 * x2 * x2 - 1.5 * x2 - 10 for x2 in x]

ans = [abs(a - b) for a, b in zip(y1, y2)]
print(x[ans.index(min(ans))])
# print(min(ans))
plt.plot(x, y1, "b")
plt.plot(x, y2, "y")
plt.show()
