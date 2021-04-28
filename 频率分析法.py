import pandas as pd  #pandas后续以pd简写表示
import math 
import numpy as np   #numpy后续以np简写表示
import matplotlib.pyplot as plt  #matplotlib绘图包后续以plt简写表示

#导入数据
文件路径 = r'E:\2020330_x\合肥市降雨量统计.xlsx'
降雨文件 = pd.read_excel(文件路径)      #导入降雨文件 
降雨量 = 数据['降雨量']                 #读取降雨表格

#统计参数
降雨量均差 = np.mean(降雨量)
降雨量标准差 = np.std(降雨量)
Cs = 降雨量.skew()                     #计算降雨偏度系数Cs
Cv = 降雨量标准差/降雨量均差             #计算降雨变差系数Cv
最大降雨量 = max(降雨量)

#计算P-III型分布频率曲线参数
α = 4/Cs**2
β = 2/(降雨量均差*Cs*Cv)
a0 = 降雨量均差*(1-2*Cv/Cs)

#构造降雨等差序列
极端最大降雨量 = 最大降雨量 + 3*降雨量标准差
降雨等差序列=[i for i in range(math.ceil(极端最大降雨量/10)*10,math.floor(a0/10)*10,-10)] 

#计算P-III型分布频率各点的概率密度函数值
各点函数值的集合 = []                      #创建函数值集合
for i in range(len(降雨等差序列)):
    f = β**α/math.gamma(α)*(降雨等差序列[i]-a0)**(α-1)*math.exp(-(降雨等差序列[i]-a0)*β)  #概率密度函数公式
    各点函数值的集合.append(f)

#计算P-III型分布频率各点的概率密度函数值
年函数值集合 = [0]
for i in range(1,len(各点函数值的集合)):
    年函数值=(各点函数值的集合[i-1]+各点函数值的集合[i])*(降雨等差序列[i-1]-降雨等差序列[i])/2
    年函数值集合.append(年函数值)

#绘制P-III型概率密度曲线    
plt.bar(range(len(年函数值集合)),年函数值集合)
plt.xlabel('x')
plt.ylabel('P')
plt.show

#对密度曲线积分
累计概率 = []
for i in range(len(年函数值集合)):
    累计概率.append(sum(年函数值集合[:i+1]))

百年一遇频率 = 1/100 

#计算百年一遇降雨量
for i in range(len(累计概率)):
    if 百年一遇频率>=累计概率[i] and 百年一遇频率<累计概率[i+1]:
       百年一遇降雨量 =降雨等差序列[i]+(百年一遇频率-累计概率[i])/(累计概率[i+1]-累计概率[i])*(降雨等差序列[i+1]-降雨等差序列[i])

print(f'合肥市百年一遇降雨量为{round(百年一遇降雨量,2)}mm')
