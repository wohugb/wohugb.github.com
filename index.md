---
layout: home
title: 巴别塔
tagline: 大鼻子文档翻译分享
---
{% include JB/setup %}


<div class="span4">
<h2>日志列表</h2>
<p>
<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
</p>
</div>
<div class="span4">
<h2>RedTheDocs.org</h2>
<p><ul class="posts">
<li><a href="https://django-docs-zh.readthedocs.org">django-docs-zh</a></li>
<li><a href="https://git-reference.readthedocs.org">Git 中文手册</a></li>
<li><a href="https://mongodb-odm-documentation.readthedocs.org">mongodb-odm-documentation</a></li>
<li><a href="https://python-documentation-cn.readthedocs.org">Python中文文档</a></li>
<li><a href="https://sphinx-doc.readthedocs.org">python-guide-zh</a></li>
<li><a href="https://sphinx-doc.readthedocs.org">sphinx-doc中文文档</a></li>
<li><a href="https://zf2-documentation-zh.readthedocs.org">Zend Framework 2 中文文档</a></li>
</ul></p>
</div>
<div class="span4">
<iframe id="sina_widget_1422986101" style="width:100%; height:500px;" frameborder="0" scrolling="no" src="http://v.t.sina.com.cn/widget/widget_blog.php?uid=1422986101&height=500&skin=wd_01&showpic=1"></iframe>
</div>

