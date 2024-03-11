# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 15:04:58 2024

@author: 86137
"""
## 1.1
import numpy as np
import matplotlib.pyplot as plt ## 绘图
import pandas  ## 读取Excel数据
import math ## 求阶乘
from scipy.optimize import minimize ## 求函数最小值对应的参数

def Gass(value, mean, sigma):
    '''创建高斯分布并返回value对应的概率值'''
    return 1/(sigma*np.sqrt(2*np.pi))*np.exp(-(value-mean)**2/(2*sigma**2))

def Lik(ob1, ob2, mean, sigma1, sigma2):
    '''由独立表征推出似然函数'''
    return Gass(ob1, mean, sigma1)*Gass(ob2, mean, sigma2)

σ1 = 1
σ2 = 1
s1 = -1
s2 = 1
'''基于给出的s和σ预估刺激值范围(m±3*σ)'''
omega = np.linspace(-4, 4, num = 1000)
lik = Lik(s1, s2, omega, σ1, σ2)
omegaMLE = omega[lik.argmax()]
print("刺激ω的值为：%s"%omegaMLE)

'''作图'''
plt.figure(figsize=(10, 10))
plt.plot(omega, lik, color = 'pink', label = 'likelihood', lw=3)
plt.xlabel('stimulus')
plt.ylabel('lik_value')
plt.title('likelihood')
plt.show()

## 1.2
'''重新定义s2的值并求出对应刺激预测值'''
s2 = np.linspace(-2, 2, num = 1000)
predict = np.array(omega[Lik(s1, s2[0], omega, σ1, σ2).argmax()])
for i in s2[1:]:
    predict = np.append(predict, omega[Lik(s1, i, omega, σ1, σ2).argmax()])
'''作图'''
plt.figure(figsize=(10, 10))
plt.plot(s2, predict, color = 'pink', lw=3)
plt.xlabel('s2_value')
plt.ylabel('expect_omega')
plt.title('omega_with_s2')

'''计算不同s2下的参数估计'''
'''确定抽取数据集：Lik(s1, s2, omega, σ1, σ2); 确定抽取次数：1000; 创建对应均值集'''
times = 1000
means_0 = np.zeros(times)
'''自举抽样过程模拟'''
for i in range(times):
    means_0[i] =  np.mean(np.random.choice(Lik(s1, 0, omega, σ1, σ2), size = len(omega), replace = True))
'''计算置信区间并绘图'''


## 1.3
'''重新定义σ2的值并求出对应刺激预测值'''
σ2 = np.linspace(0.25, 4, num = 1000)
pred = np.array(omega[Lik(-1, 1, omega, 1, σ2[0]).argmax()])
for i in σ2[1:]:
    pred = np.append(pred, omega[Lik(-1, 1, omega, 1, i).argmax()])
'''作图'''
plt.figure(figsize=(10, 10))
plt.plot(σ2, pred, color = 'pink', label = 'stimulus-s', lw=3)
plt.xlabel('σ2_value')
plt.ylabel('expect_omega')
plt.title('omega_with_σ2')
'''由图可知，随着σ2的增大，刺激值的预测值越接近于-1，即s1，说明s2的预测权重降低；
从认知的层面上可以解读为：由于该感觉通路对同一刺激表征浮动较大，个体在对刺激值的预测时
会更少地整合该感觉通路传来的信息。'''


## 2.1
data = pandas.read_csv('C:/Users/86137/Desktop/Class/大二下/认知建模基础/homework/hw-2/L02Q2.csv')
def Possion(lamda, value):
    '''创建泊松分布并返回value对应的概率值'''
    return math.exp(-lamda) * (lamda**value) / math.factorial(value)

def Rescorla_Wagner(params, stimulus, reward, spike, start_w):
    '''依据Rescorla_Wagner计算出预测值'''
    learning_rate = params[0]
    '''初始化联结强度V、预测值列表、权重列表'''
    V = 0
    pred = []
    weight = [start_w]
    for idx in range(len(stimulus)):
        delta = reward[idx] - V
        lamda = max(0.1, 3 + 3*delta)
        predict = Possion(lamda, spike[idx])
        pred.append(predict)
        if idx == 0:
            pass
        else:
            weight.append(weight[-1] + learning_rate*(predict-V)*stimulus[idx])
        V += learning_rate*(predict-V)*stimulus[idx]**2
    return pred, weight

def error_prediction(params, stimulus, reward, spike, start_w):
    '''创建误差函数'''
    predict_values, weight = Rescorla_Wagner(params, stimulus, reward, spike, start_w)
    error = np.mean((predict_values - spike)**2)
    return error

stimulus = data['stimulus'].values
spike = data['spike'].values
reward = data['reward'].values
learning_rate = [0.5]
start_w = 0
result = minimize(error_prediction, learning_rate, args=(stimulus, reward, spike, start_w))
print("拟合的学习参数为：%s"%result.x[0])


## 2.2
'''绘图刺激序列'''
plt.figure(figsize=(20, 6))
trials = np.arange(len(stimulus))
plt.subplot(3, 1, 1)
plt.plot(trials, stimulus, 'o-', color = 'blue', lw = 2)

'''绘图误差变化和权重变化'''
predict, weight = Rescorla_Wagner(result.x, stimulus, reward, spike, start_w)
plt.subplot(3, 1, 2)
plt.plot(trials, predict, 'o-', color = 'red', lw = 2)
plt.subplot(3, 1, 3)
plt.plot(trials, weight, 'o-', color = 'pink', lw = 2)




