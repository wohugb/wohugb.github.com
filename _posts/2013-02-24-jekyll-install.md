---
layout: post
category : 手册
title:  Jekyll安装
tagline: 翻译中
tags : [Jekyll,手册]
---
{% include JB/setup %}

## 安装

安装Jekyll最佳方法是通过RubyGems:

    gem install jekyll

Jekyll requires the gems `directory_watcher`, `liquid`, `maruku` and `classifier`. These are automatically installed by the gem install command.

If you encounter errors during gem installation, you may need to install the header files for compiling extension modules for ruby 1.9.1. This can be done on Debian systems by:

    sudo apt-get install ruby1.9.1-dev

or on Red Hat / CentOS / Fedora systems by:

    sudo yum install ruby-devel

On [NearlyFreeSpeech](http://nearlyfreespeech.net/) you need:

    RB_USER_INSTALL=true gem install jekyll

If you encounter errors like `Failed to build gem native extension` on Windows you may need to install [RubyInstaller DevKit](http://wiki.github.com/oneclick/rubyinstaller/development-kit).

On OSX, you may need to update RubyGems:

    sudo gem update --system

You may also need to install Command Line Tools for Xcode if you see errors like `missing headers`. Download from [here](https://developer.apple.com/downloads/index.action).


