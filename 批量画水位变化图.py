import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl

mpl.rcParams['font.sans-serif']=['SimHei'] #黑体


文件名 = input()
    


path = rf'图表\{文件名}.xlsx'
data = pd.read_excel(path,header=None,usecols=[0,1])


plt.figure(figsize=(6, 6))
plt.scatter(data[0], data[1],s = 1)
plt.xlabel('时间/s',fontsize=10,color='k')
plt.ylabel('水位/m',fontsize=10,color='k')

ax=plt.axes()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

name = path.strip('r')
name = name.replace('图表','')
name = name.replace('.xlsx','')
#清洗文件名

plt.savefig(rf"E:\202142_微水试验报告\水位图\{name}.png",bbox_inches ='tight',dpi=400)
