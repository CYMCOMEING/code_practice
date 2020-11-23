from flask import Flask
from flask import request,render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
    if request.method == "POST":
        print(request.form["username"])
        print(request.form["password"])
        if request.form["username"] == 'cym' and request.form["password"] == '123456':
            return render_template("pic.html")
    return "出错"





if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host=127.0.0.1, port=5000, debug=false
    app.run()
