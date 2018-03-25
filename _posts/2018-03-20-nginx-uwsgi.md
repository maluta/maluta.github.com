---
layout: post
title: nginx uwsgi
desc: 
proj-url:
proj-num: 01
proj-img: ../images/cc.png
proj-img-alt: image description
---

From uwsgi-docs.readthedocs.io/en/latest/tutorials/[Django_and_nginx.html](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)

What worked for me:

   1. Save the socket file in /tmp
   2. Change the mod (666)

*Important*

- https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/
