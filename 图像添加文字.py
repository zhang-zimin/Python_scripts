from PIL import Image 
from PIL import ImageFont
from PIL import ImageDraw
import os

folder = os.listdir(r'E:\文件资料\西霞院\震荡实验曲线')


for name in folder:
    src = r'E:\文件资料\西霞院\震荡实验曲线\渠道左岸东井-1.png'

    font = ImageFont.truetype("simsun.ttf", 60)

    img = Image.open(src)

    title = name.split(".")[0]

    draw = ImageDraw.Draw(img)
    
    draw.text((1050, 0),title,(0,0,0),font=font)

    img.save(r'E:\文件资料\西霞院\震荡试验曲线(修改)' + '\\'+ name)
