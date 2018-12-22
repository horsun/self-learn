import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# 获取数据 iris
iris = load_iris()
print('data:\n ', iris)

# 找到规律所在的index 即 所在的列
x_index = 3
# 通过类别 分别进行数据呈现
for label in range(len(iris.target_names)):
    print("label:", label)
    plt.hist(iris.data[iris.target == label, x_index],
             label=iris.target_names[label],
             alpha=0.5)

plt.xlabel(iris.feature_names[x_index])
plt.legend(loc='upper right')
plt.show()

x_index = 3
y_index = 0

for label in range(len(iris.target_names)):
    plt.scatter(iris.data[iris.target == label, x_index],
                iris.data[iris.target == label, y_index],
                label=iris.target_names[label])

plt.xlabel(iris.feature_names[x_index])
plt.ylabel(iris.feature_names[y_index])
plt.legend(loc='upper left')
plt.show()
