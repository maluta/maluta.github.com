---
layout: post
title: spliting files with dd
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">It's just in case that you don't <span style="text-decoration: line-through;">have</span>* want use <a href="http://unixhelp.ed.ac.uk/CGI/man-cgi?split" target="_blank">split</a>... (that is much easy). Suppose that you have a 20MB ogv movie and you want split in four parts of 5MB. You can just do:</p>

<pre>dd if=MOVIE.ogv of=pt1 bs=1M count=5
dd if=MOVIE.ogv of=pt2 bs=1M skip=5 count=5
dd if=MOVIE.ogv of=pt3 bs=1M skip=10 count=5
dd if=MOVIE.ogv of=pt4 bs=1M skip=15</pre>
To merge again...
<pre>cp pt1 final.ogv # you can ommit this temporary file by using pt1 as final file
dd if=pt2 of=final.ogv bs=1M seek=5 count=5
dd if=pt3 of=final.ogv bs=1M seek=10 count=5
dd if=pt4 of=final.ogv bs=1M seek=15
</pre>
After you can verify the integrity by using some hash generator, <em>md5sum</em> or <em>sha1sum</em> are examples.
<p style="padding-left: 30px;">$ md5sum final.ogv MOVIE.ogv
71ac8962779dcb733599dba1ce54d783 final.ogv
71ac8962779dcb733599dba1ce54d783 MOVIE.ogv</p>
* this will never happen since both <em>dd</em> and <em>split</em> are on <a href="http://www.gnu.org/software/coreutils/" target="_blank">coreutils</a> package.

<strong>Code</strong>

I wrote a simple proof-of-concept to demonstrate, just:
<p style="text-align: center;"><code>$ git clone <a href="http://gist.github.com/630395" target="_blank">git://gist.github.com/630395.git</a> split-sh
</code></p>