#!/usr/bin/env python
#coding=utf8
import matplotlib.pyplot as plt
import numpy as np
from numpy import exp,sqrt
from scipy.stats import norm
import signals, output_res

Q=0.8;R=0.2;y=0;x=0#начальные дисперсии шумов(выбраны произвольно) и нулевые значения  переменных.
P=Q*R/(Q+R)# первая оценка дисперсий шумов.
T=5.0#постоянная времени.
n=[];X=[];Y=[];Z=[]#списки для переменных.
for i in np.arange(0,100,0.2):
                n.append(i)#переменная времени.
                x=1-exp(-1/T)+x*exp(-1/T)#модельная функция для x.
                y=1-exp(-1/T)+y*exp(-1/T)# модельная функция для y.
                Y.append(y)#накопление списка значений y.
                X.append(x)# накопление списка значений x.
                norm1 = norm(y, sqrt(Q))# нормальное распределение с #математическим ожиданием – y.
                norm2 = norm(0, sqrt(R))# ))# нормальное распределение с #математическим ожиданием – 0.
                ravn1=np.random.uniform(0,2*sqrt(Q))#равномерное распределение #для шума с дисперсией Q.
                ravn2=np.random.uniform(0,2*sqrt(R))# равномерное распределение #для шума с дисперсией R.
                z=norm1.pdf( ravn1)+norm2.pdf(ravn2)#измеряемая переменная z.
                Z.append(z)# накопление списка значений z.
                P=P-(P**2)/(P+Q+R) #переход в новое состояние для x.
                x=(P*z+x*R)/(P+R)# новое состояние x.
                P=(P*R)/(P+R)# прогноз для нового состояния x.
plt.plot(n, Y, color='g',linewidth=4, label='Y')
plt.plot(n, X, color='r',linewidth=4, label='X')
plt.plot(n, Z, color='b', linewidth=1, label='Z')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# output_res.write_to_file(Z, 'signals/adaptive_func_w_noise.txt')
