---
layout: post
title: Arduino Gentoo Install
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">If you are reading this post it's probably that you already <a href="http://www.arduino.cc/playground/Linux/Gentoo" target="_blank">checked</a> other resources and had some problem to build  <em>avr-g++ </em>using <a href="http://en.gentoo-wiki.com/wiki/Crossdev" target="_blank">crossdev</a> utility.</p>

<pre>crossdev -t avr -s4</pre>
Note that <em>cpp </em>compiler wasn't created.
<pre id="comment_text_2"># qlist cross-avr/gcc | grep bin
/usr/i686-pc-linux-gnu/avr/gcc-bin/4.4.1/avr-gccbug
/usr/i686-pc-linux-gnu/avr/gcc-bin/4.4.1/avr-gcov
/usr/i686-pc-linux-gnu/avr/gcc-bin/4.4.1/avr-cpp
/usr/i686-pc-linux-gnu/avr/gcc-bin/4.4.1/avr-gcc
/usr/i686-pc-linux-gnu/avr/gcc-bin/4.4.1/avr-gcc-4.4.1</pre>
<p style="text-align: justify;">The problem is easy to fix. Simple edit<strong> </strong><em>/etc/portage/package.use/cross-avr</em> changing '<strong>nocxx</strong>' to '<strong>-nocxx</strong>' and run emerge again.</p>

<pre id="comment_text_3">emerge cross-avr/gcc cross-avr/avr-libc dev-embedded/avrdude</pre>
I'm using AVR toolchain with Arduino <a title="Download" href="http://arduino.cc/en/Main/Software" target="_blank">0017</a> flashing by USB.