---
layout: post
title: Shortening URL
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">There are <a title="List of URL shortening services" href="http://mashable.com/2008/01/08/url-shortening-services/" target="_blank">many</a> URL shortening services. I just picked one (<a href="http://u.nu" target="_blank">u.nu</a>) to use from <em>command line interface </em>and chose something really quick and simple. Here's the code:</p>

<pre><span style="color: #444444;"># -*- coding: utf-8 -*-</span>
<strong>from</strong> <span style="color: #2040a0;">urllib</span> <strong>import</strong> <span style="color: #2040a0;">urlencode</span>
<strong>import</strong> <span style="color: #2040a0;">httplib</span>
<strong>import</strong> <span style="color: #2040a0;">sys</span>

<span style="color: #2040a0;">api_url</span><span style="color: #4444ff;">=</span><span style="color: #008000;">"u.nu"</span>
<span style="color: #2040a0;">var</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">urlencode</span><span style="color: #4444ff;">(</span><span style="color: #4444ff;"><strong>{</strong></span><span style="color: #008000;">'url'</span><span style="color: #4444ff;">:</span><span style="color: #2040a0;">sys</span>.<span style="color: #2040a0;">argv</span><span style="color: #4444ff;">[</span><span style="color: #ff0000;">1</span><span style="color: #4444ff;">]</span><span style="color: #4444ff;"><strong>}</strong></span><span style="color: #4444ff;">)</span>
<span style="color: #2040a0;">args</span> <span style="color: #4444ff;">=</span> <span style="color: #008000;">"/unu-api-simple?%s"</span> <span style="color: #4444ff;">%</span> <span style="color: #4444ff;">(</span><span style="color: #2040a0;">var</span><span style="color: #4444ff;">)</span>
<span style="color: #2040a0;">conn</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">httplib</span>.<span style="color: #2040a0;">HTTPConnection</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">api_url</span><span style="color: #4444ff;">)</span>
<span style="color: #2040a0;">conn</span>.<span style="color: #2040a0;">request</span><span style="color: #4444ff;">(</span><span style="color: #008000;">"GET"</span>,<span style="color: #2040a0;">args</span><span style="color: #4444ff;">)</span>
<span style="color: #2040a0;">ret</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">conn</span>.<span style="color: #2040a0;">getresponse</span><span style="color: #4444ff;">(</span><span style="color: #4444ff;">)</span>
<strong>print</strong> <span style="color: #2040a0;">ret</span>.<span style="color: #2040a0;">read</span><span style="color: #4444ff;">(</span><span style="color: #4444ff;">)</span></pre>
<h5 style="text-align: center;">Download the script <a href="http://gist.github.com/486190" target="_blank">here</a>.</h5>
Just run passing the URL, for example:
<p style="padding-left: 30px;">$ python u.py www.coding.com.br</p>
<p style="padding-left: 30px;">http://u.nu/72mpd</p>
<p style="text-align: justify;">Easy your life by putting the script on your $PATH and execution (+x) file mode. Worth check the API from other services:</p>

<ul>
	<li><a title="Documentation of bit.ly API" href="http://code.google.com/p/bitly-api/wiki/ApiDocumentation" target="_blank">bit.ly</a></li>
	<li><a title="Documentation of migre.me API" href="http://migre.me/api-migreme/" target="_blank">migre.me</a> (brazilian company)</li>
	<li><a title="Documentation of is.gd API" href="http://is.gd/api_info.php" target="_blank">is.gd</a></li>
	<li><a href="http://tiny.cc/api-docs" target="_blank">tiny.cc</a></li>
	<li><a href="http://www.scripting.com/stories/2007/06/27/tinyurlHasAnApi.html" target="_blank">tinyurl</a></li>
</ul>
<p style="padding-left: 30px;"></p>