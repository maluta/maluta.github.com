---
layout: post
title: SHOUTcast search
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">I'm working on a project using <a href="http://yp.shoutcast.com/">SHOUTCast</a>. In order to know about  services requests, especially XML output, I made this small program to display search queries.  The program perform an Http request and parse the result in a appropriate view.</p>
<p style="text-align: center;"><img class="size-medium wp-image-713 aligncenter" title="ShoutCast Search" src="http://www.coding.com.br/wp-content/uploads/2010/03/sc-300x233.png" alt="" width="300" height="233" /><a href="http://farm5.static.flickr.com/4068/4410975721_5faa4f3bf2_o.png" target="_blank">screenshot</a></p>
<p style="text-align: center;">This code is hosted in <a title="Shoutcast search repository " href="http://github.com/maluta/shoutcast-search" target="_blank">Github</a>.</p>

<pre style="text-align: left;">$ git clone git://github.com/maluta/shoutcast-search.git 
$ cd shoutcast-search 
$ qmake &amp;&amp; make &amp;&amp; ./shoutcast-search
</pre>
<p style="text-align: justify;">To listen some radio I <em>cut &amp; paste</em> 'Playlist' info and put in some player. For example, to listen the Bob Dylan radio selected in screenshot I would do:</p>
<pre>
curl -s http://yp.shoutcast.com/sbin/tunein-station.pls?id=486</p>
</pre>
<blockquote>
[playlist]
numberofentries=2
File1=http://68.90.68.227:8001
Title1=(#1 - 11/55) DylanRadio.com
Length1=-1
File2=http://66.55.139.212:7190
Title2=(#2 - 30/50) DylanRadio.com
Length2=-1
Version=2
</blockquote>
As you can see, ouput has two URLs, so I select one and choose mplayer to play.
<pre>
mplayer http://68.90.68.227:8001
</pre>

Enjoy :-)

<strong>Bonus:</strong> A not beautiful way to play from command line... 

<pre lang="bash">
curl -s http://... | egrep "^File1" | cut -c7- | xargs mplayer
</pre>