# coding:utf-8

from flask import Flask, abort

app = Flask(__name__)


@app.route("/")
def index():

    # abort方法就相当于python中的raise，可以终止视图函数的执行
    abort(403)  # abort方法中传入的参数是错误状态码status code 403 禁止访问 404 页面不存在

    return "index page"


# abort方法传入错误状态码，，用户看到的是默认的错误页面
# 可以自定义错误处理方法，在发生特定错误时，会调用自定义的错误类，浏览器看到的即此处的返回结果
@app.errorhandler(403)
def handle_403(e):  # e接收发生错误时的参数
    # return u"请求被禁止" e
    return u"请求被禁止：%s" % e


if __name__ == '__main__':
    app.run()

