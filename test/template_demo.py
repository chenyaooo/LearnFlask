# coding:utf-8

from flask import Flask, render_template

app = Flask(__name__)

# 向模版中传递参数


@app.route("/")
def temp_para():
    # 方法一 直接在参数中以键值对方式传递
    # return render_template("temp_para.html", name="haha", age=18)

    # 方法二 准备上下文变量，在返回参数中拆包

    # 也可以传递字典和列表
    my_dict = {"a": 1, "b": 2}
    my_list = [3, 4, 5, 6, 10, 11]
    my_int = 0
    context = {
        "name": "haha",
        "age": 18,
        "my_dict": my_dict,
        "my_list": my_list,
        "my_int": my_int
    }

    return render_template("temp_para.html", **context)

# 除了模版中自带的过滤器，还可以自定义过滤器


# 1 定义过滤器函数 原理 先接收要传递的变量，再加工变量，最后将返回值传递给模版
def filter_2_list(li):
    """自定义一个过滤器，将模版变量中的列表隔一位提取出来"""
    return li[::2]


# 2 将自定义的过滤器函数加入配置的过滤器中
app.add_template_filter(filter_2_list, "li_2")  # 参数一 自定义过滤器函数的引用 参数二 模版中使用的过滤器名字


# 自定义过滤器方法二 使用template_filter装饰器,参数为模版中使用的过滤器名字
@app.template_filter("li_3")
def filter_2_list(li):
    """自定义一个过滤器，将模版变量中的列表隔两位提取出来"""
    return li[::3]


if __name__ == '__main__':
    app.run(debug=True)
