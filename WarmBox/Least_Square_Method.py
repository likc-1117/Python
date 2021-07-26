#coding:utf-8
import numpy as np
import scipy as sp
#import matplotlib.pyplot as plt
from scipy.optimize import leastsq

class least_square_method:
    #Xi=np.array([35,40,44,48,51,58])
    #Yi=np.array([36,41,46,50,54,61])


    def __init__(self,Xi,Yi):
        self.Xi=np.array(Xi)
        self.Yi=np.array(Yi)
    '''
        设定拟合函数和偏差函数
        函数的形状确定过程：
        1.先画样本图像
        2.根据样本图像大致形状确定函数形式(直线、抛物线、正弦余弦等)
    '''

    ##需要拟合的函数func :指定函数的形状
    def func(self,p,x):
        k,b=p
        return k*x+b

    ##偏差函数：x,y都是列表:这里的x,y更上面的Xi,Yi中是一一对应的
    def error(self,p,x,y):
        return self.func(p,x)-y

    '''
        主要部分：附带部分说明
        1.leastsq函数的返回值tuple，第一个元素是求解结果，第二个是求解的代价值(个人理解)
        2.官网的原话（第二个值）：Value of the cost function at the solution
        3.实例：Para=>(array([ 0.61349535,  1.79409255]), 3)
        4.返回值元组中第一个值的数量跟需要求解的参数的数量一致
    '''

    def do_leastsq(self):
        #k,b的初始值，可以任意设定,经过几次试验，发现p0的值会影响cost的值：Para[1]
        p0=[1,5]

        #把error函数中除了p0以外的参数打包到args中(使用要求)
        Para=leastsq(self.error,p0,args=(self.Xi,self.Yi))

        #读取结果
        k,b=Para[0]
        return (k,b)
    '''
       绘图，看拟合效果.
       matplotlib默认不支持中文，label设置中文的话需要另行设置
       如果报错，改成英文就可以
    '''
    '''
    #画样本点
    plt.figure(figsize=(8,6)) ##指定图像比例： 8：6
    plt.scatter(Xi,Yi,color="green",label="样本数据",linewidth=2)
    
    #画拟合直线
    x=np.linspace(0,12,100) ##在0-15直接画100个连续点
    y=k*x+b ##函数式
    plt.plot(x,y,color="red",label="拟合直线",linewidth=2)
    plt.legend(loc='lower right') #绘制图例
    plt.show()'''

