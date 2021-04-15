# Ubuntu / Debian building instructions

Tested on a pristine: - Ubuntu 13.10 amd64

## 安装

```sh
> sudo apt-get update
> sudo apt-get install git autoconf libtool build-essential libboost-all-dev libssl-dev libdb++-dev libminiupnpc-dev automake
> git clone https://github.com/miguelfreitas/twister-core.git
> cd twister-core
> ./autotool.sh
> ./configure
> make
```

## 配置 & web gui

```sh
> mkdir ~/.twister
> echo -e "rpcuser=user\nrpcpassword=pwd" > ~/.twister/twister.conf
> chmod 600 ~/.twister/twister.conf
> git clone https://github.com/miguelfreitas/twister-html.git ~/.twister/html
```

## 开始

```sh
> cd twister-core
> ./twisterd -rpcuser=user -rpcpassword=pwd -rpcallowip=127.0.0.1
```

Open http://127.0.0.1:28332/index.html and use the user/pwd credentials

Create your account !
