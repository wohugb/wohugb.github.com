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


