# coding:utf-8

from flask import Flask, current_app

app = Flask(__name__)


# 通过定义类的方式配置flask
# 1 定义
class MyConfig(object):
    DEBUG = True
    ITCAST = "python"


# 2 注册
app.config.from_object(MyConfig)


@app.route('/')
def hello_world():
    # 可以在函数中读取配置文件
    print(current_app.config.get("ITCAST"))
    
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
