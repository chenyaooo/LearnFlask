# coding: utf-8

from flask import Flask,url_for

from werkzeug.routing import BaseConverter
app = Flask(__name__)

app.config.from_pyfile("MyConfig.cfg")

class ReConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super(ReConverter, self).__init__(url_map)
        self.regex = args[0]

    def to_python(self, value):
        """把url中捕获的参数传递到value，再由to_python返回给试图函数"""
        # print value
        return value

    def to_url(self, value):
        """把url_for中的参数先传递到value中，（经处理后）再返回给试图函数"""
        value = "777"
        return value

# 在url_map中绑定 自定义的转换器re
app.url_map.converters["re"] = ReConverter


@app.route('/')
def hello_world():
    return 'Hello World!'

# 提取url中的参数  <>转换器
# @app.route("/<name>")
# def param(name):
#     return name

# 提取url中的整数参数
@app.route("/hello/<int:num>")  # <coverter: variable_name>  转换器有 int float path
def hello(num):
    return "num: %d"%num

# 在路由装饰其中使用自定义的转换器
@app.route("/id/<re('\d{3}'):id>")  # 定义一个转换器re （）内是转换器的规则
def hello_id(id):
    return id

# 只允许用post方式访问post_only函数
@app.route("/post", methods=["POST"])  # method参数是一个列表
def post_only():
    return "post only"

@app.route("/redirect")
def redirect():
    return '<a href="%s">hello id</a>'%url_for("hello_id", id="123")


if __name__ == '__main__':
    # print app.url_map
    app.run()
