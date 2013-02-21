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
<p>
[django-docs-zh](https://django-docs-zh.readthedocs.org)

[Git 中文手册](https://git-reference.readthedocs.org)

[mongodb-odm-documentation](https://mongodb-odm-documentation.readthedocs.org)

[Python中文文档](https://python-documentation-cn.readthedocs.org)

[python-guide-zh](https://sphinx-doc.readthedocs.org)

[sphinx-doc中文文档](https://sphinx-doc.readthedocs.org)

[Zend Framework 2 中文文档](https://zf2-documentation-zh.readthedocs.org)
</p>
</div>
<div class="span4">
<h2>开发者帮助</h2>
<p>
阅读 [Jekyll快速指南](http://jekyllbootstrap.com/usage/jekyll-quick-start.html)

完整使用文档: [Jekyll Bootstrap](http://jekyllbootstrap.com)
</p>
</div>

