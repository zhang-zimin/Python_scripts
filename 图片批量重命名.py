import sys
import os

path= r'D:\GeoCAD Tools 3.3\图片\ZW26'
os.chdir(path)
#切换工作目录

lines = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    lines.append(line)
#接受终端多行数据输入

filenames = os.listdir(path) 
x = len(filenames) 
for i in range(0,x):
    os.rename(filenames[i],lines[i]+'.jpg')
#重命名图片

