---
layout: post
category : 手册
title:  Jekyll使用
tagline: 翻译中
tags : [Jekyll,手册]
---
{% include JB/setup %}

创建一个Jekyll网站通常包含一下内容, [[如果已经安装jekyll.|Install]]

* 设置网站的基础架构
* 创建一些帖子, 或者 [[或者从以前的平台导入|Blog migrations]]
* 在本地运行你的网站看看长什么样
* 发布你的网站

## 基础框架

Jekyll at its core is a text transformation engine. The concept behind the system is this: you give it text written in your favorite markup language, be that Markdown, Textile, or just plain HTML, and it churns that through a layout or series of layout files. Throughout that process you can tweak how you want the site URLs to look, what data gets displayed on the layout and more. This is all done through strictly editing files, and the web interface is the final product.

基础Jekyll网站一般这样的:

<pre>
.
|-- _config.yml
|-- _includes
|-- _layouts
|   |-- default.html
|   `-- post.html
|-- _posts
|   |-- 2007-10-29-why-every-programmer-should-play-nethack.textile
|   `-- 2009-04-26-barcamp-boston-4-roundup.textile
|-- _site
`-- index.html
</pre>

作用概述:

### _config.yml

存储 [[配置|Configuration]] 数据. A majority of these options can be specified from the command line executable but it's easier to throw them in here so you don't have to remember them.

### _includes

These are the partials that can be mixed and matched by your _layouts and _posts to facilitate reuse.  The liquid tag <code>{% include file.ext %}</code> can be used to include the partial in _includes/file.ext.

### _layouts

发帖模板. Layouts are chosen on a post-by-post basis in the [[YAML front matter]], which is described in the next section. The liquid tag <code>{{ content }}</code> is used to inject data onto the page.


### _posts

你的动态内容，可以这么说. The format of these files is important, as named as `YEAR-MONTH-DAY-title.MARKUP`. The [[Permalinks|permalinks]] can be adjusted very flexibly for each post, but the date and markup language are determined solely by the file name.

### _site

这是放置Jekyll转化生成的网站. It's probably a good idea to add this to your `.gitignore` file.

### index.html 和 其他 HTML/Markdown/Textile 文件

Provided that the file has a [[YAML Front Matter]] section, it will be transformed by Jekyll. The same will happen for any `.html`, `.markdown`, `.md`, or `.textile` file in your site's root directory or directories not listed above.

### 其他文件/文件夹

Every other directory and file except for those listed above will be transferred over as expected. For example, you could have a `css` folder, a `favicon.ico`, etc, etc. There's [[plenty of sites|Sites]] already using Jekyll if you're curious as to how they're laid out.

Any files in these directories will be parsed and transformed, according to the same rules mentioned previously for files in the root directory.

### 运行Jekyll

Usually this is done through the `jekyll` executable, which is installed with the gem. In order to get a server up and running with your Jekyll site, run:

`jekyll --server` 

You'll also need the `--auto` option (provided either via command line parameters or the _config.yml) to watch files which change, if you plan to use the jekyll server during ongoing front-end development.

and then browse to http://0.0.0.0:4000. There's plenty of [[configuration options|Configuration]] available to you as well.

On Debian or Ubuntu, you may need to add `/var/lib/gems/1.8/bin/` to your path.

### base-url 选项

If you are using base-url option like 

`jekyll serve --baseurl '/blog'`

then make sure that you access the site at 

`http://localhost:4000/blog/index.html` . 

Just accessing 

`http://localhost:4000/blog`

will not work.

### 部署

Since Jekyll simply generates a folder filled with HTML files, it can be served using practically any available web server out there. Please check the [[Deployment]] page for more information regarding specific scenarios.


### Jekyll博客引用和工作流引导
A Jekyll User's post explaining how you can use jekyll for blogging and why he thinks jekyll is awesome.

[Jekyll Blogging reference and perfect workflow guide](http://qubitlogs.com/Workflow/2013/01/22/jekyll-blogging-reference-and-perfect-workflow-guide/)
