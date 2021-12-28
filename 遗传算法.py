import numpy as np
import torch
import time
from sko.GA import GA
import flopy.utils.binaryfile as bf
import pandas as pd
import flopy
import matplotlib.pyplot as plt


def MOD(a,b,c,d):            # MODFLOW程序
    model = flopy.modflow.Modflow.load(r"E:\文件资料\大论文\MODFLOW\genetic\model_MODFLOW_text\model.mfn", 
                                            exe_name = r'D:\GMS10.5\models\mf2k5\usgs\mf2005.exe')
    wel_spd = {0: [[0, 0, 0, a], [0, 0, 9,b],[0,6,0,c],[0,6,9,d]],      #[lay, row, col, flux]
              1: [[0, 0, 0, a], [0, 0,9,b],[0,6,0,c],[0,6,9,d]]}
    wel = flopy.modflow.ModflowWel(model, stress_period_data = wel_spd)
    model.write_input()
    model.run_model()
    hds = bf.HeadFile('model' + ".hed") # 获取水头文件
    head = hds.get_data() # 提取水头值
    df1 = pd.DataFrame(head[0])
    plt.subplot(121)
    plt.title('head')
    plt.imshow(df1,cmap='RdBu')
    plt.colorbar()
    plt.show(block=False)

    # df = df.drop([0,1,2,7,8,9],axis=0)       # 删除多余行
    # df = df.drop([0,1,2,7,8,9],axis=1)       # 删除多余列
    水位值 = df1.iloc[4,4]
    print(水位值)

    vds = bf.HeadFile('model' + ".vert_dis",text='Z DISPLACEMENT') # 获取沉降文件
    vd = vds.get_data() # 提取沉降值
    df2 = pd.DataFrame(vd[0])
    plt.subplot(122)
    plt.title('subsidence')
    plt.imshow(df2,cmap='Greys')
    plt.colorbar()
    plt.pause(0.001)
    plt.clf()

    沉降值 = df2.iloc[4,4]
    print(沉降值)

    return 水位值,沉降值


def obj_func(p):
    a,b,c,d,e,f,g,h= p
    水位值,沉降值 = MOD(a*e,b*f,c*g,d*h)
    A = e*(120 + 1.2*np.abs(a))
    B = f*(130 + 1.3*np.abs(b))
    C = g*(140 + 1.4*np.abs(c))
    D = h*(150 + 1.5*np.abs(d))
    return 100*np.abs(水位值-98)+100*np.abs(沉降值)+A+B+C+D

fig=plt.figure(figsize=(9,3))

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
ga = GA(func=obj_func, n_dim=8, size_pop=100, prob_mut=0.01,max_iter=10, lb=[-50,-50,-50,-50,0,0,0,0], ub=[0,0,0,0,1,1,1,1], 
        precision=[1e-3,1e-3,1e-3,1e-3,1,2,3,4])
ga.to(device=device)
start_time = time.time()
best_x, best_y = ga.run()
print(time.time() - start_time)
print('best_x:', best_x, '\n', 'best_y:', best_y)

Y_history = pd.DataFrame(ga.all_history_Y)
fig, ax = plt.subplots(1, 1)
Y_history.min(axis=1).cummin().plot(kind='line')
plt.show()
