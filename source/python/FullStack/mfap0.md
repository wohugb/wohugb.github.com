# [Angular + Python + Flask — Full stack demo](https://medium.com/@balramchavan/angular-python-flask-full-stack-demo-27192b8de1a3)

对于 JavaScript 框架，MEAN 堆栈非常有名。
我经常得到项目要求，人们希望使用 Python 构建服务器代码，主要是因为它与物联网，图像处理，数学应用或语言选择有关。
Django 是 Python 爱好者构建服务器端呈现网站的明显选择。

如果客户对技术开放，我通常会向他们提出 Angular + Python + Flask 的新技术堆栈。

Note:
我将数据库从此上下文中删除（M 的 MEAN = MongoDb）。
您可以自由使用可以从 Python 访问的任何数据库。
大多数人更喜欢 MySql 和 PostgreSQL。
稍后我会尝试用数据库示例更新这个故事。

## Angular

Angular 是用于构建单页面应用程序的 JavaScript（实际上是用 Typescript 编写的）框架。

Angular Docs

Edit description
angular.io

## Python

Python 是服务器端编程语言，非常强大，可构建复杂的物联网，图像处理和其他类型的系统。

Welcome to Python.org

The official home of the Python Programming Language
www.python.org

## Flask

Flask 是 Python 的 REST API 框架。如果您来自 MEAN 堆栈背景，则类似于“Express.js”。

Welcome | Flask (A Python Microframework)

Flask is a microframework for Python based on Werkzeug, Jinja 2 and good intentions. And before you ask: It's BSD…
flask.pocoo.org

## Full stack development

以下设置步骤已在 Windows 10 上执行。对于 Linux flavor OS，步骤可能不同但非常简单，Python 是内置的新版 Linux。

### Setup:

Install Python stable version

1. Install “pip” package. Download below file and execute it. It should install pip. (Don’t know what is pip? It is similar to “npm” or “NuGet” for Python packages)

https://bootstrap.pypa.io/get-pip.py

3. Update pip and setup tools — `pip install — upgrade pip setuptools`

4. Install virtual environment for pip— `pip install virtualenv`

5. Install flask — `pip install Flask`

6. Install flask helper packages — `pip install flask flask-jsonpify flask-sqlalchemy flask-restful`

### Writing Server side code

A simple Python script can be upgraded to REST server by importing and initializing Flask packages.

In above gist, @app.route(“/”) maps incoming GET “/” request to function hello() and return a simple JSON object.

This approach works but it is not good OOPs solution. In real world application, we build projects in terms of classes and objects.

Scared? Don’t be! We can update our server code to be more OOPs oriented and that is why we have imported other Flask helper packages.

Let’s see what changed.

Line № 5- — We are importing “Api” package and creating it’s object from Flask’s “app” object.

Line № 7- “Employees” is simple Python class with a “get()” member function. “Resource” parameter passed to “Employees” class contains incoming REST API call information.

Line № 11- Here we are creating REST API route mapping. All REST APIs should be configured here with their target classes. In this example, whenever user navigate to ‘server-url/employees’ then ‘get()’ function of ‘Employees’ class shall be executed and its result shall be returned to user.

In this manner, you can continue writing your business logic in Python classes and create REST API configuration to map them to REST end points.

## Angular client side code:

For Angular, it really doesn’t matter what technology is used for building REST API whether it is Java Springboot, ASP.NET Web API, Node.js, Python or any other. As long as resources can be accessed via HTTP commands, Angular is good.

To consume our Python REST API, just create a new Angular and call HttpClient methods (GET/PUT/POST/DELETE).

If you run server and client applications, you shall get CORS error.

Ideal solution is to server Angular from Python so that it won’t throw CORS error (that’s what MEAN stack is, isn’t it?). But for simplicity of this article, we shall skip CORS error.

## Install CORS packages -`pip install -U flask-cors`

Once installed, just call CORS(app) function and you will not see that error again.

Here is client+ server source code:

ultrasonicsoft/angular-python-flask-demo

Contribute to angular-python-flask-demo development by creating an account on GitHub.
github.com
Here is complete server side code for quick reference:

And that should be your first Angular + Python + Flask example up and running.

Hope you enjoyed it.
