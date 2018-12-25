# url :https://wizardforcel.gitbooks.io/scipycon-2018-sklearn-tut/content/6.html
import numpy as np
import matplotlib.pyplot as plt

# 从-3 -> 3 中取出 100条随机数
x = np.linspace(-3, 3, 100)

print(x)

rng = np.random.RandomState(0)
print(rng.uniform(size=len(x)))
y1 = np.sin(4 * x)
y2 = np.sin(4 * x) + x
y = np.sin(4 * x) + x + rng.uniform(size=len(x))

plt.plot(x, y1, 'x')
plt.title('normal sin()')
plt.show()

plt.plot(x, y2, 'x')
plt.title('sin() + x ')
plt.show()

plt.plot(x, y, 'x')
plt.title('sin()+ x + random num')
plt.show()
