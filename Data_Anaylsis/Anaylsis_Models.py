# coding=utf-8
import pandas as pd
from scipy.stats import f
import matplotlib.pyplot as plt
from sklearn import model_selection
import statsmodels.api as sm
import numpy as np

'''一元线性回归模型计算'''
simple_learn_data = pd.read_excel('./Data/data_test02.xlsx', sheet_name='Piazz')
# print(type(simple_learn_data))
# print(simple_learn_data.head())  # 查看前n行
# fit = sm.formula.ols('Diameter~Price', data=simple_learn_data).fit()#一元线性回归模型参数计算,ols翻译为最小二乘法
# print(fit.params)
# print('Diameter={0}+{1}Price'.format(fit.params['Intercept'], fit.params['Price']))
# print(fit.summary())
# # 画图
# x_data = simple_learn_data.loc[:, 'Diameter'].values
# y_data = simple_learn_data.loc[:, 'Price'].values
# plt.figure()
# plt.title('Piazz size and price')
# plt.xlabel('Diameter')
# plt.xlabel('Price')
# plt.xlim(0, 25)
# plt.ylim(0, 25)
# plt.plot(x_data, y_data, 'k.')#散点图
# plt.show()
# dat = sm.datasets.get_rdataset(simple_learn_data).data
# print(dat)


'''
多元线性回归模型
'''
# mul_learn_data = pd.read_excel('./Data/data_test02.xlsx', sheet_name='Sales')
# print(mul_learn_data.head())
# # # 将数据集拆分成训练集和测试集
# train, test = model_selection.train_test_split(mul_learn_data, test_size=0.2, random_state=123)
# print(train)
# print(test)
# model = sm.formula.ols('sales~TV+Radio+newspaper', data=train).fit()
# print('模型的片回归系数分别为\n', model.params)
# # 删除test数据总的sales变量，用剩下的变量进行预测
# text_X = test.drop(labels='sales', axis=1)
# pred = model.predict(exog=text_X)
# print('对比预测值和实际值的差异:\n', pd.DataFrame({'Prediction': pred, 'Read': test.sales}))
# # 计算相关系数，结果越接近1，数据之间的相关性就越高
# print(simple_learn_data.corr(method='pearson', min_periods=3))
# print(mul_learn_data.columns)
# print(mul_learn_data.corrwith(mul_learn_data['sales']))  # 其他变量与sales的相关系数
# print(mul_learn_data.drop('sales', axis=1).corr())  # 去掉某一列，此处为sales列，后进行两两相关系数求解
# print(mul_learn_data.drop(['sales', 'TV'], axis=1).corr())

'''
线性回归模型的假设检验-F检验（验证模型的合理性-因变量的系数不全为零）
'''
# avg_sales = train.sales.mean()#sales的平均值
# #统计变量个数和观测个数
# p = model.df_model
# n = train.shape[0]
# print(p)
# print(n)
# #计算回归离差平方和
# RSS = np.sum((model.fittedvalues - avg_sales) ** 2)
# print(RSS)
# #计算误差平方和
# ESS = np.sum(model.resid ** 2)
# print(ESS)
# #计算总平方和
# TSS = RSS + ESS
# #计算F用计量的值
# F = (RSS/p) / (ESS/(n-p-1))
# print(F)
# #计算F检验的理论值
# f_theroy = f.ppf(q=0.95, dfn=p, dfd=n-p-1)
# print(f_theroy)
# #F远大于f_theroy时，表明模型时有效的

'''
线性回归模型的假设检验-t检验（验证模中因变量系数的合理性-都不为零）
原假设：有因变量的系数的值=0
备用假设：所有因变量的系数都不等于0
'''
# print(model.summary())#获取的t值的绝对值>2则表示原假设被拒绝，p值<=0.05也可表示拒绝原假设

