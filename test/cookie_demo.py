# coding:utf-8

from flask import Flask, make_response, request

app = Flask(__name__)


# 设置cookie 与django中类似，由response来设置
@app.route("/set_cookie")
def set_cookie():

    # 1 生成response对象
    resp = make_response("set cookie success")

    # 2 由response对象来设置cookie,默认失效时间是浏览器关闭
    resp.set_cookie("id", "haha")

    # 3 设置过期时间 跟Django中完全一样
    resp.set_cookie("id2", "haha2", max_age=3600)

    return resp


# 获取cookie，跟django中一样，由request对象获取
@app.route("/get_cookie")
def get_cookie():

    # request中的cookie属性，保存了浏览器中的cookie
    cookie = request.cookies.get("id")
    return cookie


# 删除cookie 跟Django中一样，由response对象删除
@app.route("/del_cookie")
def del_cookie():

    # 1 生成response对象
    resp = make_response("delete cookie success")

    # 但是删除cookie不是真的从浏览器中删除，而是把失效时间设置为浏览器关闭
    resp.delete_cookie("id2")

    return resp


if __name__ == '__main__':
    app.run()
