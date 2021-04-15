# OS X 构建说明和注释

在OS X上构建`twisterd`指南

## 注释

* Tested on OS X 10.9.1 on Intel processors only. PPC is not supported because it is big-endian.
* All of the commands should be executed in a Terminal application. The built-in one is located in `/Applications/Utilities`.

## 准备

### 安装Xcode

你需要安装`Xcode`并打上所有选项这样编译器和所有东西可在在目录`/usr`并不只是在 `/Developer`.
Xcode should be available on your OS X installation media, but if not,
你可以在[https://developer.apple.com/xcode/](https://developer.apple.com/xcode/)获取当前版本.
如果安装 Xcode 4.3 或者更新版本, 你需要安装命令行工具.
This can be done in `Xcode > Preferences > Downloads > Components` and generally must be re-done or updated every time Xcode is updated.

### 安装Git

There's an assumption that you already have `git` installed, as well.
If not, it's the path of least resistance to install [GitHub Desktop](https://desktop.github.com/)或者[Git for OS X](https://code.google.com/p/git-osx-installer/).
It is also available via Homebrew or MacPorts.

### 安装Homebrew

你也需要安装[Homebrew](http://brew.sh/)或者[MacPorts](https://www.macports.org/)用来安装依赖库. It's largely a religious decision which to choose, but I tested only with Homebrew.

The installation of the actual dependencies is covered in the Instructions sections below.

## Homebrew

### 安装依赖

```sh
  brew install boost miniupnpc openssl berkeley-db4 autoconf automake libtool
```

### 构建 `twisterd`

1. 克隆`github`树以来获取源码并进入目录.
  ```sh
    > git clone https://github.com/miguelfreitas/twister-core.git
    > cd twister-core
  ```
1. 使用`autotool`构建`twister`
  ```sh
    > ./autotool.sh
    > ./configure --enable-logging --with-openssl=/usr/local/opt/openssl --with-libdb=/usr/local/opt/berkeley-db4
    > make
  ```
  (如果你有多个CPU, 使用`make -j N`,`N`是内核数)
1. 如果事情往南走，再试一次，确保清理干净:
  ```sh
    > make clean
  ```

如果一切顺利的话, you should now have a twisterd executable in the twister-core directory.

请参阅下面的运行说明。

## MacPorts

### 安装依赖

使用`MacPorts`非常直接安装依赖.

```sh
  sudo port install boost db48@+no_java openssl miniupnpc libtool
```

安装完依赖, 执行:

```sh
  ./autotool.sh
  ./configure --enable-logging
  make
```

如果安装以后, 需要重试, 确保清空:

```sh
  make clean
```

## 运行

It's now available at `./twisterd`, provided that you are still in the `twister-core` directory. We have to first create the RPC configuration file, though.

运行 `./twisterd` to get the filename where it should be put, or just try these commands:

```sh
  mkdir -p "/Users/${USER}/.twister"
  echo -e "rpcuser=user\nrpcpassword=pwd\nrpcallowip=127.0.0.1" > "/Users/${USER}/.twister/twister.conf"
  chmod 600 "/Users/${USER}/.twister/twister.conf"
```

When next you run it, it will start downloading the blockchain,
but it won't output anything while it's doing this.
可能需要几个小时.
If you see a lonely `connect: Operation timed out`, don't freak out, it seems to work fine.

其它命令:

```sh
  tail -f ~/.twister/debug.log
  ./twisterd --help  # for a list of command-line options.
  ./twisterd -daemon # to start it as a daemon.
  ./twisterd help    # When the daemon is running, to get a list of RPC commands
```

为了获取 HTML 接口, 你需要下载它并链接 .twister:

```sh
  git clone https://github.com/miguelfreitas/twister-html.git /Users/${USER}/Library/Application\ Support/twister/html
```

一旦做完, 可在这里访问 http://localhost:28332/home.html

## 故障诊断

1. You get "DHT network down" in WEB interface on /network.html page
* 重启你的Mac
