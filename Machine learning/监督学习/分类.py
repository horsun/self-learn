from sklearn.datasets import make_blobs
# url:https://wizardforcel.gitbooks.io/scipycon-2018-sklearn-tut/content/5.html
x, y = make_blobs(centers=2, random_state=0, cluster_std=1.5)
print("x:", x)
print("Y", y)
print("X shape", x.shape)
print("Y Shape", y.shape)
print('first 5 samples: \n', x[:5, :])
print(x[:5])
import matplotlib.pyplot as plt

# plt.figure(figsize=(8, 8))
# [y==0,0] 第一个0 代表 y的value 是否为零 第二个 某列
# plt.scatter(x[y == 0, 0], x[y == 0, 1], s=40, label='0')
# plt.scatter(x[y == 1, 0], x[y == 1, 1], s=40, label='1', marker='s')
# plt.xlabel('first feature')
# plt.ylabel('second feature')
# plt.legend(loc='upper right')
# plt.show()

# 训练模型
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1234, stratify=y)
from sklearn.linear_model import LogisticRegression

# 训练分析
classifier = LogisticRegression()
classifier.fit(x_train, y_train)
prediction = classifier.predict(x_test)
print(prediction)
print(y_test)
import numpy as np

print(np.mean(prediction == y_test))
print(classifier.score(x_test, y_test))
print(classifier.score(x_train, y_train))
