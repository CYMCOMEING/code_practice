# pip install opencv-python
from cv2 import cv2
from PIL import Image
import os
from numpy import average, dot, linalg, fromfile, uint8


def get_thum(image, size=(64, 64), greyscale=False):
    # 利用image对图像大小重新设置, Image.ANTIALIAS为高质量的
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        # 将图片转换为L模式，其为灰度图，其每个像素用8个bit表示
        image = image.convert('L')
    return image

# 计算图片的余弦距离


def comp_cosin(i1, i2):
    image1 = get_thum(Image.open(i1))
    image2 = get_thum(Image.open(i2))
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


# 将图片转化为RGB
def make_regalur_image(img, size=(64, 64)):
    gray_image = img.resize(size).convert('RGB')
    return gray_image

# 计算直方图


def hist_similar(lh, rh):
    assert len(lh) == len(rh)
    hist = sum(1 - (0 if l == r else float(abs(l-r))/max(l, r))
               for l, r in zip(lh, rh))/len(lh)
    return hist


def comp_similar(img1, img2):
    image1 = make_regalur_image(Image.open(img1))
    image2 = make_regalur_image(Image.open(img2))
    return hist_similar(image1.histogram(), image2.histogram())


# 均值哈希算法
def ahash(img):
    # image = cv2.imread(img)
    image = cv_imread(img)
    
    # 将图片缩放为8*8的
    image = cv2.resize(image, (8, 8), interpolation=cv2.INTER_CUBIC)
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
    ahash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i, j] > avg:
                ahash_str = ahash_str + '1'
            else:
                ahash_str = ahash_str + '0'
    result = ''
    for i in range(0, 64, 4):
        result += ''.join('%x' % int(ahash_str[i: i + 4], 2))
    # print("ahash值：",result)
    return result

# 差异值哈希算法


def dhash(img):
    # image = cv2.imread(img)
    image = cv_imread(img)
    # 将图片转化为8*8
    image = cv2.resize(image, (9, 8), interpolation=cv2.INTER_CUBIC)
    # 将图片转化为灰度图
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    dhash_str = ''
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j+1]:
                dhash_str = dhash_str + '1'
            else:
                dhash_str = dhash_str + '0'
    result = ''
    for i in range(0, 64, 4):
        result += ''.join('%x' % int(dhash_str[i: i+4], 2))
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


def comp_ahash(img1, img2):
    hash1 = ahash(img1)
    hash2 = ahash(img2)
    return campHash(hash1, hash2)


def comp_dhash(img1, img2):
    hash1 = dhash(img1)
    hash2 = dhash(img2)
    return campHash(hash1, hash2)


def cv_imread(file_path):
    cv_img = cv2.imdecode(fromfile(file_path, dtype=uint8), cv2.IMREAD_UNCHANGED)
    return cv_img

    # file_path_gbk = file_path.encode('utf-8')        # unicode转gbk，字符串变为字节数组
    # img_mat = cv2.imread(file_path_gbk.decode())  # 字节数组直接转字符串，不解码
    # return img_mat

    root_dir, file_name = os.path.split(file_path)
    pwd = os.getcwd()
    if root_dir:
        os.chdir(root_dir)
    cv_img = cv2.imread(file_name)
    os.chdir(pwd)
    return cv_img



if __name__ == "__main__":
    # res = comp_cosin(r"a.jpg", r"a.png")
    # res = comp_similar(r"a.jpg", r"a.png")
    # res = comp_ahash(r"a.jpg", r"a.png")
    res = comp_dhash(r"a.jpg", r"a.png")
    print(res)
