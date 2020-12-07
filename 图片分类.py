import os
import shutil

path = r'D:\GeoCAD Tools 3.3\图片\待处理图片'
path2 = r'D:\GeoCAD Tools 3.3\图片'
files_list = os.listdir(path)
文件夹名称 = os.listdir(path2)
孔号列表 = []

for file in files_list:
    图片名称, suffix = os.path.splitext(file)
    孔号 = 图片名称.split('-')[0]
    孔号列表.append(孔号)

孔号列表 = list(set(孔号列表))
for i in range(len(文件夹名称)):
    for a in range(len(孔号列表)):
        if  文件夹名称[i] != 孔号列表[a]:
            try:
                os.makedirs(path2+'\\'+孔号列表[a])
            except OSError:
                pass
#如果以前没有这个孔号的文件夹就创建一个新的文件夹
for file in files_list:
    for x in 文件夹名称:
        图片名称, suffix = os.path.splitext(file)
        孔号 = 图片名称.split('-')[0]
        if 孔号 == x:
            shutil.move(path+'\\'+file,path2+'\\'+x)
#把岩性照片添加到对应的文件夹中
