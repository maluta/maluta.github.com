---
layout: post
title: IP representation
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Yesterday I came across with an interesting contruction for IP address. Suppose that you want store the address '192.168.10.33' no matter the dot.</p>
<p style="text-align: center;"><strong>192</strong>&lt;&lt;24|<strong>168</strong>&lt;&lt;16|<strong>10</strong>&lt;&lt;8|<strong>33</strong></p>
That produces
<p style="text-align: center;">3232238113 (0xc0a80a21)</p>
<p style="text-align: justify;">To return is just get the address in hex format and split in 4 sections. Means that: c0 (192) a8  (168) 0a (10) 21 (33). An example using Python generators to return using <em>big endian</em> format (<a href="http://gist.github.com/514917">download</a>).</p> 
<span style="color: #2040a0;">def</span> <span style="color: #2040a0;">octet</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">ip</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">:</span>
<strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for</strong> <span style="color: #2040a0;">i</span> <strong>in</strong> <span style="color: #2040a0;">range</span><span style="color: #4444ff;">(</span><span style="color: #4444ff;">-</span><span style="color: #ff0000;">24</span>,<span style="color: #ff0000;">8</span>,<span style="color: #ff0000;">8</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">:</span>
<span style="color: #2040a0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;yield</span> <span style="color: #2040a0;">ip</span> <span style="color: #4444ff;">&gt;</span><span style="color: #4444ff;">&gt;</span> <span style="color: #4444ff;">-</span><span style="color: #2040a0;">i</span> <span style="color: #4444ff;">&amp;</span> <span style="color: #ff0000;">0xff</span>

And got each value:

<p style="padding-left: 30px;">r = octet(ip)
r.next() # returns 192
r.next() # returns 168
r.next() # returns 10
r.next() # returns 33</p>