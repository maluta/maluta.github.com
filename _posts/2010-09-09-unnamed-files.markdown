---
layout: post
title: unnamed files
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<div>
<p style="text-align: justify;">I'm a heavy user of <em>command line interface </em>and often named files without extension. This behavior forces me to use <strong>file </strong>utility every time I have doubts.</p>

<div id="_mcePaste" style="padding-left: 30px; text-align: justify;">$ file stick-note1</div>
<div id="_mcePaste" style="padding-left: 30px;">stick-note1: ASCII text</div>
<p style="text-align: justify;">When organizing my <em>home/</em> I came across with many files like that, so I decided make this script to walk throughout files and check if it's text file without extension and put .txt after.</p>
<p style="text-align: center;"><a href="http://gist.github.com/raw/572801/382091bf34aa449d8fc0e21a36d48a4a61b084ff/name.py" target="_blank">download script</a></p>
$ python names.py
This only change the file on current directory and it's a "works for me" approach. Adapt to your needs.

</div>