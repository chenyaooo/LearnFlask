# coding:utf-8

from flask import Flask, abort

app = Flask(__name__)


@app.route("/")
def index():
    return "index page"


# flask中的请求钩子，功能类似于django的中间件,以装饰器方式存在


# 第一请求之前被调用
@app.before_first_request
def handle_before_first_req():
    print("handle_before_first_req")


# 每次请求之前被调用
@app.before_request
def handle_before_req():
    print("handle_before_req")


# 如果视图函数没有异常，请求之后被调用
@app.after_request
def handle_after_req(response):
    print("handle_after_req")
    return response


# 每次请求之后被调用，不管有没有异常
@app.teardown_request
def handle_after_all_req(response):
    print("handle_after_all_req")
    return response


@app.route("/err")
def err():
    a = 1/0
    return "NeverExcute"


if __name__ == '__main__':
    app.run(debug=True)
