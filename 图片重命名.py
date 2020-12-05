import sys
import os

lines = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    lines.append(line)
#接受终端多行数据输入

filenames = os.listdir(os.getcwd()) 
a = filenames.pop()

x = len(a) + 1

for i in range(0,x):
     os.rename(filenames[i],lines[i]+'.jpg')