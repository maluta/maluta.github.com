---
layout: post
title: Changes on kernel cross compiling
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Probably if you compile - many times - <a href="http://www.kernel.org">Linux</a> for embedded hardware you change <a href="file:/usr/src/linux/Makefile">Makefile</a> to your specific architecture and compiler. An example:
<pre># Set the ARCH and CROSS_COMPILE default values
ARCH            ?= arm
CROSS_COMPILE   ?= arm-unknown-linux-gnu-</pre>
Latest Linux (~2.6.31) turns it deprecated (commit <a href="http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commit;h=2331d1a6cd3d6e580bc88b9a160066d9e1177fe1">575543347b5baed0ca927cb90ba8807396fe9cc9</a>). Now the settings are saved in two files named:
<p style="padding-left: 30px;">include/generated/kernel.arch
include/generated/kernel.cross

<strong>What changes?</strong>

Using the new way you don't edit Makefile anymore, just need set once your definitions for cross compiling:
<pre>$ make ARCH=arm CROSS_COMPILE=arm-unknown-linux-gnu-</pre>
And for next builds just run <em>make</em>
<pre>$ make</pre>
This works both for plain builds and for O=... builds.