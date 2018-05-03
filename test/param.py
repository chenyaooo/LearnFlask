# coding:utf-8

from flask import Flask,request

app = Flask(__name__)

# app.config.from_pyfile("MyConfig.cfg")

class MyConfig(object):
    """用创建类的方法配置flask"""
    DEBUG = True


@app.route('/')
def hello_world():
    name = request.args.get("name")
    return name


@app.route("/upload", methods=["POST"])
def upload():
    """上传"""
    pic_file = request.files.get("pic")

    if pic_file:
        pic_file.save("./upload_file")
        return "sucess"
    else:
        return "failed"


if __name__ == '__main__':
    app.run()
