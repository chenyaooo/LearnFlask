# coding:utf-8

from flask import Flask, make_response, redirect, url_for, jsonify
import json

app = Flask(__name__)


@app.route("/")
def index():

    # return "index page"  # 视图函数不仅可以返回响应体，还可以返回状态码和响应头
    # abort方法中的状态码是http标准状态码，但是视图函数返回的状态码可以自定义
    # return (body, status, header) 响应头可以是元组构成的列表，也可以是字典

    # return "index page", 666, [("city", "wuhan"),]
    # return "index page", 666, {"city": "wuhan"}

    # status不仅可以是数字，还可以是包含信息的字符串
    # return "index page", "666 flask", {"city": "wuhan"}

    # 视图函数返回的信息由flask自动组建成response，通过make_response，可以自定义response
    resp = make_response("index page")  # 响应体
    resp.status = "666"  # 状态码
    resp.headers["city"] = "wuhan"  # 响应头
    return resp


# 返回json数据
@app.route("/json")
def return_json():
    j = {
        "name": "haha",
        "age": 18
    }

    # 将python中的dict转换为json格式的str
    # 除了转换数据格式外，还需要修改响应头的Content-Type
    # return json.dumps(j), 200, {"Content-Type": "application/json"}

    # flask提供了便捷的方式返回json数据，不需要更改数据结构，也不需要手动填写响应头
    return jsonify(j)


# flask中重定向
@app.route("/login")
def login():

    # redirect用法与Django中基本一致
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=True)

