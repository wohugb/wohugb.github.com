# Awesome Flask [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

> 精选的 Flask 资源和插件的精选列表

- [Awesome Flask ![Awesome](https://github.com/sindresorhus/awesome)](#awesome-flask-awesomehttpsgithubcomsindresorhusawesome)
  - [框架](#%E6%A1%86%E6%9E%B6)
  - [管理界面](#%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2)
  - [分析](#%E5%88%86%E6%9E%90)
  - [认证](#%E8%AE%A4%E8%AF%81)
  - [授权](#%E6%8E%88%E6%9D%83)
  - [数据库](#%E6%95%B0%E6%8D%AE%E5%BA%93)
  - [数据库迁移](#%E6%95%B0%E6%8D%AE%E5%BA%93%E8%BF%81%E7%A7%BB)
  - [对话](#%E5%AF%B9%E8%AF%9D)
  - [高速缓存](#%E9%AB%98%E9%80%9F%E7%BC%93%E5%AD%98)
  - [数据验证](#%E6%95%B0%E6%8D%AE%E9%AA%8C%E8%AF%81)
  - [电子邮件](#%E7%94%B5%E5%AD%90%E9%82%AE%E4%BB%B6)
  - [国际化](#%E5%9B%BD%E9%99%85%E5%8C%96)
  - [全文检索](#%E5%85%A8%E6%96%87%E6%A3%80%E7%B4%A2)
  - [限速](#%E9%99%90%E9%80%9F)
  - [任务队列](#%E4%BB%BB%E5%8A%A1%E9%98%9F%E5%88%97)
  - [异常跟踪](#%E5%BC%82%E5%B8%B8%E8%B7%9F%E8%B8%AA)
  - [追踪](#%E8%BF%BD%E8%B8%AA)
  - [APM](#apm)
  - [其他 SDK](#%E5%85%B6%E4%BB%96-sdk)
  - [前端](#%E5%89%8D%E7%AB%AF)
  - [开发（调试/测试/文档）](#%E5%BC%80%E5%8F%91%E8%B0%83%E8%AF%95%E6%B5%8B%E8%AF%95%E6%96%87%E6%A1%A3)
  - [Utils](#utils)
  - [资源](#%E8%B5%84%E6%BA%90)
    - [教程](#%E6%95%99%E7%A8%8B)
    - [课程](#%E8%AF%BE%E7%A8%8B)
    - [图书](#%E5%9B%BE%E4%B9%A6)
    - [幻灯片](#%E5%B9%BB%E7%81%AF%E7%89%87)
    - [影片](#%E5%BD%B1%E7%89%87)
    - [用烧瓶建造](#%E7%94%A8%E7%83%A7%E7%93%B6%E5%BB%BA%E9%80%A0)
    - [样板](#%E6%A0%B7%E6%9D%BF)

## 框架

- [Connexion](https://github.com/zalando/connexion) - Swagger/OpenAPI First framework for Python on top of Flask with automatic endpoint validation and OAuth2 support
- [Flask-MongoRest](https://github.com/closeio/flask-mongorest) - Restful API framework wrapped around MongoEngine
- [Eve](https://github.com/pyeve/eve) - REST API framework powered by Flask, MongoDB and good intentions
- [Flask-Restless](https://github.com/jfinkels/flask-restless) - A Flask extension for creating simple ReSTful APIs from SQLAlchemy models
- [Flask-RESTful](https://github.com/flask-restful/flask-restful) - Simple framework for creating REST APIs
- [Flask-RestPlus](https://github.com/noirbizarre/flask-restplus) - syntaxic sugar, helpers and automatically generated Swagger documentation.
- [Flask-Potion](https://github.com/biosustain/potion) - RESTful API framework for Flask and SQLAlchemy
- [Zappa](https://github.com/Miserlou/Zappa) - Build and deploy server-less Flask applications on AWS Lambda and API Gateway

## 管理界面

- [Flask-Admin](https://github.com/flask-admin/flask-admin) - Simple and extensible administrative interface framework for Flask

## 分析

- [Flask-Analytics](https://github.com/citruspi/Flask-Analytics) - Analytics snippets generator extension for the Flask framework
- [Flask-Matomo](https://github.com/Lanseuo/flask-matomo) - Track requests to your Flask website with Matomo

## 认证

- [Flask-Security](https://github.com/mattupstate/flask-security) - Quick and simple security for Flask applications
- [Flask-Login](https://github.com/maxcountryman/flask-login) - Flask user session management
- [Flask-User](https://github.com/lingthio/Flask-User) - Customizable user account management for Flask
- [Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth) - Simple extension that provides Basic and Digest HTTP authentication for Flask routes
- [Flask-Praetorian](https://github.com/dusktreader/flask-praetorian) - Strong, Simple, and Precise security for Flask APIs (using jwt)

## 授权

- [Authlib](https://github.com/lepture/authlib) - Authlib is an ambitious authentication library for OAuth 1, OAuth 2, OpenID clients, servers and more.
- [Authomatic](https://github.com/authomatic/authomatic) - Authomatic provides out of the box support for a number of providers using OAuth 1.0a (Twitter, Tumblr and more) and OAuth 2.0 (Facebook, Foursquare, GitHub, Google, LinkedIn, PayPal and more)
- [Flask-Pundit](https://github.com/anurag90x/flask-pundit) - Extension based on Rails' [Pundit](https://github.com/varvet/pundit) gem that provides easy way to organize access control for your models
- [Flask-Dance](https://github.com/singingwolfboy/flask-dance) - OAuth consumer extension for Flask, shipped with pre-set support for Facebook, GitHub, Google, etc.

## 数据库

- [Flask-MongoEngine](https://github.com/MongoEngine/flask-mongoengine) - MongoEngine flask extension with WTF model forms support
- [Flask-SQLAlchemy](https://github.com/mitsuhiko/flask-sqlalchemy) - Adds SQLAlchemy support to Flask

## 数据库迁移

- [Flask-Migrate](https://github.com/miguelgrinberg/Flask-Migrate) - SQLAlchemy database migrations for Flask applications using Alembic

## 对话

- [Flask-Session](https://github.com/fengsp/flask-session) - Server side session extension for Flask

## 高速缓存

- [Flask-Caching](https://github.com/sh4nks/flask-caching) - Adds easy cache support to Flask
- [flask-heroku-cacheify](https://github.com/rdegges/flask-heroku-cacheify) - Automatic Flask cache configuration on Heroku

## 数据验证

- [Flask-WTF](https://github.com/lepture/flask-wtf) - Simple integration of Flask and WTForms, including CSRF, file upload and Recaptcha integration.

## 电子邮件

- [Flask-Mail](https://github.com/mattupstate/flask-mail/) - Flask-Mail adds SMTP mail sending to your Flask applications

## 国际化

- [flask-babel](https://github.com/python-babel/flask-babel) - i18n and l10n support for Flask based on Babel and pytz

## 全文检索

- [SQLAlchemy-Searchable](https://github.com/kvesteri/sqlalchemy-searchable) - Full-text searching for Flask-SQLAlchemy (Postgres only)
- [flask_msearch](https://github.com/honmaple/flask-msearch) - Full text search for flask with whoosh

## 限速

- [Flask-Limiter](https://github.com/alisaifee/flask-limiter) - Flask-Limiter provides rate limiting features to flask routes

## 任务队列

- [dramatiq](https://github.com/Bogdanp/dramatiq) - A fast and reliable distributed task processing library for Python 3
- [huey](https://github.com/coleifer/huey) - a little task queue for python
- [Flask-RQ](https://github.com/mattupstate/flask-rq) - RQ (Redis Queue) integration for Flask applications
- [celery](https://github.com/celery/celery/) - Distributed Task Queue

## 异常跟踪

- [sentry-sdk](https://github.com/getsentry/sentry-python) - Python client for [Sentry](https://sentry.io/welcome/).
- [airbrake-python](https://github.com/airbrake/airbrake-python) - Python client for [Airbrake](https://airbrake.io/)

## 追踪

- [flask-zipkin](https://github.com/qiajigou/flask-zipkin) - Distributed tracing with [Zipkin](https://zipkin.io/).
- [Flask-OpenTracing](https://github.com/opentracing-contrib/python-flask) - Distributed tracing with [OpenTracing](http://opentracing.io/).

## APM

- [elastic-apm](https://github.com/elastic/apm-agent-python) - Elastic APM agent for Python

## 其他 SDK

- [Flask-GoogleMaps](https://github.com/rochacbruno/Flask-GoogleMaps) - Build and embed google maps in our Flask templates
- [Flask-Gravatar](https://github.com/zzzsochi/Flask-Gravatar) - Small and simple gravatar usage in Flask
- [Flask-Pusher](https://github.com/iurisilvio/Flask-Pusher) - Pusher integration for Flask
- [Flask-Azure-Storage](https://github.com/alejoar/Flask-Azure-Storage) - Flask extension that provides integration with Azure Storage

## 前端

- [Flask-CORS](https://github.com/corydolphin/flask-cors) - A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible
- [flask-assets](https://github.com/miracle2k/flask-assets) - Flask webassets integration
- [flask-s3](https://github.com/e-dard/flask-s3) - Seamlessly serve your static assets of your Flask app from Amazon S3
- [Flask-SSLify](https://github.com/kennethreitz/flask-sslify) - Force SSL on your Flask app
- [Flask-HTMLmin](https://github.com/hamidfzm/Flask-HTMLmin) - Flask html minifier

## 开发（调试/测试/文档）

- [Flasgger](https://github.com/rochacbruno/flasgger) - Create API documentation for Flask views using Swagger 2.0 specs
- [flask-apispec](https://github.com/jmcarp/flask-apispec) - simple self-documenting APIs with flask
- [flask2postman](https://github.com/numberly/flask2postman) - Generate a Postman collection from your Flask application
- [flask_profiler](https://github.com/muatik/flask-profiler) - endpoint analyzer/profiler for Flask
- [Flask-DebugToolbar](https://github.com/mgood/flask-debugtoolbar) - A port of the django debug toolbar to flask
- [flask-debug-toolbar-mongo](https://github.com/cenkalti/flask-debug-toolbar-mongo) - MongoDB panel for the Flask Debug Toolbar
- [Flask-Testing](https://github.com/jarus/flask-testing) - Unittest extensions for Flask
- [pytest-flask](https://github.com/pytest-dev/pytest-flask) - A set of pytest fixtures to test Flask applications
- [Flask-MonitoringDashboard](https://github.com/flask-dashboard/Flask-MonitoringDashboard) - Automatically monitor the evolving performance of Flask/Python web services.
- [nplusone](https://github.com/jmcarp/nplusone#flask-sqlalchemy) - Auto-detect n+1 queries with Flask and SQLAlchemy
- [connexion](https://github.com/zalando/connexion) - Swagger/OpenAPI First framework for Python on top of Flask with automatic endpoint validation & OAuth2 support.

## Utils

- [flask-marshmallow](https://github.com/marshmallow-code/flask-marshmallow) Flask + marshmallow for beautiful APIs
- [flask-jsonrpc](https://github.com/cenobites/flask-jsonrpc) - A basic JSON-RPC implementation for your Flask-powered sites
- [Flask-Bcrypt](https://github.com/maxcountryman/flask-bcrypt) - Flask-Bcrypt is a Flask extension that provides bcrypt hashing utilities for your application
- [Mixer](https://github.com/klen/mixer) - Mixer is application to generate instances of Django or SQLAlchemy models
- [Flask-FeatureFlags](https://github.com/trustrachel/Flask-FeatureFlags) - A Flask extension that enables or disables features based on configuration
- [Flask-Reggie](https://github.com/rhyselsmore/flask-reggie) - Regex Converter for Flask URL Routes
- [Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO) - Socket.IO integration for Flask applications
- [Flask-Moment](https://github.com/miguelgrinberg/Flask-Moment) - Formatting of dates and times in Flask templates using moment.js
- [Flask-Paginate](https://github.com/lixxu/flask-paginate) - Pagination support for Flask
- [Flask-graphql](https://github.com/graphql-python/flask-graphql) - Adds GraphQL support to your Flask application

## 资源

### 教程

- [如何构建一个永不停机的新闻应用程序，几乎没有任何成本](http://blog.apps.npr.org/2013/02/14/app-template-redux.html) (by NPR)
- [使用 Flask 在 Python 中构建网站](http://maximebf.com/blog/2012/10/building-websites-in-python-with-flask/)
- [The Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [使用 Python 和 Flask 实现 RESTful Web API](http://blog.luisrei.com/articles/flaskrest.html)
- [发现 Flask - 使用 Flask 进行全栈 Web 开发](https://github.com/realpython/discover-flask)
- [Flaskr - Flask 介绍，测试驱动开发和 jQuery](https://github.com/mjhea0/flaskr-tdd)

### 课程

- [完整的堆栈基础](https://www.udacity.com/course/full-stack-foundations--ud088)
- [设计 RESTful API](https://www.udacity.com/course/designing-restful-apis--ud388)

### 图书

- [探索烧瓶](https://exploreflask.com/en/latest/)
- [Flask Web 开发](http://shop.oreilly.com/product/0636920031116.do)
- [真正的 Python](https://realpython.com)
- [学习 Flask 框架](https://www.packtpub.com/web-development/learning-flask-framework)
- [烧瓶蓝图](https://www.packtpub.com/web-development/flask-blueprints)
- [烧瓶框架食谱](https://www.packtpub.com/web-development/flask-framework-cookbook)
- [掌握烧瓶](https://www.packtpub.com/web-development/mastering-flask)
- [使用 Flask 构建 Web 应用程序](https://www.packtpub.com/web-development/building-web-applications-flask)

### 幻灯片

- [使用 Flask 创建漂亮的 REST API](http://pycoder.net/bospy/presentation.html)
- [高级烧瓶模式](https://speakerdeck.com/mitsuhiko/advanced-flask-patterns)
- [烧瓶的善良](https://speakerdeck.com/kennethreitz/flasky-goodness)
- [领域驱动设计（...与 Flask）](https://speakerdeck.com/mikedebo/domain-driven-design-dot-dot-dot-with-flask)
- [在 Flask 我们相信](https://speakerdeck.com/playpauseandstop/in-flask-we-trust)

### 影片

- [PyVideo](https://pyvideo.org/search.html?q=flask)
- [实用的 Flask Web 开发教程](https://www.youtube.com/playlist?list=PLQVvvaa0QuDc_owjTbIY4rbgXOFkUYOUB)

### 用烧瓶建造

- [zmusic-ng](https://git.zx2c4.com/zmusic-ng/) - ZX2C4 Music provides a web interface for playing and downloading music files using metadata.
- [GuitarFan](https://github.com/lowrain/GuitarFan) - guitar tab
- [June](https://github.com/pythoncn/june) - ~~python-china.org~~
- [Zerqu](https://github.com/lepture/zerqu) - ZERQU is a content-focused API-based platform. eg: [Python-China](https://python-china.org)
- [motiky](https://github.com/notedit/motiky)
- [missing](https://github.com/notedit/missing) - a list service called missing
- [thenewsmeme.com](https://github.com/danjac/newsmeme)
- [overholt](https://github.com/mattupstate/overholt) - Example Flask application illustrating common practices
- [pypress](https://github.com/laoqiu/pypress) - flask team blog
- [thepast.me](https://github.com/laiwei/thepast)
- [redispapa](https://github.com/no13bus/redispapa) - another redis monitor by using flask, angular, socket.io
- [flaskblog](https://github.com/defshine/flaskblog) - a simple blog system based on flask
- [cleanblog](https://github.com/defshine/cleanblog) - a clean blog system based on flask and mongoengine
- [Quokka CMS](https://github.com/rochacbruno/quokka) - CMS made with Flask and MongoDB
- [chat](https://github.com/lzyy/chat) - a live chat built with python (flask + gevent + apscheduler) + redis
- [chatapp](https://github.com/vinceprignano/chatapp) - Flask and Angular.js Chat Application using Socket.io
- [Frozen-Flask](https://github.com/Frozen-Flask/Frozen-Flask) - Freezes a Flask application into a set of static files
- [mcflyin](https://github.com/wrobstory/mcflyin) - A small timeseries transformation API built on Flask and Pandas
- [Skylines](https://github.com/skylines-project/skylines) - Live tracking, flight database and competition framework
- [airflow](https://github.com/apache/incubator-airflow) - Airflow is a system to programmatically author, schedule and monitor data pipelines.
- [timesketch](https://github.com/google/timesketch) - Collaborative forensics timeline analysis
- [changes](https://github.com/dropbox/changes) - A dashboard for your code. A build system.
- [security_monkey](https://github.com/Netflix/security_monkey) - monitors policy changes and alerts on insecure configurations in an AWS account.
- [securedrop](https://github.com/freedomofpress/securedrop)- an open-source whistleblower submission system that media organizations can use to securely accept documents from and communicate with anonymous sources.
- [sync_engine](https://github.com/nylas/sync-engine) - IMAP/SMTP sync system with modern APIs
- [cleansweep](https://github.com/AamAadmiParty/cleansweep) - Volunteer & Campaign Management System
- [indico](https://github.com/indico/indico) - a general-purpose event management web-based solution. It includes a full-blown conference organization workflow as well as tools for meeting management and room booking. It provides as well integration with video-conferencing solutions.
- [flaskbb](https://github.com/flaskbb/flaskbb) - A classic Forum Software in Python using Flask.
- [PythonBuddy](https://github.com/ethanchewy/PythonBuddy) - Online Python Editor With Live Syntax Checking and Execution

### 样板

- [fbone](https://github.com/imwilsonxu/fbone)
- [cookiecutter-flask](https://github.com/sloria/cookiecutter-flask)
- [Flask-Foundation](https://github.com/JackStouffer/Flask-Foundation)
- [flask-rest-template](https://github.com/alexandre/flask-rest-template)
- [gae-init](https://gae-init.appspot.com) - Flask boilerplate running on Google App Engine
- [Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder) - Simple and rapid application builder framework, built on top of Flask. includes detailed security, auto form generation, google charts and much more
