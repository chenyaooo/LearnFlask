`5.03`
# Flask

day01	
## HTTP通信
- 浏览器到服务器
- 浏览器发出请求报文request
  - 起始行
  - 请求头header
  - 请求体body
- 通过**TCP传输**
- 服务器按照HTTP协议格式进行解析
  - 根据解析后的请求信息,进行**路由分发**
  - 具体业务逻辑,执行相应代码
  - 组织响应数据,打包成HTTP响应报文
- 服务器返回HTTP协议数据
  - 起始行
  - 响应头header
  - 响应体body 

### question
1. 路由分发?
2. WSGI协议?
3. 服务器模型
3. django的功能是框架,自身提供的服务器runserver只是方便调适.在django后期的安排中,使用uwsgi服务器

### 框架

#### 核心
1. 实现路由
2. 视图函数(业务逻辑)
3. flask的核心
   - Werkzeug  实现路由
   - Jinja2  实现模版

#### 框架的轻重
- 重量级:Django
- 轻量级:Flask、Tornada.Webpy


### 迁移所有的虚拟环境,依赖包
- pip freeze > 文件   重定向
- pip install 

- 导入相关的包
- 创建flask的app
  
  ```
  app = Flask(__name__,
              static_url_path="",  #  默认是/static
              template_url_path=""  # 默认是/template)
  
  __name__:模块名,flask会把这个模块所在的目录当作当前flask的工程目录,以此目录为根目录寻找static和template
  
  ```


- Flask中绑定路由

	```
	跟Django不同,没有专门的文件负责url
	而是跟之前学习过的webmini框架类似,使用路由的装饰器
	
	@app.route("/")
	
	```

- 启动服务器
  
  ```
  Flask中也有用于测试的服务器,
  相当于Django中的 python manage.py runserver
  
  app.run()
  ```
  
  
- 为flask添加配置
  
  ```
  1.通过外置文件
  新建文件 MyConfig.cfg
  app.config.from_pyfile("MyConfig.cfg")
  
  
  2.通过对象的方式读取配置参数
  class MyConfig(object):
  		"""配置信息"""
  		DEBUG = True
  		
  3.在程序启动时
  app.run(debug=True)
  
  ```
  
  
- 指定访问的host和port

  1. app.run(host="0.0.0.0", port="")
  2. ip设为0.0.0.0的话,既可以访问本机回环地址127.0.0.1,也可以访问外网地址


- 同一路由装饰多个函数
  - 第一个函数会被运用

- 查看路由映射: url_map


- app.route()的参数
  1. 路由,路径 “/”
  2. 请求方式 method=['GET']

- url反解析
  
  ```
  在Django的url中,如果要使用反向解析,需要自己命名
  url(r'', views.index, name='index')
  
  在flask中,使用反解析,不需要自己命名,函数名就是url的名字,要使用反解析,需要使用flask自带的url_for
  
  url_for(“views‘ name”) ---> urls' address
  
  
  ```
  
- 转换器
  
  ![](images/flask_路由过滤器.png)

  ```
  # app.route(“/<name>”)
  
  提取出url中的整数
  app.route(“/<int:id>”)  # int --> 过滤条件 id --> 提取出的东西
  def hello(id):
  		return id
  ```
  
  - 当flask自带的路由过滤器不能满足要求时,如“提取出url后的3个整数”
  - 自定义路由转化器
  
  ```
  1.自定义转化器类
  class ReConverter(BaseConverter):
  		"""自定义的支持传入正则表达式的转换器"""
  		
  		def __init__(self, url_map, *args):
  		# 调用父类方法,注意flask使用的是python2,调用父类方法时需要传入名字
  		
  		super(Reconverter, self).__init__(url_map)
  		# 将传入的参数args,保存到regex属性中
  		
  		self.regex = args[0]  # args[0]就是我们在路由装饰器参数中传入的正则表达式
 
 2. 绑定
 app.url_map.converter["re"]=ReConverter
 
 3. 在路由装饰器中使用正则
   #  捕获url中的3个整数
   app.route(“/id/<re('\d{3}'):id>”)
  def hello(id):
  		return id
  
  
  ```
  
#### question
- 路由中的动态参数?



- 上传 


   