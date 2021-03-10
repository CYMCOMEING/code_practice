from config import *
import os
# 导入Flask类
from flask import Flask, request, render_template, redirect, url_for, flash
# 获取上传文件的文件名
from werkzeug.utils import secure_filename
# 实例化，可视为固定格式
app = Flask(__name__)

# route()方法用于设定路由；类似spring路由配置


@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dx')
def rand_dx():
    _, title, content = get_dxdata()
    # return '{}<br>{}<br>'.format(title,content)
    return render_template('./dx.html', title=title, content=content)


@app.route('/bvideo')
def get_bvideo_pic():
    img_src = ''
    if request.method == 'GET':
        bv_num = request.args.get('bv_num')
        img_src = get_video_pic(bv_num)

    return render_template('./bvideo_pic.html', img_src=img_src)


UPLOAD_FOLDER = r'./upload'   # 上传路径
ALLOWED_EXTENSIONS = set(
    ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc'])   # 允许上传的文件类型


def allowed_file(filename):   # 验证上传的文件名是否符合要求，文件名必须带点并且符合允许上传的文件类型要求，两者都满足则返回 true
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

# 参考 https://zhuanlan.zhihu.com/p/23731819


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':   # 如果是 POST 请求方式
        file = request.files['file']   # 获取上传的文件
        if file:
            # if file and allowed_file(file.filename):   # 如果文件存在并且符合要求则为 true
            filename = secure_filename(file.filename)   # 获取上传文件的文件名
            print(filename)
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            file.save(os.path.join(UPLOAD_FOLDER, filename))   # 保存文件
            # return '{} upload successed!'.format(filename)   # 返回保存成功的信息
            return redirect(url_for("upload_file"))  # 重定向到上传页面
    # 使用 GET 方式请求页面时或是上传文件失败时返回上传文件的表单页面
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/yunpan/')
@app.route('/yunpan/<path:client_path>')
# @app.route('/yunpan/<path>/')
def yunpan_dir(client_path=None):
    server_path = UPLOAD_FOLDER + '/'
    abspath = ''
    fileslist = []

    if not client_path:
        client_path = ""
    else:
        print(client_path.split('/'))
        abspath += '/'.join(client_path.split('/')[0:-2])
        if abspath:
            abspath += '/'
        print(abspath)
        # 获取服务器上的路径
        server_path += client_path

    if os.path.exists(server_path):
        files = [f if os.path.isfile(server_path + f)
                 else f + '/' for f in os.listdir(server_path)]
        filespath = [client_path+f for f in files]
        fileslist = zip(files, filespath)
    return render_template("yunpan.html", curr_path=client_path, fileslist=fileslist, abspath=abspath)


if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    app.run(host="0.0.0.0", port=5000)
    # print(get_dxdata())
