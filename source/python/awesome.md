# Awesome Python

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome Python frameworks, libraries, software and resources.

Inspired by [awesome-php](https://github.com/ziadoz/awesome-php).

- [Awesome Python ![Awesome](https://github.com/sindresorhus/awesome)](#awesome-python-awesomehttpsgithubcomsindresorhusawesome)
  - [管理面板](#%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BF)
  - [Algorithms and Design Patterns](#algorithms-and-design-patterns)
  - [Audio](#audio)
  - [Authentication](#authentication)
  - [Build Tools](#build-tools)
  - [Built-in Classes Enhancement](#built-in-classes-enhancement)
  - [CMS](#cms)
  - [Caching](#caching)
  - [ChatOps Tools](#chatops-tools)
  - [Code Analysis](#code-analysis)
  - [Command-line Tools](#command-line-tools)
  - [Compatibility](#compatibility)
  - [Computer Vision](#computer-vision)
  - [Concurrency and Parallelism](#concurrency-and-parallelism)
  - [Configuration](#configuration)
  - [Cryptography](#cryptography)
  - [Data Analysis](#data-analysis)
  - [Data Validation](#data-validation)
  - [Data Visualization](#data-visualization)
  - [Database](#database)
  - [Database Drivers](#database-drivers)
  - [Date and Time](#date-and-time)
  - [Debugging Tools](#debugging-tools)
  - [Deep Learning](#deep-learning)
  - [DevOps Tools](#devops-tools)
  - [Distributed Computing](#distributed-computing)
  - [Distribution](#distribution)
  - [Documentation](#documentation)
  - [Downloader](#downloader)
  - [E-commerce](#e-commerce)
  - [Editor Plugins and IDEs](#editor-plugins-and-ides)
  - [Email](#email)
  - [Environment Management](#environment-management)
  - [Files](#files)
  - [Foreign Function Interface](#foreign-function-interface)
  - [Forms](#forms)
  - [Functional Programming](#functional-programming)
  - [GUI](#gui)
  - [Game Development](#game-development)
  - [Geolocation](#geolocation)
  - [HTML Manipulation](#html-manipulation)
  - [HTTP](#http)
  - [Hardware](#hardware)
  - [Image Processing](#image-processing)
  - [Implementations](#implementations)
  - [Interactive Interpreter](#interactive-interpreter)
  - [Internationalization](#internationalization)
  - [Job Scheduler](#job-scheduler)
  - [Logging](#logging)
  - [Machine Learning](#machine-learning)
  - [Microsoft Windows](#microsoft-windows)
  - [Miscellaneous](#miscellaneous)
  - [Natural Language Processing](#natural-language-processing)
  - [Network Virtualization](#network-virtualization)
  - [Networking](#networking)
  - [News Feed](#news-feed)
  - [ORM](#orm)
  - [Package Management](#package-management)
  - [Package Repositories](#package-repositories)
  - [Permissions](#permissions)
  - [Processes](#processes)
  - [Queue](#queue)
  - [Recommender Systems](#recommender-systems)
  - [RESTful API](#restful-api)
  - [Robotics](#robotics)
  - [RPC Servers](#rpc-servers)
  - [Science](#science)

---

## 管理面板

_Libraries for administrative interfaces._

- [ajenti](https://github.com/ajenti/ajenti) - The admin panel your servers deserve.
- [django-grappelli](http://grappelliproject.com) - A jazzy skin for the Django Admin-Interface.
- [django-suit](http://djangosuit.com/) - Alternative Django Admin-Interface (free only for Non-commercial use).
- [django-xadmin](https://github.com/sshwsfc/xadmin) - Drop-in replacement of Django admin comes with lots of goodies.
- [flask-admin](https://github.com/flask-admin/flask-admin) - Simple and extensible administrative interface framework for Flask.
- [flower](https://github.com/mher/flower) - Real-time monitor and web admin for Celery.
- [wooey](https://github.com/wooey/wooey) - A Django app which creates automatic web UIs for Python scripts.

## 算法和设计模式

_Python implementation of algorithms and design patterns._

- [algorithms](https://github.com/keon/algorithms) - Minimal examples of data structures and algorithms in Python.
- [PyPattyrn](https://github.com/tylerlaberge/PyPattyrn) - A simple yet effective library for implementing common design patterns.
- [python-patterns](https://github.com/faif/python-patterns) - A collection of design patterns in Python.
- [sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/) - Fast, pure-Python implementation of SortedList, SortedDict, and SortedSet types.

## 音频

_Libraries for manipulating audio and its metadata._

- Audio
  - [audioread](https://github.com/beetbox/audioread) - Cross-library (GStreamer + Core Audio + MAD + FFmpeg) audio decoding.
  - [dejavu](https://github.com/worldveil/dejavu) - Audio fingerprinting and recognition.
  - [mingus](http://bspaans.github.io/python-mingus/) - An advanced music theory and notation package with MIDI file and playback support.
  - [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis) - Python Audio Analysis Library: Feature Extraction, Classification, Segmentation and Applications
  - [pydub](https://github.com/jiaaro/pydub) - Manipulate audio with a simple and easy high level interface.
  - [TimeSide](https://github.com/Parisson/TimeSide) - Open web audio processing framework.
- Metadata
  - [beets](https://github.com/beetbox/beets) - A music library manager and [MusicBrainz](https://musicbrainz.org/) tagger.
  - [eyeD3](https://github.com/nicfit/eyeD3) - A tool for working with audio files, specifically MP3 files containing ID3 metadata.
  - [mutagen](https://github.com/quodlibet/mutagen) - A Python module to handle audio metadata.
  - [tinytag](https://github.com/devsnd/tinytag) - A library for reading music meta data of MP3, OGG, FLAC and Wave files.

## 认证

_Libraries for implementing authentications schemes._

- OAuth
  - [authlib](https://github.com/lepture/authlib) - JavaScript Object Signing and Encryption draft implementation.
  - [django-allauth](https://github.com/pennersr/django-allauth) - Authentication app for Django that "just works."
  - [django-oauth-toolkit](https://github.com/evonove/django-oauth-toolkit) - OAuth 2 goodies for Django.
  - [oauthlib](https://github.com/idan/oauthlib) - A generic and thorough implementation of the OAuth request-signing logic.
  - [python-oauth2](https://github.com/joestump/python-oauth2) - A fully tested, abstract interface to creating OAuth clients and servers.
  - [python-social-auth](https://github.com/omab/python-social-auth) - An easy-to-setup social authentication mechanism.
- JWT
  - [pyjwt](https://github.com/jpadilla/pyjwt) - JSON Web Token implementation in Python.
  - [python-jose](https://github.com/mpdavis/python-jose/) - A JOSE implementation in Python.
  - [python-jwt](https://github.com/davedoesdev/python-jwt) - A module for generating and verifying JSON Web Tokens.

## 构建工具

_Compile software from source code._

- [BitBake](http://www.yoctoproject.org/docs/1.6/bitbake-user-manual/bitbake-user-manual.html) - A make-like build tool for embedded Linux.
- [buildout](http://www.buildout.org/en/latest/) - A build system for creating, assembling and deploying applications from multiple parts.
- [PlatformIO](https://github.com/platformio/platformio-core) - A console tool to build code with different development platforms.
- [pybuilder](https://github.com/pybuilder/pybuilder) - A continuous build tool written in pure Python.
- [SCons](http://www.scons.org/) - A software construction tool.

## 内置类增强功能

_Libraries for enhancing Python built-in classes._

- [dataclasses](https://docs.python.org/3/library/dataclasses.html) - (Python standard library) Data classes.
- [attrs](https://github.com/python-attrs/attrs) - Replacement for `__init__`, `__eq__`, `__repr__`, etc. boilerplate in class definitions.
- [bidict](https://github.com/jab/bidict) - Efficient, Pythonic bidirectional map data structures and related functionality..
- [Box](https://github.com/cdgriffith/Box) - Python dictionaries with advanced dot notation access.
- [DottedDict](https://github.com/carlosescri/DottedDict) - A library that provides a method of accessing lists and dicts with a dotted path notation.

## CMS

_Content Management Systems._

- [wagtail](https://wagtail.io/) - A Django content management system.
- [django-cms](https://www.django-cms.org/en/) - An Open source enterprise CMS based on the Django.
- [feincms](https://github.com/feincms/feincms) - One of the most advanced Content Management Systems built on Django.
- [Kotti](https://github.com/Kotti/Kotti) - A high-level, Pythonic web application framework built on Pyramid.
- [mezzanine](https://github.com/stephenmcd/mezzanine) - A powerful, consistent, and flexible content management platform.
- [plone](https://plone.org/) - A CMS built on top of the open source application server Zope.
- [quokka](https://github.com/rochacbruno/quokka) - Flexible, extensible, small CMS powered by Flask and MongoDB.

## 高速缓存

_Libraries for caching data._

- [beaker](https://github.com/bbangert/beaker) - A WSGI middleware for sessions and caching.
- [django-cache-machine](https://github.com/django-cache-machine/django-cache-machine) - Automatic caching and invalidation for Django models.
- [django-cacheops](https://github.com/Suor/django-cacheops) - A slick ORM cache with automatic granular event-driven invalidation.
- [dogpile.cache](http://dogpilecache.readthedocs.io/en/latest/) - dogpile.cache is next generation replacement for Beaker made by same authors.
- [HermesCache](https://pypi.python.org/pypi/HermesCache) - Python caching library with tag-based invalidation and dogpile effect prevention.
- [pylibmc](https://github.com/lericson/pylibmc) - A Python wrapper around the [libmemcached](https://libmemcached.org/libMemcached.html) interface.
- [python-diskcache](http://www.grantjenks.com/docs/diskcache/) - SQLite and file backed cache backend with faster lookups than memcached and redis.

## ChatOps 工具

_Libraries for chatbot development._

- [errbot](https://github.com/errbotio/errbot/) - The easiest and most popular chatbot to implement ChatOps.

## 代码分析

_Tools of static analysis, linters and code quality checkers. See: [awesome-static-analysis](https://github.com/mre/awesome-static-analysis)._

- Code Analysis
  - [coala](https://github.com/coala/coala/) - Language independent and easily extendable code analysis application.
  - [code2flow](https://github.com/scottrogowski/code2flow) - Turn your Python and JavaScript code into DOT flowcharts.
  - [prospector](https://github.com/PyCQA/prospector) - A tool to analyse Python code.
  - [pycallgraph](https://github.com/gak/pycallgraph) - A library that visualises the flow (call graph) of your Python application.
- Code Linters
  _ [flake8](https://pypi.python.org/pypi/flake8) - A wrapper around `pycodestyle`, `pyflakes` and McCabe.
  _ [pylint](https://www.pylint.org/) - A fully customizable source code analyzer.
  _ [pylama](https://github.com/klen/pylama) - A code audit tool for Python and JavaScript.
  Code Formatters
  _ [black](https://github.com/ambv/black) - The uncompromising Python code formatter. \* [yapf](https://github.com/google/yapf) - Yet another Python code formatter from Google.
- Static Type Checkers
  - [mypy](http://mypy-lang.org/) - Check variable types during compile time.
  - [pyre-check](https://github.com/facebook/pyre-check) - Performant type checking.
- Static Type Annotations Generators
  - [MonkeyType](https://github.com/Instagram/MonkeyType) - A system for Python that generates static type annotations by collecting runtime types

## 命令行工具

_Libraries for building command-line application._

- Command-line Application Development
  - [cement](http://builtoncement.com/) - CLI Application Framework for Python.
  - [click](http://click.pocoo.org/dev/) - A package for creating beautiful command line interfaces in a composable way.
  - [cliff](https://docs.openstack.org/developer/cliff/) - A framework for creating command-line programs with multi-level commands.
  - [clint](https://github.com/kennethreitz/clint) - Python Command-line Application Tools.
  - [docopt](http://docopt.org/) - Pythonic command line arguments parser.
  - [python-fire](https://github.com/google/python-fire) - A library for creating command line interfaces from absolutely any Python object.
  - [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) - A library for building powerful interactive command lines.
- Terminal Rendering
  - [asciimatics](https://github.com/peterbrittain/asciimatics) - A package to create full-screen text UIs (from interactive forms to ASCII animations).
  - [bashplotlib](https://github.com/glamp/bashplotlib) - Making basic plots in the terminal.
  - [colorama](https://pypi.python.org/pypi/colorama) - Cross-platform colored terminal text.
- Productivity Tools
  - [cookiecutter](https://github.com/audreyr/cookiecutter) - A command-line utility that creates projects from cookiecutters (project templates).
  - [doitlive](https://github.com/sloria/doitlive) - A tool for live presentations in the terminal.
  - [howdoi](https://github.com/gleitz/howdoi) - Instant coding answers via the command line.
  - [PathPicker](https://github.com/facebook/PathPicker) - Select files out of bash output.
  - [percol](https://github.com/mooz/percol) - Adds flavor of interactive selection to the traditional pipe concept on UNIX.
  - [thefuck](https://github.com/nvbn/thefuck) - Correcting your previous console command.
  - [tmuxp](https://github.com/tony/tmuxp) - A [tmux](https://github.com/tmux/tmux) session manager.
  - [try](https://github.com/timofurrer/try) - A dead simple CLI to try out python packages - it's never been easier.
- CLI Enhancements
  - [httpie](https://github.com/jakubroztocil/httpie) - A command line HTTP client, a user-friendly cURL replacement.
  - [kube-shell](https://github.com/cloudnativelabs/kube-shell) - An integrated shell for working with the Kubernetes CLI.
  - [mycli](https://github.com/dbcli/mycli) - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
  - [pgcli](https://github.com/dbcli/pgcli) - Postgres CLI with autocompletion and syntax highlighting.
  - [saws](https://github.com/donnemartin/saws) - A Supercharged [aws-cli](https://github.com/aws/aws-cli).

## 兼容性

_Libraries for migrating from Python 2 to 3._

- [python-future](http://python-future.org/index.html) - The missing compatibility layer between Python 2 and Python 3.
- [python-modernize](https://github.com/mitsuhiko/python-modernize) - Modernizes Python code for eventual Python 3 migration.
- [six](https://pypi.python.org/pypi/six) - Python 2 and 3 compatibility utilities.

## 计算机视觉

_Libraries for computer vision._

- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library.
- [pytesseract](https://github.com/madmaze/pytesseract) - Another wrapper for [Google Tesseract OCR](https://github.com/tesseract-ocr).
- [SimpleCV](http://simplecv.org/) - An open source framework for building computer vision applications.

## 并发和并行

_Libraries for concurrent and parallel execution. See [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio)._

- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html) - (Python standard library) A high-level interface for asynchronously executing callables.
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) - (Python standard library) Process-based parallelism.
- [eventlet](http://eventlet.net/) - Asynchronous framework with WSGI support.
- [gevent](http://www.gevent.org/) - A coroutine-based Python networking library that uses [greenlet](https://github.com/python-greenlet/greenlet).
- [uvloop](https://github.com/MagicStack/uvloop) - Ultra fast implementation of `asyncio` event loop on top of `libuv`.
- [scoop](https://github.com/soravux/scoop) - Scalable Concurrent Operations in Python.

## 配置

_Libraries for storing and parsing configuration options._

- [configobj](https://github.com/DiffSK/configobj) - INI file parser with validation.
- [configparser](https://docs.python.org/3/library/configparser.html) - (Python standard library) INI file parser.
- [profig](https://profig.readthedocs.io/en/default/) - Config from multiple formats with value conversion.
- [python-decouple](https://github.com/henriquebastos/python-decouple) - Strict separation of settings from code.

## 加密

- [cryptography](https://cryptography.io/en/latest/) - A package designed to expose cryptographic primitives and recipes to Python developers.
- [paramiko](https://github.com/paramiko/paramiko) - A Python (2.6+, 3.3+) implementation of the SSHv2 protocol, providing both client and server functionality.
- [passlib](https://passlib.readthedocs.io/en/stable/) - Secure password storage/hashing library, very high level.
- [pynacl](https://github.com/pyca/pynacl) - Python binding to the Networking and Cryptography (NaCl) library.

## 数据分析

_Libraries for data analyzing._

- [Blaze](https://github.com/blaze/blaze) - NumPy and Pandas interface to Big Data.
- [Open Mining](https://github.com/mining/mining) - Business Intelligence (BI) in Pandas interface.
- [Orange](https://orange.biolab.si/) - Data mining, data visualization, analysis and machine learning through visual programming or scripts.
- [Pandas](http://pandas.pydata.org/) - A library providing high-performance, easy-to-use data structures and data analysis tools.
- [Optimus](https://github.com/ironmussa/Optimus) - Cleansing, pre-processing, feature engineering, exploratory data analysis and easy Machine Learning with a PySpark backend.

## 数据验证

_Libraries for validating data. Used for forms in many cases._

- [Cerberus](https://github.com/pyeve/cerberus) - A lightweight and extensible data validation library.
- [colander](https://docs.pylonsproject.org/projects/colander/en/latest/) - Validating and deserializing data obtained via XML, JSON, an HTML form post.
- [Dash](https://plot.ly/products/dash/) - Built on top of Flask, React and Plotly aimed at analytical web applications.
  - [awesome-dash](https://github.com/Acrotrend/awesome-dash)
- [jsonschema](https://github.com/Julian/jsonschema) - An implementation of [JSON Schema](http://json-schema.org/) for Python.
- [schema](https://github.com/keleshev/schema) - A library for validating Python data structures.
- [Schematics](https://github.com/schematics/schematics) - Data Structure Validation.
- [valideer](https://github.com/podio/valideer) - Lightweight extensible data validation and adaptation library.
- [voluptuous](https://github.com/alecthomas/voluptuous) - A Python data validation library.

## 数据可视化

_Libraries for visualizing data. See: [awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization)._

- [Altair](https://github.com/altair-viz/altair) - Declarative statistical visualization library for Python.
- [Bokeh](https://github.com/bokeh/bokeh) - Interactive Web Plotting for Python.
- [bqplot](https://github.com/bloomberg/bqplot) - Interactive Plotting Library for the Jupyter Notebook
- [ggplot](https://github.com/yhat/ggpy) - Same API as ggplot2 for R.
- [Matplotlib](http://matplotlib.org/) - A Python 2D plotting library.
- [Pygal](http://www.pygal.org/en/latest/) - A Python SVG Charts Creator.
- [PyGraphviz](https://pypi.python.org/pypi/pygraphviz) - Python interface to [Graphviz](http://www.graphviz.org/).
- [PyQtGraph](http://www.pyqtgraph.org/) - Interactive and realtime 2D/3D/Image plotting and science/engineering widgets.
- [Seaborn](https://github.com/mwaskom/seaborn) - Statistical data visualization using Matplotlib.
- [VisPy](https://github.com/vispy/vispy) - High-performance scientific visualization based on OpenGL.

## 数据库

_Databases implemented in Python._

- [pickleDB](https://github.com/patx/pickledb) - A simple and lightweight key-value store for Python.
- [tinydb](https://github.com/msiemens/tinydb) - A tiny, document-oriented database.
- [ZODB](https://github.com/zopefoundation/ZODB) - A native object database for Python. A key-value and object graph database.

## 数据库驱动

_Libraries for connecting and operating databases._

- MySQL - [awesome-mysql](http://shlomi-noach.github.io/awesome-mysql/)
  - [mysqlclient](https://github.com/PyMySQL/mysqlclient-python) - MySQL connector with Python 3 support ([mysql-python](https://sourceforge.net/projects/mysql-python/) fork).
  - [PyMySQL](https://github.com/PyMySQL/PyMySQL) - A pure Python MySQL driver compatible to mysql-python.
- PostgreSQL - [awesome-postgres](https://github.com/dhamaniasad/awesome-postgres)
  - [psycopg2](http://initd.org/psycopg/) - The most popular PostgreSQL adapter for Python.
  - [queries](https://github.com/gmr/queries) - A wrapper of the psycopg2 library for interacting with PostgreSQL.
- Other Relational Databases
  - [pymssql](http://www.pymssql.org/en/latest/) - A simple database interface to Microsoft SQL Server.
- NoSQL Databases
  - [cassandra-driver](https://github.com/datastax/python-driver) - The Python Driver for Apache Cassandra.
  - [happybase](https://github.com/wbolster/happybase) - A developer-friendly library for Apache HBase.
  - [kafka-python](https://github.com/dpkp/kafka-python) - The Python client for Apache Kafka.
  - [py2neo](https://py2neo.org/) - Python wrapper client for Neo4j's restful interface.
  - [pymongo](https://github.com/mongodb/mongo-python-driver) - The official Python client for MongoDB.
  - [redis-py](https://github.com/andymccurdy/redis-py) - The Python client for Redis.
- Asynchronous Clients
  - [motor](https://github.com/mongodb/motor) - The async Python driver for MongoDB.
  - [Telephus](https://github.com/driftx/Telephus) - Twisted based client for Cassandra.
  - [txpostgres](https://github.com/wulczer/txpostgres) - Twisted based asynchronous driver for PostgreSQL.
  - [txRedis](https://github.com/deldotdr/txRedis) - Twisted based client for Redis.

## 日期和时间

_Libraries for working with dates and times._

- [Chronyk](https://github.com/KoffeinFlummi/Chronyk) - A Python 3 library for parsing human-written times and dates.
- [dateutil](https://github.com/dateutil/dateutil) - Extensions to the standard Python [datetime](https://docs.python.org/3/library/datetime.html) module.
- [delorean](https://github.com/myusuf3/delorean/) - A library for clearing up the inconvenient truths that arise dealing with datetimes.
- [moment](https://github.com/zachwill/moment) - A Python library for dealing with dates/times. Inspired by [Moment.js](http://momentjs.com/).
- [Pendulum](https://github.com/sdispater/pendulum) - Python datetimes made easy.
- [PyTime](https://github.com/shinux/PyTime) - A easy-use Python module which aims to operate date/time/datetime by string.
- [pytz](https://launchpad.net/pytz) - World timezone definitions, modern and historical. Brings the [tz database](https://en.wikipedia.org/wiki/Tz_database) into Python.
- [when.py](https://github.com/dirn/When.py) - Providing user-friendly functions to help perform common date and time actions.
- [maya](https://github.com/kennethreitz/maya) - Datetimes for Humans, Maya is mostly built around the headaches and use-cases around parsing datetime data from websites.

## 调试工具

_Libraries for debugging code._

- pdb-like Debugger
  - [ipdb](https://github.com/gotcha/ipdb) - IPython-enabled [pdb](https://docs.python.org/3/library/pdb.html).
  - [pdb++](https://github.com/antocuni/pdb) - Another drop-in replacement for pdb.
  - [pudb](https://github.com/inducer/pudb) - A full-screen, console-based Python debugger.
  - [wdb](https://github.com/Kozea/wdb) - An improbable web debugger through WebSockets.
- Tracing
  - [lptrace](https://github.com/khamidou/lptrace) - [strace](http://man7.org/linux/man-pages/man1/strace.1.html) for Python programs.
  - [manhole](https://github.com/ionelmc/python-manhole) - Debug service that will accept unix domain socket connections and present the stacktraces for all threads and an interactive prompt.
  - [pyringe](https://github.com/google/pyringe) - Debugger capable of attaching to and injecting code into Python processes.
  - [python-hunter](https://github.com/ionelmc/python-hunter) - A flexible code tracing toolkit.
- Profiler
  - [line_profiler](https://github.com/rkern/line_profiler) - Line-by-line profiling.
  - [memory_profiler](https://github.com/fabianp/memory_profiler) - Monitor Memory usage of Python code.
  - [profiling](https://github.com/what-studio/profiling) - An interactive Python profiler.
  - [py-spy](https://github.com/benfred/py-spy) - A sampling profiler for Python programs. Written in Rust.
  - [pyflame](https://github.com/uber/pyflame) - A ptracing profiler For Python.
  - [vprof](https://github.com/nvdv/vprof) - Visual Python profiler.
- Others
  - [icecream](https://github.com/gruns/icecream) - Inspect variables, expressions, and program execution with a single, simple function call.
  - [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) - Display various debug information for Django.
  - [django-devserver](https://github.com/dcramer/django-devserver) - A drop-in replacement for Django's runserver.
  - [flask-debugtoolbar](https://github.com/mgood/flask-debugtoolbar) - A port of the django-debug-toolbar to flask.
  - [pyelftools](https://github.com/eliben/pyelftools) - Parsing and analyzing ELF files and DWARF debugging information.

## 深度学习

_Frameworks for Neural Networks and Deep Learning. See: [awesome-deep-learning](https://github.com/ChristosChristofidis/awesome-deep-learning)._

- [caffe](https://github.com/BVLC/caffe) - A fast open framework for deep learning..
- [keras](https://github.com/keras-team/keras) - A high-level neural networks library and capable of running on top of either TensorFlow or Theano.
- [mxnet](https://github.com/dmlc/mxnet) - A deep learning framework designed for both efficiency and flexibility.
- [pytorch](https://github.com/pytorch/pytorch) - Tensors and Dynamic neural networks in Python with strong GPU acceleration.
- [SerpentAI](https://github.com/SerpentAI/SerpentAI) - Game agent framework. Use any video game as a deep learning sandbox.
- [tensorflow](https://github.com/tensorflow/tensorflow) - The most popular Deep Learning framework created by Google.
- [Theano](https://github.com/Theano/Theano) - A library for fast numerical computation.

## DevOps 工具

_Software and libraries for DevOps._

- [ansible](https://github.com/ansible/ansible) - A radically simple IT automation platform.
- [cloudinit](https://cloudinit.readthedocs.io/en/latest/) - A multi-distribution package that handles early initialization of a cloud instance.
- [cuisine](https://github.com/sebastien/cuisine) - Chef-like functionality for Fabric.
- [docker-compose](https://docs.docker.com/compose/) - Fast, isolated development environments using [Docker](https://www.docker.com/).
- [fabric](https://github.com/fabric/fabric) - A simple, Pythonic tool for remote execution and deployment.
- [fabtools](https://github.com/fabtools/fabtools) - Tools for writing awesome Fabric files.
- [honcho](https://github.com/nickstenning/honcho) - A Python clone of [Foreman](https://github.com/ddollar/foreman), for managing Procfile-based applications.
- [OpenStack](https://www.openstack.org/) - Open source software for building private and public clouds.
- [pexpect](https://github.com/pexpect/pexpect) - Controlling interactive programs in a pseudo-terminal like GNU expect.
- [psutil](https://github.com/giampaolo/psutil) - A cross-platform process and system utilities module.
- [saltstack](https://github.com/saltstack/salt) - Infrastructure automation and management system.
- [supervisor](https://github.com/Supervisor/supervisor) - Supervisor process control system for UNIX.

## 分布式计算

_Frameworks and libraries for Distributed Computing._

- Batch Processing
  - [PySpark](https://pypi.python.org/pypi/pyspark/) - [Apache Spark](https://spark.apache.org/) Python API.
  - [dask](https://github.com/dask/dask) - A flexible parallel computing library for analytic computing.
  - [luigi](https://github.com/spotify/luigi) - A module that helps you build complex pipelines of batch jobs.
  - [mrjob](https://github.com/Yelp/mrjob) - Run MapReduce jobs on Hadoop or Amazon Web Services.
  - [Ray](https://github.com/ray-project/ray/) - A system for parallel and distributed Python that unifies the machine learning ecosystem.
- Stream Processing
  - [faust](https://github.com/robinhood/faust) - A stream processing library, porting the ideas from [Kafka Streams](https://kafka.apache.org/documentation/streams/) to Python.
  - [streamparse](https://github.com/Parsely/streamparse) - Run Python code against real-time streams of data via [Apache Storm](http://storm.apache.org/).

## 分配

_Libraries to create packaged executables for release distribution._

- [dh-virtualenv](https://github.com/spotify/dh-virtualenv) - Build and distribute a virtualenv as a Debian package.
- [Nuitka](http://nuitka.net/) - Compile scripts, modules, packages to an executable or extension module.
- [py2app](http://pythonhosted.org/py2app/) - Freezes Python scripts (Mac OS X).
- [py2exe](http://www.py2exe.org/) - Freezes Python scripts (Windows).
- [PyInstaller](https://github.com/pyinstaller/pyinstaller) - Converts Python programs into stand-alone executables (cross-platform).
- [pynsist](http://pynsist.readthedocs.io/en/latest/) - A tool to build Windows installers, installers bundle Python itself.

## 文档

_Libraries for generating project documentation._

- [sphinx](https://github.com/sphinx-doc/sphinx/) - Python Documentation generator.
  - [awesome-sphinxdoc](https://github.com/yoloseem/awesome-sphinxdoc)
- [pdoc](https://github.com/mitmproxy/pdoc) - Epydoc replacement to auto generate API documentation for Python libraries.
- [pycco](https://github.com/pycco-docs/pycco) - The literate-programming-style documentation generator.

## 下载

_Libraries for downloading._

- [s3cmd](https://github.com/s3tools/s3cmd) - A command line tool for managing Amazon S3 and CloudFront.
- [s4cmd](https://github.com/bloomreach/s4cmd) - Super S3 command line tool, good for higher performance.
- [you-get](https://you-get.org/) - A YouTube/Youku/Niconico video downloader written in Python 3.
- [youtube-dl](https://rg3.github.io/youtube-dl/) - A small command-line program to download videos from YouTube.

## E-commerce

_Frameworks and libraries for e-commerce and payments._

- [alipay](https://github.com/lxneng/alipay) - Unofficial Alipay API for Python.
- [Cartridge](https://github.com/stephenmcd/cartridge) - A shopping cart app built using the Mezzanine.
- [django-oscar](http://oscarcommerce.com/) - An open-source e-commerce framework for Django.
- [django-shop](https://github.com/awesto/django-shop) - A Django based shop system.
- [merchant](https://github.com/agiliq/merchant) - A Django app to accept payments from various payment processors.
- [money](https://github.com/carlospalol/money) - Money class with optional CLDR-backed locale-aware formatting and an extensible currency exchange solution.
- [python-currencies](https://github.com/Alir3z4/python-currencies) - Display money format and its filthy currencies.
- [forex-python](https://github.com/MicroPyramid/forex-python) - Foreign exchange rates, Bitcoin price index and currency conversion.
- [saleor](http://getsaleor.com/) - An e-commerce storefront for Django.
- [shoop](https://www.shuup.com/en/) - An open source E-Commerce platform based on Django.

## 编辑器插件和 IDE

- Emacs
  - [elpy](https://github.com/jorgenschaefer/elpy) - Emacs Python Development Environment.
- Sublime Text
  - [anaconda](https://github.com/DamnWidget/anaconda) - Anaconda turns your Sublime Text 3 in a full featured Python development IDE.
  - [SublimeJEDI](https://github.com/srusskih/SublimeJEDI) - A Sublime Text plugin to the awesome auto-complete library Jedi.
- Vim
  - [jedi-vim](https://github.com/davidhalter/jedi-vim) - Vim bindings for the Jedi auto-completion library for Python.
  - [python-mode](https://github.com/python-mode/python-mode) - An all in one plugin for turning Vim into a Python IDE.
  - [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) - Includes [Jedi](https://github.com/davidhalter/jedi)-based completion engine for Python.
- Visual Studio
  - [PTVS](https://github.com/Microsoft/PTVS) - Python Tools for Visual Studio.
- Visual Studio Code
  - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) - An extension with rich support for the Python language, with features including linting, IntelliSense, formatting, refactoring, debugging, unit tests, and jupyter support.
- IDE
  - [PyCharm](https://www.jetbrains.com/pycharm/) - Commercial Python IDE by JetBrains. Has free community edition available.
  - [spyder](https://github.com/spyder-ide/spyder) - Open Source Python IDE.

## 电子邮件

_Libraries for sending and parsing email._

- [envelopes](http://tomekwojcik.github.io/envelopes/) - Mailing for human beings.
- [flanker](https://github.com/mailgun/flanker) - A email address and Mime parsing library.
- [imbox](https://github.com/martinrusev/imbox) - Python IMAP for Humans.
- [inbox.py](https://github.com/kennethreitz/inbox.py) - Python SMTP Server for Humans.
- [lamson](https://github.com/zedshaw/lamson) - Pythonic SMTP Application Server.
- [Marrow Mailer](https://github.com/marrow/mailer) - High-performance extensible mail delivery framework.
- [modoboa](https://github.com/modoboa/modoboa) - A mail hosting and management platform including a modern and simplified Web UI.
- [Nylas Sync Engine](https://github.com/nylas/sync-engine) - Providing a RESTful API on top of a powerful email sync platform.
- [yagmail](https://github.com/kootenpv/yagmail) - Yet another Gmail/SMTP client.

## 环境管理

_Libraries for Python version and environment management._

- [pipenv](https://github.com/kennethreitz/pipenv) - Sacred Marriage of Pipfile, Pip, & Virtualenv.
- [poetry](https://github.com/sdispater/poetry) - Python dependency management and packaging made easy.
- [pyenv](https://github.com/pyenv/pyenv) - Simple Python version management.
- [venv](https://docs.python.org/3/library/venv.html) - (Python standard library in Python 3.3+) Creating lightweight virtual environments.
- [virtualenv](https://pypi.python.org/pypi/virtualenv) - A tool to create isolated Python environments.

## Files

_Libraries for file manipulation and MIME type detection._

- [mimetypes](https://docs.python.org/3/library/mimetypes.html) - (Python standard library) Map filenames to MIME types.
- [path.py](https://github.com/jaraco/path.py) - A module wrapper for [os.path](https://docs.python.org/3/library/os.path.html).
- [pathlib](https://docs.python.org/3/library/pathlib.html) - (Python standard library) An cross-platform, object-oriented path library.
- [PyFilesystem2](https://github.com/pyfilesystem/pyfilesystem2) - Python's filesystem abstraction layer.
- [python-magic](https://github.com/ahupp/python-magic) - A Python interface to the libmagic file type identification library.
- [Unipath](https://github.com/mikeorr/Unipath) - An object-oriented approach to file/directory operations.
- [watchdog](https://github.com/gorakhargosh/watchdog) - API and shell utilities to monitor file system events.

## 外部函数接口

_Libraries for providing foreign function interface._

- [cffi](https://pypi.python.org/pypi/cffi) - Foreign Function Interface for Python calling C code.
- [ctypes](https://docs.python.org/3/library/ctypes.html) - (Python standard library) Foreign Function Interface for Python calling C code.
- [PyCUDA](https://mathema.tician.de/software/pycuda/) - A Python wrapper for Nvidia's CUDA API.
- [SWIG](http://www.swig.org/Doc1.3/Python.html) - Simplified Wrapper and Interface Generator.

## Forms

_Libraries for working with forms._

- [Deform](https://github.com/Pylons/deform) - Python HTML form generation library influenced by the formish form generation library.
- [django-bootstrap3](https://github.com/dyve/django-bootstrap3) - Bootstrap 3 integration with Django.
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - A Django app which lets you create beautiful forms in a very elegant and DRY way.
- [django-remote-forms](https://github.com/WiserTogether/django-remote-forms) - A platform independent Django form serializer.
- [WTForms](https://github.com/wtforms/wtforms) - A flexible forms validation and rendering library.

## 功能编程

_Functional Programming with Python._

- [Coconut](http://coconut-lang.org/) - Coconut is a variant of Python built for simple, elegant, Pythonic functional programming.
- [CyToolz](https://github.com/pytoolz/cytoolz/) - Cython implementation of Toolz: High performance functional utilities.
- [fn.py](https://github.com/kachayev/fn.py) - Functional programming in Python: implementation of missing features to enjoy FP.
- [funcy](https://github.com/Suor/funcy) - A fancy and practical functional tools.
- [Toolz](https://github.com/pytoolz/toolz) - A collection of functional utilities for iterators, functions, and dictionaries.

## GUI

_Libraries for working with graphical user interface applications._

- [curses](https://docs.python.org/3/library/curses.html) - Built-in wrapper for [ncurses](http://www.gnu.org/software/ncurses/) used to create terminal GUI applications.
- [Eel](https://github.com/ChrisKnott/Eel) - Little library for making simple Electron-like offline HTML/JS GUI apps, with full access to Python capabilities and libraries.
- [enaml](https://github.com/nucleic/enaml) - Creating beautiful user-interfaces with Declaratic Syntax like QML.
- [Flexx](https://github.com/zoofIO/flexx) - Flexx is a pure Python toolkit for creating GUI's, that uses web technology for its rendering.
- [Gooey](https://github.com/chriskiehl/Gooey) - Turn command line programs into a full GUI application with one line.
- [kivy](https://kivy.org/) - A library for creating NUI applications, running on Windows, Linux, Mac OS X, Android and iOS.
- [pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home) - A cross-platform windowing and multimedia library for Python.
- [PyGObject](https://wiki.gnome.org/Projects/PyGObject) - Python Bindings for GLib/GObject/GIO/GTK+ (GTK+3).
- [PyQt](https://riverbankcomputing.com/software/pyqt/intro) - Python bindings for the [Qt](https://www.qt.io/) cross-platform application and UI framework, with support for both Qt v4 and Qt v5 frameworks.
- [PySide](https://wiki.qt.io/PySide) - Python bindings for the [Qt](http://www.qt.io/) cross-platform application and UI framework, supporting the Qt v4 framework.
- [PySimpleGUI](https://github.com/PySimpleGUI/PySimpleGUI) - Wrapper for tkinter, Qt, WxPython and Remi that creates a unified, easy to understand & more Python-like interface for beginner and intermediate level custom GUIs.
- [pywebview](https://github.com/r0x0r/pywebview/) - A lightweight cross-platform native wrapper around a webview component that allows to display HTML content in its own native dedicated window.
- [Tkinter](https://wiki.python.org/moin/TkInter) - Tkinter is Python's de-facto standard GUI package.
- [Toga](https://github.com/pybee/toga) - A Python native, OS native GUI toolkit.
- [urwid](http://urwid.org/) - A library for creating terminal GUI applications with strong support for widgets, events, rich colors, etc.
- [wxPython](https://wxpython.org/) - A blending of the wxWidgets C++ class library with the Python.

## 游戏开发

_Awesome game development libraries._

- [Cocos2d](http://cocos2d.org/) - cocos2d is a framework for building 2D games, demos, and other graphical/interactive applications. It is based on pyglet.
- [Harfang3D](http://www.harfang3d.com) - Python framework for 3D, VR and game development. Manage and display complex 3D scenes, with physics, video, sound and music, access VR devices. All written in C++.
- [Panda3D](https://www.panda3d.org/) - 3D game engine developed by Disney and maintained by Carnegie Mellon's Entertainment Technology Center. Written in C++, completely wrapped in Python.
- [Pygame](http://www.pygame.org/news.html) - Pygame is a set of Python modules designed for writing games.
- [PyOgre](http://www.ogre3d.org/tikiwiki/PyOgre) - Python bindings for the Ogre 3D render engine, can be used for games, simulations, anything 3D.
- [PyOpenGL](http://pyopengl.sourceforge.net/) - Python ctypes bindings for OpenGL and it's related APIs.
- [PySDL2](https://pysdl2.readthedocs.io) - A ctypes based wrapper for the SDL2 library.
- [RenPy](https://www.renpy.org/) - A Visual Novel engine.

## 地理位置

_Libraries for geocoding addresses and working with latitudes and longitudes._

- [django-countries](https://github.com/SmileyChris/django-countries) - A Django app that provides country choices for use with forms, flag icons static files, and a country field for models.
- [GeoDjango](https://docs.djangoproject.com/en/dev/ref/contrib/gis/) - A world-class geographic web framework.
- [GeoIP](https://github.com/maxmind/geoip-api-python) - Python API for MaxMind GeoIP Legacy Database.
- [geojson](https://github.com/frewsxcv/python-geojson) - Python bindings and utilities for GeoJSON.
- [geopy](https://github.com/geopy/geopy) - Python Geocoding Toolbox.
- [pygeoip](https://github.com/appliedsec/pygeoip) - Pure Python GeoIP API.

## HTML 操作

_Libraries for working with HTML and XML._

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Providing Pythonic idioms for iterating, searching, and modifying HTML or XML.
- [bleach](https://github.com/mozilla/bleach) - A whitelist-based HTML sanitization and text linkification library.
- [cssutils](https://pypi.python.org/pypi/cssutils/) - A CSS library for Python.
- [html5lib](https://github.com/html5lib/html5lib-python) - A standards-compliant library for parsing and serializing HTML documents and fragments.
- [lxml](http://lxml.de/) - A very fast, easy-to-use and versatile library for handling HTML and XML.
- [MarkupSafe](https://github.com/pallets/markupsafe) - Implements a XML/HTML/XHTML Markup safe string for Python.
- [pyquery](https://github.com/gawel/pyquery) - A jQuery-like library for parsing HTML.
- [untangle](https://github.com/stchris/untangle) - Converts XML documents to Python objects for easy access.
- [WeasyPrint](http://weasyprint.org) - A visual rendering engine for HTML and CSS that can export to PDF.
- [xmldataset](https://xmldataset.readthedocs.io/en/latest/) - Simple XML Parsing.
- [xmltodict](https://github.com/martinblech/xmltodict) - Working with XML feel like you are working with JSON.

## HTTP

_Libraries for working with HTTP._

- [grequests](https://github.com/kennethreitz/grequests) - requests + gevent for asynchronous HTTP requests.
- [httplib2](https://github.com/httplib2/httplib2) - Comprehensive HTTP client library.
- [requests](http://docs.python-requests.org/en/latest/) - HTTP Requests for Humans™.
- [treq](https://github.com/twisted/treq) - Python requests like API built on top of Twisted's HTTP client.
- [urllib3](https://github.com/shazow/urllib3) - A HTTP library with thread-safe connection pooling, file post support, sanity friendly.

## 硬件

_Libraries for programming with hardware._

- [ino](http://inotool.org/) - Command line toolkit for working with [Arduino](https://www.arduino.cc/).
- [keyboard](https://github.com/boppreh/keyboard) - Hook and simulate global keyboard events on Windows and Linux.
- [mouse](https://github.com/boppreh/mouse) - Hook and simulate global mouse events on Windows and Linux.
- [Pingo](http://www.pingo.io/) - Pingo provides a uniform API to program devices like the Raspberry Pi, pcDuino, Intel Galileo, etc.
- [PyUserInput](https://github.com/SavinaRoja/PyUserInput) - A module for cross-platform control of the mouse and keyboard.
- [scapy](https://github.com/secdev/scapy) - A brilliant packet manipulation library.
- [wifi](https://github.com/rockymeza/wifi) - A Python library and command line tool for working with WiFi on Linux.

## 图像处理

_Libraries for manipulating images._

- [hmap](https://github.com/rossgoodwin/hmap) - Image histogram remapping.
- [imgSeek](https://sourceforge.net/projects/imgseek/) - A project for searching a collection of images using visual similarity.
- [nude.py](https://github.com/hhatto/nude.py) - Nudity detection.
- [pagan](https://github.com/daboth/pagan) - Retro identicon (Avatar) generation based on input string and hash.
- [pillow](https://github.com/python-pillow/Pillow) - Pillow is the friendly [PIL](http://www.pythonware.com/products/pil/) fork.
- [pyBarcode](https://pythonhosted.org/pyBarcode/) - Create barcodes in Python without needing PIL.
- [pygram](https://github.com/ajkumar25/pygram) - Instagram-like image filters.
- [python-qrcode](https://github.com/lincolnloop/python-qrcode) - A pure Python QR Code generator.
- [Quads](https://github.com/fogleman/Quads) - Computer art based on quadtrees.
- [scikit-image](http://scikit-image.org/) - A Python library for (scientific) image processing.
- [thumbor](https://github.com/thumbor/thumbor) - A smart imaging service. It enables on-demand crop, re-sizing and flipping of images.
- [wand](https://github.com/dahlia/wand) - Python bindings for [MagickWand](http://www.imagemagick.org/script/magick-wand.php), C API for ImageMagick.

## 实现

_Implementations of Python._

- [CLPython](https://github.com/metawilm/cl-python) - Implementation of the Python programming language written in Common Lisp.
- [CPython](https://github.com/python/cpython) - **Default, most widely used implementation of the Python programming language written in C.**
- [Cython](http://cython.org/) - Optimizing Static Compiler for Python. Uses type mixins to compile Python into C or C++ modules resulting in large performance gains
- [Grumpy](https://github.com/google/grumpy) - More compiler than interpreter as more powerful CPython2.7 replacement (alpha).
- [IronPython](https://github.com/IronLanguages/ironpython3) - Implementation of the Python programming language written in C# targeting the .NET Framework and Mono.
- [Jython](https://hg.python.org/jython) - Implementation of Python programming language written in Java for the Java virtual machine (JVM).
- [MicroPython](https://github.com/micropython/micropython) - MicroPython - a lean and efficient Python programming language implementation for microcontrollers and constrained systems
- [Numba](http://numba.pydata.org/) - Python JIT compiler to LLVM aimed at scientific Python.
- [PeachPy](https://github.com/Maratyszcza/PeachPy) - x86-64 assembler embedded in Python. Can be used as inline assembler for Python or as a stand-alone assembler for Windows, Linux, OS X, Native Client and Go.
- [Pyjion](https://github.com/Microsoft/Pyjion) - A JIT for Python based upon CoreCLR.
- [PyPy](https://bitbucket.org/pypy/pypy) - Implementation of the Python programming language written in RPython and translated into C. PyPy focuses on speed, efficiency and compatibility with the original CPython interpreter. The interpreter uses black magic to make Python very fast without having to add in additional type information.
- [PySec](https://github.com/ebranca/owasp-pysec) - Hardened version of python that makes it easier for security professionals and developers to write applications more resilient to attacks and manipulations.
- [Pyston](https://github.com/dropbox/pyston) - A Python implementation built using LLVM and modern JIT techniques with the goal of achieving good performance.
- [Stackless Python](https://github.com/stackless-dev/stackless/wiki) - An enhanced version of the Python programming language which allows programmers to reap the benefits of thread-based programming without the performance and complexity problems associated with conventional threads.

## 互动口译员

_Interactive Python interpreters (REPL)._

- [bpython](https://github.com/bpython/bpython) - A fancy interface to the Python interpreter.
- [Jupyter Notebook (IPython)](https://jupyter.org) - A rich toolkit to help you make the most out of using Python interactively.
  - [awesome-jupyter](https://github.com/markusschanta/awesome-jupyter)
- [ptpython](https://github.com/jonathanslenders/ptpython) - Advanced Python REPL built on top of the [python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit).

## 国际化

_Libraries for working with i18n._

- [Babel](http://babel.pocoo.org/en/latest/) - An internationalization library for Python.
- [PyICU](https://github.com/ovalhub/pyicu) - A wrapper of International Components for Unicode C++ library ([ICU](http://site.icu-project.org/)).

## 工作安排

_Libraries for scheduling jobs._

- [APScheduler](http://apscheduler.readthedocs.io/en/latest/) - A light but powerful in-process task scheduler that lets you schedule functions.
- [django-schedule](https://github.com/thauber/django-schedule) - A calendaring app for Django.
- [doit](http://pydoit.org/) - A task runner and build tool.
- [gunnery](https://github.com/gunnery/gunnery) - Multipurpose task execution tool for distributed systems with web-based interface.
- [Joblib](http://pythonhosted.org/joblib/index.html) - A set of tools to provide lightweight pipelining in Python.
- [Plan](https://github.com/fengsp/plan) - Writing crontab file in Python like a charm.
- [schedule](https://github.com/dbader/schedule) - Python job scheduling for humans.
- [Spiff](https://github.com/knipknap/SpiffWorkflow) - A powerful workflow engine implemented in pure Python.
- [TaskFlow](https://docs.openstack.org/developer/taskflow/) - A Python library that helps to make task execution easy, consistent and reliable.
- [Airflow](https://airflow.apache.org/) - Airflow is a platform to programmatically author, schedule and monitor workflows.

## 记录

_Libraries for generating and working with logs._

- [Eliot](https://github.com/ScatterHQ/eliot) - Logging for complex & distributed systems.
- [logbook](http://logbook.readthedocs.io/en/stable/) - Logging replacement for Python.
- [logging](https://docs.python.org/3/library/logging.html) - (Python standard library) Logging facility for Python.
- [raven](https://github.com/getsentry/raven-python) - Python client for Sentry, a log/error tracking, crash reporting and aggregation platform for web applications.

## 机器学习

_Libraries for Machine Learning. See: [awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning#python)._

- [H2O](https://github.com/h2oai/h2o-3) - Open Source Fast Scalable Machine Learning Platform.
- [Metrics](https://github.com/benhamner/Metrics) - Machine learning evaluation metrics.
- [NuPIC](https://github.com/numenta/nupic) - Numenta Platform for Intelligent Computing.
- [scikit-learn](http://scikit-learn.org/) - The most popular Python library for Machine Learning.
- [Spark ML](http://spark.apache.org/docs/latest/ml-guide.html) - [Apache Spark](http://spark.apache.org/)'s scalable Machine Learning library.
- [vowpal_porpoise](https://github.com/josephreisinger/vowpal_porpoise) - A lightweight Python wrapper for [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/).
- [xgboost](https://github.com/dmlc/xgboost) - A scalable, portable, and distributed gradient boosting library.

## Microsoft Windows

_Python programming on Microsoft Windows._

- [Python(x,y)](http://python-xy.github.io/) - Scientific-applications-oriented Python Distribution based on Qt and Spyder.
- [pythonlibs](http://www.lfd.uci.edu/~gohlke/pythonlibs/) - Unofficial Windows binaries for Python extension packages.
- [PythonNet](https://github.com/pythonnet/pythonnet) - Python Integration with the .NET Common Language Runtime (CLR).
- [PyWin32](https://sourceforge.net/projects/pywin32/) - Python Extensions for Windows.
- [WinPython](https://winpython.github.io/) - Portable development environment for Windows 7/8.

## 杂

_Useful libraries or tools that don't fit in the categories above._

- [blinker](https://github.com/jek/blinker) - A fast Python in-process signal/event dispatching system.
- [boltons](https://github.com/mahmoud/boltons) - A set of pure-Python utilities.
- [itsdangerous](https://github.com/pallets/itsdangerous) - Various helpers to pass trusted data to untrusted environments.
- [pluginbase](https://github.com/mitsuhiko/pluginbase) - A simple but flexible plugin system for Python.
- [tryton](http://www.tryton.org/) - A general purpose business framework.

## 自然语言处理

_Libraries for working with human languages._

- General
  - [gensim](https://github.com/RaRe-Technologies/gensim) - Topic Modelling for Humans.
  - [langid.py](https://github.com/saffsd/langid.py) - Stand-alone language identification system.
  - [nltk](http://www.nltk.org/) - A leading platform for building Python programs to work with human language data.
  - [pattern](https://github.com/clips/pattern) - A web mining module for the Python.
  - [polyglot](https://github.com/aboSamoor/polyglot) - Natural language pipeline supporting hundreds of languages.
  - [pytext](https://github.com/facebookresearch/pytext) - A natural language modeling framework based on PyTorch.
  - [PyTorch-NLP](https://github.com/PetrochukM/PyTorch-NLP) - A toolkit enabling rapid deep learning NLP prototyping for research.
  - [spacy](https://spacy.io/) - A library for industrial-strength natural language processing in Python and Cython.
  - [stanfordnlp](https://github.com/stanfordnlp/stanfordnlp) - The Stanford NLP Group's official Python library, supporting 50+ languages.
- Chinese
  - [jieba](https://github.com/fxsjy/jieba) - The most popular Chinese text segmentation library.
  - [pkuseg-python](https://github.com/lancopku/pkuseg-python) - A toolkit for Chinese word segmentation in various domains.
  - [snownlp](https://github.com/isnowfy/snownlp) - A library for processing Chinese text.
  - [funNLP](https://github.com/fighting41love/funNLP) - A collection of tools and datasets for Chinese NLP.

## 网络虚拟化

_Tools and libraries for Virtual Networking and SDN (Software Defined Networking)._

- [mininet](https://github.com/mininet/mininet) - A popular network emulator and API written in Python.
- [pox](https://github.com/noxrepo/pox) - A Python-based SDN control applications, such as OpenFlow SDN controllers.

## 联网

_Libraries for networking programming._

- [asyncio](https://docs.python.org/3/library/asyncio.html) - (Python standard library) Asynchronous I/O, event loop, coroutines and tasks.
  - [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio)
- [pulsar](https://github.com/quantmind/pulsar) - Event-driven concurrent framework for Python.
- [pyzmq](https://github.com/zeromq/pyzmq) - A Python wrapper for the ZeroMQ message library.
- [Twisted](https://twistedmatrix.com/trac/) - An event-driven networking engine.
- [napalm](https://github.com/napalm-automation/napalm) - Cross-vendor API to manipulate network devices.

## 新闻 Feed

_Libraries for building user's activities._

- [django-activity-stream](https://github.com/justquick/django-activity-stream) - Generating generic activity streams from the actions on your site.
- [Stream Framework](https://github.com/tschellenbach/Stream-Framework) - Building newsfeed and notification systems using Cassandra and Redis.

## ORM

_Libraries that implement Object-Relational Mapping or data mapping techniques._

- Relational Databases
  - [Django Models](https://docs.djangoproject.com/en/dev/topics/db/models/) - A part of Django.
  - [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper.
    - [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy)
  - [dataset](https://github.com/pudo/dataset) - Store Python dicts in a database - works with SQLite, MySQL, and PostgreSQL.
  - [orator](https://github.com/sdispater/orator) - The Orator ORM provides a simple yet beautiful ActiveRecord implementation.
  - [peewee](https://github.com/coleifer/peewee) - A small, expressive ORM.
  - [pony](https://github.com/ponyorm/pony/) - ORM that provides a generator-oriented interface to SQL.
  - [pydal](https://github.com/web2py/pydal/) - A pure Python Database Abstraction Layer.
- NoSQL Databases
  - [hot-redis](https://github.com/stephenmcd/hot-redis) - Rich Python data types for Redis.
  - [mongoengine](https://github.com/MongoEngine/mongoengine) - A Python Object-Document-Mapper for working with MongoDB.
  - [PynamoDB](https://github.com/pynamodb/PynamoDB) - A Pythonic interface for [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).
  - [redisco](https://github.com/kiddouk/redisco) - A Python Library for Simple Models and Containers Persisted in Redis.

## 包管理

_Libraries for package and dependency management._

- [pip](https://pip.pypa.io/en/stable/) - The Python package and dependency manager.
  - [PyPI](https://pypi.org/)
  - [pip-tools](https://github.com/jazzband/pip-tools) - A set of tools to keep your pinned Python dependencies fresh.
- [conda](https://github.com/conda/conda/) - Cross-platform, Python-agnostic binary package manager.

## 包存储库

_Local PyPI repository server and proxies._

- [warehouse](https://github.com/pypa/warehouse) - Next generation Python Package Repository (PyPI).
- [bandersnatch](https://github.com/pypa/bandersnatch/) - PyPI mirroring tool provided by Python Packaging Authority (PyPA).
- [devpi](https://github.com/devpi/devpi) - PyPI server and packaging/testing/release tool.
- [localshop](https://github.com/jazzband/localshop) - Local PyPI server (custom packages and auto-mirroring of pypi).

## 权限

_Libraries that allow or deny users access to data or functionality._

- [django-guardian](https://github.com/django-guardian/django-guardian) - Implementation of per object permissions for Django 1.2+
- [django-rules](https://github.com/dfunckt/django-rules) - A tiny but powerful app providing object-level permissions to Django, without requiring a database.

## 流程

_Libraries for starting and communicating with OS processes._

- [delegator.py](https://github.com/kennethreitz/delegator.py) - [Subprocesses](https://docs.python.org/3.6/library/subprocess.html) for Humans™ 2.0.
- [sarge](https://sarge.readthedocs.io/en/latest/) - Yet another wrapper for subprocess.
- [sh](https://github.com/amoffat/sh) - A full-fledged subprocess replacement for Python.

## 队列

_Libraries for working with event and task queues._

- [celery](http://www.celeryproject.org/) - An asynchronous task queue/job queue based on distributed message passing.
- [huey](https://github.com/coleifer/huey) - Little multi-threaded task queue.
- [mrq](https://github.com/pricingassistant/mrq) - Mr. Queue - A distributed worker task queue in Python using Redis & gevent.
- [rq](https://github.com/rq/rq) - Simple job queues for Python.

## 推荐系统

_Libraries for building recommender systems._

- [annoy](https://github.com/spotify/annoy) - Approximate Nearest Neighbors in C++/Python optimized for memory usage.
- [fastFM](https://github.com/ibayer/fastFM) - A library for Factorization Machines.
- [implicit](https://github.com/benfred/implicit) - A fast Python implementation of collaborative filtering for implicit datasets.
- [libffm](https://github.com/guestwalk/libffm) - A library for Field-aware Factorization Machine (FFM).
- [lightfm](https://github.com/lyst/lightfm) - A Python implementation of a number of popular recommendation algorithms.
- [spotlight](https://github.com/maciejkula/spotlight) - Deep recommender models using PyTorch.
- [Surprise](https://github.com/NicolasHug/Surprise) - A scikit for building and analyzing recommender systems.
- [tensorrec](https://github.com/jfkirk/tensorrec) - A Recommendation Engine Framework in TensorFlow.

## RESTful API

_Libraries for developing RESTful APIs._

- Django
  - [django-rest-framework](http://www.django-rest-framework.org/) - A powerful and flexible toolkit to build web APIs.
  - [django-tastypie](http://tastypieapi.org/) - Creating delicious APIs for Django apps.
- Flask
  - [eve](https://github.com/pyeve/eve) - REST API framework powered by Flask, MongoDB and good intentions.
  - [flask-api-utils](https://github.com/marselester/flask-api-utils) - Taking care of API representation and authentication for Flask.
  - [flask-api](http://www.flaskapi.org/) - Browsable Web APIs for Flask.
  - [flask-restful](https://github.com/flask-restful/flask-restful) - Quickly building REST APIs for Flask.
  - [flask-restless](https://github.com/jfinkels/flask-restless) - Generating RESTful APIs for database models defined with SQLAlchemy.
- Pyramid
  - [cornice](https://github.com/Cornices/cornice) - A RESTful framework for Pyramid.
- Framework agnostic
  - [apistar](https://github.com/encode/apistar) - A smart Web API framework, designed for Python 3.
  - [falcon](http://falconframework.org/) - A high-performance framework for building cloud APIs and web app backends.
  - [hug](https://github.com/timothycrosley/hug) - A Python3 framework for cleanly exposing APIs over HTTP and the Command Line with automatic documentation and validation.
  - [restless](https://github.com/toastdriven/restless) - Framework agnostic REST framework based on lessons learned from Tastypie.
  - [ripozo](https://github.com/vertical-knowledge/ripozo) - Quickly creating REST/HATEOAS/Hypermedia APIs.
  - [sandman](https://github.com/jeffknupp/sandman) - Automated REST APIs for existing database-driven systems.

## 机器人

_Libraries for robotics._

- [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) - This is a compilation of various robotics algorithms with visualizations.
- [rospy](http://wiki.ros.org/rospy) - This is a library for ROS (Robot Operating System).

## RPC 服务器

_RPC-compatible servers._

- [SimpleJSONRPCServer](https://github.com/joshmarshall/jsonrpclib/) - This library is an implementation of the JSON-RPC specification.
- [SimpleXMLRPCServer](https://docs.python.org/3/library/xmlrpc.server.html) - (Python standard library) Simple XML-RPC server implementation, single-threaded.
- [zeroRPC](https://github.com/0rpc/zerorpc-python) - zerorpc is a flexible RPC implementation based on [ZeroMQ](http://zeromq.org/) and [MessagePack](http://msgpack.org/).

## 科学

_Libraries for scientific computing._

- [astropy](http://www.astropy.org/) - A community Python library for Astronomy.
- [bcbio-nextgen](https://github.com/chapmanb/bcbio-nextgen) - Providing best-practice pipelines for fully automated high throughput sequencing analysis.
- [bccb](https://github.com/chapmanb/bcbb) - Collection of
