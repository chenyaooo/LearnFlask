# coding:utf-8

from flask import Flask, current_app
from flask_script import Manager

app = Flask(__name__)

# 创建管理员类Manager对象，并托管app
manager = Manager(app)


@app.route("/")
def index():
    return "index page"


if __name__ == '__main__':
    manager.run()
