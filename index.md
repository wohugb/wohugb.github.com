---
layout: page
title: 巴别塔
tagline: 大鼻子文档翻译分享
---
{% include JB/setup %}

## 日志列表

<ul class="posts">
  {% for post in site.posts %}
    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ BASE_PATH }}{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>


## 开发者帮助

阅读 [Jekyll快速指南](http://jekyllbootstrap.com/usage/jekyll-quick-start.html)
完整使用文档: [Jekyll Bootstrap](http://jekyllbootstrap.com)

