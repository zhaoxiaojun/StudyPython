#coding=utf8
import matplotlib.pyplot as plt

plt.figure('plot_name',figsize=(10,8),dpi=80)
#plt.subplots_adjust(left=0.08,right=0.95,bottom=0.05,top=0.95,hspace=0.75)

subplt = plt.subplot(2,2,2)
subplt.set_title('title: hello world')  #设置标题

#设置横纵坐标
subplt.set_ylim(0, 6)
subplt.set_xlim(0, 6)

#描绘一条线
x = (1,5)
y = (0,4)
subplt.plot(x,y,color='r',linewidth=1.5,linestyle='-',label='label1')

subplt.legend() #显示图例
subplt.grid(True) #显示网格

#显示横纵坐标label
subplt.set_xlabel('x_label',{'color':'b'})
subplt.set_ylabel('y_label', {'color':'g'})

#显示出来
plt.show()
