from time import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn import manifold, datasets

# 制造样本
n_points = 1000
X, color = datasets.samples_generator.make_s_curve(n_points, random_state=0)
n_neighbors = 10

fig = plt.figure(figsize=(5, 5))  #画板
#gs = fig.add_gridspec(1,2)  #共2副子图
ax1 = fig.add_subplot(121, projection='3d')  #第一幅子图表示原始样本分布
ax1.scatter(X[:, 0], X[:, 1], X[:, 2], c=color, cmap=plt.cm.Spectral)

# MDS降维
n_components = 2
t0 = time()  #计时开始
mds = manifold.MDS(n_components, max_iter=100, n_init=1)  #建立MDS模型
Y = mds.fit_transform(X)
t1 = time()  #计时结束
ax2 = fig.add_subplot(122)
ax2.scatter(Y[:, 0], Y[:, 1], c=color, cmap=plt.cm.Spectral)  #第2副子图表示降维后样本分布
ax2.set_title("MDS (%.2g sec)" % (t1 - t0))
ax2.xaxis.set_major_formatter(NullFormatter())
ax2.yaxis.set_major_formatter(NullFormatter())

plt.show()
