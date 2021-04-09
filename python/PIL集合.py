import os
os.chdir(os.path.split(os.path.realpath(__file__))[0])
# 安装
#pip install PIL
import numpy as np
import base64
from io import BytesIO
from PIL import Image,ImageFilter,ImageDraw,ImageFont, ImageOps
pic_file = '测试用图片.jpg'
save_file = 's_' + pic_file
# 读取图片
def read_img():
    img = Image.open(pic_file)
    print(img.format, img.size, img.mode)
    print(img.info)
    # 显示图片
    img.show()
    # 保存图片
    img.save(save_file)

# 图片与array互转
def array():
    img = Image.open(pic_file)
    # Image转np.array
    arr = np.array(img)
    print(arr.shape)
    print(arr.dtype)
    # np.array转Image
    arr = (np.ones((256,256))*np.arange(0,256)).astype(np.uint8)
    img = Image.fromarray(arr)
    img.show()

# 图片与string互转
def pic_str():
    img = Image.open(pic_file)
    # Image转string
    buffer = BytesIO()
    img.save(buffer, 'PNG')
    b = buffer.getvalue()
    s = base64.b64encode(b).decode("utf-8")
    print(s[0:1000])
    # string转Image
    b = base64.b64decode(s.encode("utf-8"))
    buffer = BytesIO(b)
    img = Image.open(buffer)
    img.show()

# 由彩色转灰度
def convert():
    # 转成灰度
    img = Image.open(pic_file)
    img.convert("L").show()
    # PIL中有九种不同模式，分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F
    # 模式“1”为二值图像，非黑即白。但是它每个像素用8个bit表示，0表示黑，255表示白。
    # 模式“L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。在PIL中，从模式“RGB”转换为“L”模式是按照下面的公式转换的：L = R * 299/1000 + G * 587/1000+ B * 114/1000
    # 模式“P”为8位彩色图像，它的每个像素用8个bit表示，其对应的彩色值是按照调色板查询出来的。
    # 模式“RGBA”为32位彩色图像，它的每个像素用32个bit表示，其中24bit表示红色、绿色和蓝色三个通道，另外8bit表示alpha通道，即透明通道。
    # 模式“CMYK”为32位彩色图像，它的每个像素用32个bit表示。模式“CMYK”就是印刷四分色模式，它是彩色印刷时采用的一种套色模式，利用色料的三原色混色原理，加上黑色油墨，共计四种颜色混合叠加，形成所谓“全彩印刷”。四种标准颜色是：C：Cyan = 青色，又称为‘天蓝色’或是‘湛蓝’M：Magenta = 品红色，又称为‘洋红色’；Y：Yellow = 黄色；K：Key Plate(blacK) = 定位套版色（黑色）。
    # PIL中“RGB”转换为“CMYK”的公式如下：
    # C = 255 - R
    # M = 255 - G
    # Y = 255 - B
    # K = 0
    # 模式“YCbCr”为24位彩色图像，它的每个像素用24个bit表示。YCbCr其中Y是指亮度分量，Cb指蓝色色度分量，而Cr指红色色度分量。人的肉眼对视频的Y分量更敏感，因此在通过对色度分量进行子采样来减少色度分量后，肉眼将察觉不到的图像质量的变化。
    # 模式“RGB”转换为“YCbCr”的公式如下：
    # Y= 0.257*R+0.504*G+0.098*B+16
    # Cb = -0.148*R-0.291*G+0.439*B+128
    # Cr = 0.439*R-0.368*G-0.071*B+128
    # 模式“I”为32位整型灰色图像，它的每个像素用32个bit表示，0表示黑，255表示白，(0,255)之间的数字表示不同的灰度。在PIL中，从模式“RGB”转换为“I”模式是按照下面的公式转换的：
    # I = R * 299/1000 + G * 587/1000 + B * 114/1000
    # 模式“F”为32位浮点灰色图像，它的每个像素用32个bit表示，0表示黑，255表示白，(0,255)之间的数字表示不同的灰度。在PIL中，从模式“RGB”转换为“F”模式是按照下面的公式转换的：
    # F = R * 299/1000+ G * 587/1000 + B * 114/1000

# 图片通道分离与合并
def split_merge():
    # 分离通道
    img = Image.open(pic_file)
    r,g,b = img.split()
    print(r,g,b)
    # 合并通道
    Image.merge(mode = "RGBA", bands = [r,g,b,r]).show()

# 调整图片尺寸
def set_size():
    # 调整大小
    img = Image.open(pic_file)
    print(img.size)
    img_resized = img.resize((300,300))
    print(img_resized.size)
    img_resized.show()

# 截取图片部分区域
def crop():
    img = Image.open(pic_file)
    # Image.crop(left, up, right, below)
    # left：与左边界的距离
    # up：与上边界的距离
    # right：还是与左边界的距离
    # below：还是与上边界的距离
    img_croped = img.crop(box = (20,20,70,70)) 
    print(img_croped.size)
    img_croped.show()

# 图片旋转
def rotate():
    img = Image.open(pic_file)
    img_rotated = img.rotate(15,center = (0,0)) #以center为中心逆时针旋转
    img_rotated.show()

# 图片翻转
def transpose():
    img = Image.open(pic_file)
    # 左右翻转
    img_left_right = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_left_right.show()
    # 上下翻转
    img_top_bottom = img.transpose(Image.FLIP_TOP_BOTTOM)
    img_top_bottom.show()

# 镜面转换(同左右翻转)
def mirror():
    img = Image.open(pic_file)
    im_mirror = ImageOps.mirror(img) 
    im_mirror.show()

# 提取图片边缘,高斯模糊
def filter():
    img = Image.open(pic_file)
    # 提取图片边缘
    img_edges = img.filter(ImageFilter.FIND_EDGES)
    img_edges.show()
    # 高斯模糊
    img_blur = img.filter(ImageFilter.GaussianBlur(radius=3))
    img_blur.show()

# 添加文字
def arial():
    img = Image.open(pic_file)
    draw = ImageDraw.Draw(img)
    arial = ImageFont.truetype('./截图/文鼎PL简报宋.ttf', 46)
    draw.text((10,10),"就这?",font =arial, fill="white")
    img.show()

# 绘制图形
def draw():
    img = Image.open(pic_file)
    draw = ImageDraw.Draw(img)
    # 直线
    draw.line([0,0,641,641],fill = "red",width = 5)
    # 矩形
    draw.rectangle([78,24,455,320], fill=None, outline ='lawngreen',width = 5)
    # 椭圆
    draw.arc(xy = [78,24,455,320],start = 0,end = 360,fill="red",width=5)
    img.show()

# 在图片上粘贴其他图片
def paste():
    img = Image.open(pic_file)
    img_resized = img.resize((50,50))
    img.paste(img_resized,box = [80,10])
    img.show()

if __name__ == "__main__":
    paste()