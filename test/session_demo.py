# coding:utf-8

from flask import Flask, session

app = Flask(__name__)

# 设置session需要使用secret_key,属于配置文件内容
# 当配置内容很少时，不需要使用配置文件或MyConfig类，而是使用类似字典的方式存储

# 密钥是一段随机乱码
app.config["SECRET_KEY"] = "nbdbciuv[owif0nke293m"


# 与Django有所不同，flask中有session接口直接调用，而不是response对象的属性
@app.route("/set_session")
def set_session():

    # session类似于字典 session的内容因为使用了密钥，所以在浏览器上是乱码
    session["name"] = "hahaha"

    return "set session success"


# 获取session 方法类似于字典
@app.route("/get_session")
def get_session():
    name = session.get("name")
    return name


# 删除session
@app.route("/del_session")
def del_session():
    session.pop("name")
    return "delete session success"


if __name__ == '__main__':
    app.run()
