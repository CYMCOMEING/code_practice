"""
遍历指定文件
解压文件
解压所有文件

问题用winrar压缩的带密码的zip文件，
zipfile不支持该格式

zipfile提供的压缩方法有：
ZIP_STORED，ZIP_DEFLATED， ZIP_BZIP2和ZIP_LZMA
ZIP_STOREED：只是作为一种存储，实际上并未压缩
ZIP_DEFLATED：用的是gzip压缩算法
ZIP_BZIP2：用的是bzip2压缩算法
ZIP_LZMA：用的是lzma压缩算法
"""


import rarfile
import zipfile
import glob
import os


def unrar(file, path=None, pwd=None):
    if not file:
        print('file {} error.'.format(file))
        return
    try:
        with rarfile.RarFile(file) as rf:
            rf.extractall(path=path, pwd=bytes(pwd,encoding='utf-8'))
    except Exception as e:
        print("file:{}  {}".format(file, e))

def unzip(file, path=None, pwd=None):
    if not file:
        print('file {} error.'.format(file))
        return
    try:
        with zipfile.ZipFile(file) as zf:
            zf.extractall(path=path, pwd=bytes(pwd,encoding='utf-8'))
    except Exception as e:
        print("file:{}  {}".format(file, e))


def getfiles(pathname):
    return glob.iglob(pathname + r'\*[.rar|.zip]')

def un_file(file, opt_dir=None, pwd=None):
    # 压缩文件
    filetype = file.split('.')[-1]
    if filetype == 'zip':
        unzip(file, opt_dir, pwd)
    if filetype == 'rar':
        unrar(file, opt_dir, pwd)


def un_all(pathname, pwd=None):
    # 解压目录下所有压缩文件
    fi = getfiles(pathname)
    for file in fi:
        opt_dir = pathname + '/'+ os.path.basename(file).split('.')[0]
        un_file(file, opt_dir, pwd)
        

def create_zip(pathname, opt_zip):
    with zipfile.ZipFile(opt_zip, 'w') as zf:
        base_dir = os.path.abspath(pathname)
        replace_dir = os.path.dirname(base_dir)
        print(base_dir)
        print(replace_dir)
        for root, dirs, files in os.walk(base_dir):

            # root 表示当前正在访问的文件夹路径
            # dirs 表示该文件夹下的子目录名list
            # files 表示该文件夹下的文件list
            opt_path = root
            opt_path = opt_path.replace(replace_dir, '')
            #print('A '+root+'\n'+opt_path)

            # 遍历文件
            for f in files:
                zf.write(os.path.join(root, f), os.path.join(opt_path, f))
                print('C '+os.path.join(root, f)+"\n"+os.path.join(opt_path, f))
                pass
            # 遍历所有的文件夹
            for d in dirs:
                zf.write(os.path.join(root, d), os.path.join(opt_path, d))
                print('B '+os.path.join(root, d)+"\n"+os.path.join(opt_path, d))
                pass
            


#un_all(r'D:\python\test', '123')
# create_zip('D:\\html', 'D:\\html.zip')

