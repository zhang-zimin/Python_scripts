import shutil
import os


dir1 = r"E:\test\1"
dir2 = r"E:\test\2"
# print(os.path.join(dir,'1'))

files =os.listdir(r"E:\test\1")
for j in range(1,1501):
    data = ''
    for i in files:
        后缀名 = i.split('.')[-1]
        shutil.copy(os.path.join(dir1,i),os.path.join(dir2,str(j)+'.'+后缀名))
    with open(r"E:\test\1\new.mfn",'r') as f:
        for line in f:
            new_name = str(j)
            line = line.replace('new',new_name)
            data += line
    with open(rf"E:\test\2\{j}.mfn",'w',encoding='utf-8') as f:
        f.write(data)
