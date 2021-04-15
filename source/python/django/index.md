# Django 简要学习文档

## 安装

!!! note "删除旧版本"
    ```sh
    $ python -c "import django; print(django.__path__)"
    ```

!!! note "安装"
    ```sh
    # Django2 不支持 python2
    $ pip3 install Django
    ```

!!! note "验证"
    ```sh
    >>> import django
    >>> print(django.get_version())
    2.0
    # 或者
    $ python -m django --version
    2.0
    ```

## 创建项目

### 第一步 出生

#### 创建项目

```sh
    $ django-admin startproject mysite
    ...
```

!!! note "目录结构"
    ```
        mysite/
            manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py
    ```

#### 启动开发服务器

!!! note "启动开发服务器"
    ```sh
        $ python manage.py runserver 10.11.14.19:9701
    ```

!!! note "配置 Nginx"
    ```conf
        upstream  py-apidev  {
            server 10.11.14.19:9701;
        }

        server {
            listen  80;
            server_name py-apidev.test.com;
            ...
            location / {
                ...
                proxy_pass http://py-apidev;
                ...
            }
        }
    ```

!!! note "配置允许域名"
    ```sh
        $ vim settings.py
    ```
    ```
        ALLOWED_HOSTS = [
            'py-apidev.test.com',
            'py-api.test.com'
        ]
    ```

#### 创建Polls应用

```sh
    $ python manage.py startapp polls
    ...
```

!!! note "目录结构"
    ```
        polls/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py
    ```

!!! note "编辑视图 polls/views.py"
    ```py
        from django.http import HttpResponse

        def index(request):
            return HttpResponse("Hello, world. You're at the polls index.")
    ```

!!! note "应用路由：polls/urls.py"
    ```
        from django.urls import path
        from . import views
        urlpatterns = [
            path('', views.index, name='index'),
        ]
    ```

!!! note "入口路由：mysite/urls.py"
    ```
        from django.urls import include, path
        from django.contrib import admin

        urlpatterns = [
            path('polls/', include('polls.urls')),
            path('admin/', admin.site.urls),
        ]
    ```

#### path 参数

##### path() argument: route

##### path() argument: view

##### path() argument: kwargs

##### path() argument: name

### 第二步 数据库

### 第三步 视图

### 第四步 表单

### 第五步 自动测试

### 第六步 样式和图片

### 第七步 管理