# coding:utf-8

from flask import Flask, request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

# 表单中的csrf_token需要secret_key
app.config["SECRET_KEY"] = "nig89tgj32ojo"

# flask中的表单类，与Django中的模型类相似


# 表单类要继承FlaskForm
class RegisterForm(FlaskForm):
    """注册表单类，表单中的字段自定义"""

    # 字段的参数接收限制条件，是一个列表
    name = StringField(label="name", validators=[DataRequired()])
    password = PasswordField(label=u"密码", validators=[DataRequired()])
    passwd2 = PasswordField(label=u"再次输入密码", validators=[EqualTo("password")])
    sub = SubmitField(label=u"提交")


# 在视图函数中生成RegisterForm实例对象，接收并验证表单信息
@app.route("/register", methods=["POST", "GET"])
def register():

    # 创建一个自定义表单的实例对象
    form = RegisterForm()

    # 判断请求方式，如果是get，则返回表单；post则验证表单信息
    if request.method == "GET":
        return render_template("register.html", form=form, err="")

    # 验证表单，如果表单提交信息正确，则获取表单信息，否则返回错误信息
    # form对象有一个验证表单提交表单信息的方法 form.validate_on_submit()
    # validate_on_submit方法会验证表单中的信息是否符合自定义表单类中的限制条件，如果全部符合则返回True
    if form.validate_on_submit():
        # 通过表单获取提交的信息
        name = form.name

        return "%s success" % name
    else:
        return render_template("register.html", form=form, err=u"填写的信息出错")


if __name__ == '__main__':
    app.run(debug=True)
