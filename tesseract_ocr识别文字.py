#光学字符识别
import pytesseract as pt
from PIL import Image

img = Image.open('1.jpg')
text = pt.image_to_string(img,lang='chi_sim')
print(text)
