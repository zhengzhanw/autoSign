__author__ = 'v_zhwzheng'
import os
from PIL import Image

import pytesseract


threshold = 140
table = []
name = 'code.png'
im = Image.open(name)
#转化到灰度图
imgry = im.convert('L')
#保存图像
imgry.save('g'+name)
#二值化，采用阈值分割法，threshold为分割点
for j in range(256):
    if j < threshold:
        table.append(0)
    else:
        table.append(1)
out = imgry.point(table, '1')
out.save('b'+name)
#识别
text = pytesseract.image_to_string(out)
#识别对吗
text = text.strip()
text = text.upper();
print (text)
text = pytesseract.image_to_string(Image.open('code.png'), lang="eng")
print(text)