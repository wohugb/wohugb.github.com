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

## LaTeX 转 PNG

Maruku comes with optional support for LaTeX to PNG rendering via blahtex (Version 0.6) which must be in your `$PATH` along with `dvips`.

(NOTE: [remi’s fork of Maruku](http://github.com/remi/maruku/tree/master) does not assume a fixed location for `dvips` if you need that fixed)

## RDiscount

If you prefer to use [RDiscount](http://github.com/rtomayko/rdiscount/tree/master) instead of [Maruku](http://maruku.rubyforge.org/) for markdown, just make sure it’s installed:

    sudo gem install rdiscount

And run Jekyll with the following option:

    jekyll --rdiscount

Or, in your `_config.yml` file put the following so you don’t have to specify the flag:

    markdown: rdiscount

## Pygments 安装

If you want syntax highlighting via the `{% highlight %}` tag in your posts, you’ll need to install [Pygments](http://pygments.org/) and then follow the Pygments Usage notes in the section below.

### On OS X Leopard, Snow Leopard:

It already comes preinstalled with Python 2.6

    sudo easy_install Pygments

Alternatively on OS X with MacPorts:

    sudo port install python25 py25-pygments

Alternatively on OS X with Homebrew:

    brew install python
    # export PATH="/usr/local/share/python:${PATH}"
    easy_install pip
    pip install --upgrade distribute
    pip install pygments

**Note**: Homebrew doesn’t symlink the executables for you. For the Homebrew default Cellar location and Python 2.7, be sure to add `/usr/local/share/python` to your `PATH`.  For, more information, check out [this](https://github.com/mxcl/homebrew/wiki/Homebrew-and-Python).

### 在Archlinux上:

    sudo pacman -S python-pygments

Or to use python2 for pygments:

    sudo pacman -S python2-pygments

**Note**: python2 pygments version creates a `pygmentize2` executable, while jekyll tries to find `pygmentize`.  Either create a symlink `# ln -s /usr/bin/pygmentize2 /usr/bin/pygmentize` or use the python3 version. (This advice seems to be outdated — python2-pygments does install pygmentize).

### 在Ubuntu和Debian上:

    sudo apt-get install python-pygments

### 在Fedora和CentOS上:

    sudo yum install python-pygments

### 在Gentoo上:

    sudo emerge -av dev-python/pygments

## Pygments 使用

Pygments is designed to use an external CSS file to define the highlighting colors and styles. After you have installed Pygments, you must generate this CSS file. This is done with:

    pygmentize -S default -f html > pygments.css

The command will create a new style sheet named 'pygments.css' in your current directory. Move that stylesheet into your site's CSS directory and include a `<link rel="stylesheet" href="/path/to/pygments.css">` reference to it in your HTML layouts. Or, copy the contents into an existing CSS file that is already being called from your layouts. 

Once the CSS is in place, the syntax for adding actual code highlighting blocks to your source documents is:

