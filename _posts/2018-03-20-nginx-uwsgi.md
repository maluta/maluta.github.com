---
layout: post
title: nginx uwsgi
desc:
proj-url:
proj-num: 01
proj-img: ../images/cc.png
proj-img-alt: image description
---

I followed the [Setting up Django and your web server with uWSGI and nginx](http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html) tutorial


`uwsgi --ini <INIT FILE> --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log`


What worked differently for me:

   1. Save the socket file in /tmp
   2. Change socket permission to rw (666)
   3. Not using the emperor mode

*Bonus*

- [Pitfalls and Common Mistakes](https://www.nginx.com/resources/wiki/start/topics/tutorials/config_pitfalls/) using nginx
