---
layout: post
title: Problems updating intltool on Gentoo
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



If you are experiencing some problems on updating dev-util/intltool on Gentoo, this is the message that is shown:

<blockquote>checking for perl... /usr/bin/perl
checking for perl &gt;= 5.8.1... 5.10.1
checking for XML::Parser... configure: error: XML::Parser perl module is required for intltool</blockquote>

In other emerges if its failing on some perl module check during ./configure, its maybe because dev-lang/perl was updated an its modules weren't compiled against the new one, on my case I just runned the command:

<pre lang="bash">perl-cleaner --all</pre>

It will rebuild all your modules against your new perl, then you can re-emerge dev-util/intltool.