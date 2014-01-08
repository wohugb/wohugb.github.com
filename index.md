---
layout: home
title: 巴别塔
tagline: 大鼻子文档翻译分享
group: navigation
---
{% include JB/setup %}


<div class="span4">
<h2>如何搭建这个站点</h2>
<p>
<ol>
<li>注册账号yourname，创建一个yourname.github.com的Repo.</li>
<li>
<ul>
	<li>$ git clone https://github.com/plusjade/jekyll-bootstrap.git yourname.github.com</li>
	<li>$ cd yourname.github.com</li>
	<li>$ git remote set-url origin git@github.com:yourname/yourname.github.com.git</li>
	<li>$ git push origin master</li>
</ul>
</li>
<li>修改_config.yml内容为你的信息.</li>
<li>修改模板和每页的内容.</li>
<li>可以用Egit或者SmartGit/Hg提交发布文件.</li>
<li>git clone git://github.com/twitter/bootstrap.git 下载最新的bootstrap文件.</li>
</ol>
</p>
</div>
<div class="span4">
<h2>日志列表</h2>
<p>
<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
</p>
<h2>RedTheDocs.org</h2>
<p><ul class="posts">
<li><a href="https://django-docs-zh.readthedocs.org">django-docs-zh</a></li>
<li><a href="https://git-reference.readthedocs.org">Git 中文手册</a></li>
<li><a href="https://mongodb-odm-documentation.readthedocs.org">mongodb-odm-documentation</a></li>
<li><a href="https://python-documentation-cn.readthedocs.org">Python中文文档</a></li>
<li><a href="https://sphinx-doc.readthedocs.org">python-guide-zh</a></li>
<li><a href="https://sphinx-doc.readthedocs.org">sphinx-doc中文文档</a></li>
<li><a href="https://zf2-documentation-zh.readthedocs.org">Zend Framework 2 中文文档</a></li>
<li><a href="https://readthedocs.readthedocs.org">Read The Docs 中文文档</a></li>
</ul></p>
</div>
<div class="span4">
<iframe width="100%" height="550" class="share_self"  frameborder="0" scrolling="no" src="http://widget.weibo.com/weiboshow/index.php?language=&width=0&height=550&fansRow=2&ptype=1&speed=0&skin=2&isTitle=1&noborder=1&isWeibo=1&isFans=1&uid=1422986101&verifier=99541cab&dpc=1"></iframe>
</div>

