# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/17 14:52
# @Author  : xhh
# @Desc    : 余弦相似度计算
# @File    : difference_image_consin.py
# @Software: PyCharm
# pip install opencv-python
from PIL import Image
from numpy import average, dot, linalg
 
# 对图片进行统一化处理
def get_thum(image, size=(64,64), greyscale=False):
    # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
        image = image.convert('L')
    return image
 
# 计算图片的余弦距离
def image_similarity_vectors_via_numpy(i1, i2):
    image1 = get_thum(i1)
    image2 = get_thum(i2)
    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        # linalg=linear（线性）+algebra（代数），norm则表示范数
        # 求图片的范数？？
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    # dot返回的是点积，对二维数组（矩阵）进行计算
    res = dot(a / a_norm, b / b_norm)
    return res
 
def comp_cosin(img1, img2):
 image1 = Image.open(img1)
 image2 = Image.open(img2)
 cosin = image_similarity_vectors_via_numpy(image1, image2)
 print('图片余弦相似度',cosin)
 '把图片表示成一个向量，通过计算向量之间的余弦距离来表征两张图片的相似度'


"""
利用SSIM（结构相似度度量）计算图片的相似度

是一种全参考的图像质量评价指标，分别从亮度、对比度、结构三个方面度量图像相似性。

SSIM取值范围[0, 1]，值越大，表示图像失真越小。

在实际应用中，可以利用滑动窗将图像分块，令分块总数为N，考虑到窗口形状对分块的影响，采用高斯加权计算每一窗口的均值、方差以及协方差，然后计算对应块的结构相似度SSIM，最后将平均值作为两图像的结构相似性度量，即平均结构相似性SSIM
"""
"""
# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/17 14:26
# @Author  : xhh
# @Desc    : 结构相似度量，计算图片之间的相似度
# @File    : difference_image_ssim.py
# @Software: PyCharm
# pip install scikit-image
from skimage.measure import compare_ssim
from scipy.misc import imread
import numpy as np
 
# 读取图片
def comp_ssim(i1, i2):
 img1 = imread(i1)
 img2 = imread(i2)
 img2 = np.resize(img2, (img1.shape[0], img1.shape[1], img1.shape[2]))
 print(img1.shape)
 print(img2.shape)
 ssim =  compare_ssim(img1, img2, multichannel = True)
 print('ssim比较', ssim)
"""

"""
通过直方图计算
直方图过于简单，只能捕捉颜色信息的相似性，捕捉不到更多的信息。只要颜色分布相似，就会判定二者相似度较高。
"""

# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/17 16:04
# @Author  : xhh
# @Desc    : 通过直方图计算图片的相似度
# @File    : difference_image_hist.py
# @Software: PyCharm
from PIL import Image
 
# 将图片转化为RGB
def make_regalur_image(img, size=(64, 64)):
    gray_image = img.resize(size).convert('RGB')
    return gray_image
 
# 计算直方图
def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    hist = sum(1 - (0 if l == r else float(abs(l-r))/max(l,r))for l, r in zip(lh, rh))/len(lh)
    return hist
 
# 计算相似度
def calc_similar(li, ri):
    calc_sim = hist_similar(li.histogram(), ri.histogram())
    return calc_sim

def comp_similar(img1, img2):
    image1 = Image.open(img1)
    image1 = make_regalur_image(image1)
    image2 = Image.open(img2)
    image2 = make_regalur_image(image2)
    print("图片间的相似度为",calc_similar(image1, image2))



"""
感知哈希算法是一类算法的总称，包括aHash、pHash、dHash。顾名思义，感知哈希不是以严格的方式计算Hash值，而是以更加相对的方式计算哈希值，因为“相似”与否，就是一种相对的判定。

aHash：平均值哈希。速度比较快，但是常常不太精确。
pHash：感知哈希。精确度比较高，但是速度方面较差一些。
dHash：差异值哈希。精确度较高，且速度也非常快
注意： 但是在下面我用了ahash和dhash得到的哈希值都是一样的，我就有点懵逼了！！！

计算图片的hanming距离步骤（代码里面有介绍）：

先将图片压缩成8*8的小图
将图片转化为灰度图
计算图片的Hash值，这里的hash值是64位，或者是32位01字符串
将上面的hash值转换为16位的
通过hash值来计算汉明距离
"""


# -*- coding: utf-8 -*-
# !/usr/bin/env python
# @Time    : 2018/11/16 15:40
# @Author  : xhh
# @Desc    : 图片的hash算法
# @File    : image_3hash.py
# @Software: PyCharm
import cv2
 
# 均值哈希算法
def ahash(image):
    # 将图片缩放为8*8的
    image =  cv2.resize(image, (8,8), interpolation=cv2.INTER_CUBIC)
    # 将图片转化为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # s为像素和初始灰度值，hash_str为哈希值初始值
    s = 0
    ahash_str = ''
    # 遍历像素累加和
    for i in range(8):
        for j in range(8):
            s = s+gray[i, j]
    # 计算像素平均值
    avg = s/64
    # 灰度大于平均值为1相反为0，得到图片的平均哈希值，此时得到的hash值为64位的01字符串
    ahash_str  = ''
    for i in range(8):
        for j in range(8):
            if gray[i,j]>avg:
                ahash_str = ahash_str + '1'
            else:
                ahash_str = ahash_str + '0'
    result = ''
    for i in range(0, 64, 4):
        result += ''.join('%x' % int(ahash_str[i: i + 4], 2))
    # print("ahash值：",result)
    return result
 
# 差异值哈希算法
def dhash(image):
    # 将图片转化为8*8
    image = cv2.resize(image,(9,8),interpolation=cv2.INTER_CUBIC )
    # 将图片转化为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    dhash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i,j]>gray[i, j+1]:
                dhash_str = dhash_str + '1'
            else:
                dhash_str = dhash_str + '0'
    result = ''
    for i in range(0, 64, 4):
        result += ''.join('%x'%int(dhash_str[i: i+4],2))
    # print("dhash值",result)
    return result
 
# 计算两个哈希值之间的差异
def campHash(hash1, hash2):
    n = 0
    # hash长度不同返回-1,此时不能比较
    if len(hash1) != len(hash2):
        return -1
    # 如果hash长度相同遍历长度
    for i in range(len(hash1)):
        if hash1[i] != hash2[i]:
            n = n+1
    return n

def comp_hash(i1, i2):
 img1 = i1
 img2 = i2
 img1 = cv2.imread(img1)
 img2 = cv2.imread(img2)
 
 hash1 = ahash(img1)
 print('img1的ahash值',hash1)
 hash2= dhash(img1)
 print('img1的dhash值',hash2)
 hash3= ahash(img2)
 print('img2的ahash值',hash3)
 hash4= dhash(img2)
 print('img2的dhash值',hash4)
 camphash1 = campHash(hash1, hash3)
 camphash2= campHash(hash2, hash4)
 print("ahash均值哈希相似度：",camphash1)
 print("dhash差异哈希相似度：",camphash2)



from PIL import Image
import math
import operator
from functools import reduce

def image_contrast(img1, img2):

    image1 = Image.open(img1)
    image2 = Image.open(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a, b: (a-b)**2, h1, h2)))/len(h1))
    return result

if __name__ == '__main__':
 img1 = r'D:\python\a.png'
 img2 = r'D:\python\b.png'
 comp_cosin(img1, img2)
 #comp_ssim(img1, img2)
 comp_similar(img1, img2)
 comp_hash(img1, img2)
 print(image_contrast(img1, img2))
