import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import svm
from matplotlib import colors
import matplotlib as mpl
import matplotlib.pyplot as plt


def init_type(name):
    type_name = {
        b"Iris-setosa": 0,
        b"Iris-versicolor": 1,
        b"Iris-virginica": 2,
    }
    return type_name[name]


# converters用于将分类转为数字 调用上面的方法 {<index>:<function>}
# delimiter 用于切割soua
data = np.loadtxt('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
                  delimiter=',',
                  converters={4: init_type},
                  )

# split(数据，
#       分割位置，
#       轴=1（水平分割） or 0（垂直分割）)。
# 相当于把 value 和 sort split开
x, y = np.split(data,
                (4,),
                axis=1)

# numpy对象切割,取前俩列
# [<行切割>,<列切割>]
x = x[:, :2]

# train_test_split( train_data,#样本
#                   train_target,#样本结果
#                   test_size=数字,#样本占比，如果是整数的话就是样本的数量
#                   random_state=0,#随机数的种子
#                   )
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.6)
# clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
clf = svm.SVC(C=0.8, kernel='linear', gamma=20, decision_function_shape='ovr')
clf.fit(x_train, y_train.ravel())

print(clf.score(x_train, y_train))  # 精度
y_hat = clf.predict(x_train)

print(clf.score(x_test, y_test))
y_hat2 = clf.predict(x_test)

x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False

cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])

grid_hat = clf.predict(grid_test)  # 预测分类值
grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同

alpha = 0.5
plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)  # 预测值的显示
plt.plot(x[:, 0], x[:, 1], 'o', alpha=alpha, color='blue', markeredgecolor='k')
plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10)  # 圈中测试集样本
plt.xlabel(u'length', fontsize=13)
plt.ylabel(u'width', fontsize=13)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title(u'sort', fontsize=15)
plt.show()
