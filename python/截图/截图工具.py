import PIL
from PIL import ImageGrab


# 参数说明  
# 第一个参数 开始截图的x坐标  
# 第二个参数 开始截图的y坐标  
# 第三个参数 结束截图的x坐标  
# 第四个参数 结束截图的y坐标  
bbox = (760, 0, 1160, 1080)  
im = ImageGrab.grab(bbox)  

# 参数 保存截图文件的路径  
im.save('as.png')
