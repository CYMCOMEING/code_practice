from config import *
# 导入Flask类
from flask import Flask,request,render_template
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





if __name__ == '__main__':
  # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    app.run(host="0.0.0.0", port=5000)
    # print(get_dxdata())
