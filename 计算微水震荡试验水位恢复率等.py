import pandas as pd
import numpy as np
import os

def getfiles():
    files = []
    filenames=os.listdir()
    for file in filenames:
        if '.xlsx' in file:
            files.append(file)
    return files

for path in getfiles():
    data = pd.read_excel(path,sheet_name='Sheet1',header=None,usecols=[0,1])
    
    激发前水位 = data[1][0]
    data = data[data[1]>激发前水位]#去除小于激发前水位的值
    行数 = data.shape[0] 
    水位恢复稳定值 = data[1][行数]
    水位恢复后的稳定值 = data[-1:-3]
    激发水位 = data[1].max()
    激发时间 = int(np.where(data==激发水位)[0][0])
    水位恢复时间 = data.shape[0] - 激发时间 
    水位抬升 = 激发水位 - 激发前水位
    水位恢复 = 激发水位 - 水位恢复稳定值
    水位恢复率 = 水位恢复/水位抬升*100
    钻孔 = path.split('.')[0]
    print(钻孔,水位抬升*100,水位恢复*100,水位恢复率,水位恢复时间)

