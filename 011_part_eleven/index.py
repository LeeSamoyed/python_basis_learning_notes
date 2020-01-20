#### import
# 使用导入的方式，引入函数
import importlib
fib = importlib.import_module('011_part_eleven.fib')

print(fib.fibonacci(1))
print(fib.fibonacci(3))
print(fib.fibonacci(10))


#### Pillow库使用
from PIL import Image, ImageFilter
im = Image.open('1.jpg')

box = (100 , 100 , 400 , 400)
region = im.crop(box)
region.save('result.jpg')