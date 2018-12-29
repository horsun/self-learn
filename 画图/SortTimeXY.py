import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.1, 100)

plt.title("time complexity")
plt.scatter(x, x * (np.log2(x)), s=0.5, alpha=0.5, label='O(n*logn)')  # O(nlogn) 时间复杂度
plt.scatter(x, x, s=0.5, alpha=0.5, label='O(n)')  # O(nlogn) 时间复杂度
plt.scatter(x, x * x, s=0.5, alpha=0.5, label='O(n²)')  # O(n²)时间复杂度
plt.legend(loc='best')
plt.show()
