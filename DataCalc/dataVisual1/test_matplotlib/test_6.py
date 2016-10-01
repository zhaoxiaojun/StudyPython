#coding=utf8
from pylab import *

'''
饼状图
'''

n = 20
Z = np.ones(n)
Z[-1] *= 2

plt.axes([0.025,0.025,0.95,0.95])

plt.pie(Z, explode=Z*.05, colors = ['%f' % (i/float(n)) for i in range(n)])
plt.gca().set_aspect('equal')
plt.xticks([]), plt.yticks([])

savefig('./figures/pie_ex.png',dpi=48)
plt.show()
