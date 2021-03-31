import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])
# 安装
# python -m pip install PIL

from PIL import Image, ImageOps
im = Image.open('测试用图片.jpg')
im_mirror = ImageOps.mirror(im) # 做镜面转换
im_mirror.save('m_测试用图片.jpg') # 保存镜像图片