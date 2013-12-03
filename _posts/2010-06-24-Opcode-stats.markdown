---
layout: post
title: Opcode stats
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">I was trying some GCC options and decided see how they affect assembly code generated. I've created a simple Python script that parses <em>.s</em> output and put in a human readable way. Suppose the classical <em>Hello World </em>program. The output will be something like:</p>
<p style="padding-left: 30px;">$ python stats_opcodes.py file</p>
For Cortex-m3 (check <a href="http://www.coding.com.br/embarcado/cortex-m3-and-qemu/" target="_blank">previous</a> post):
<p style="padding-left: 30px;"><img class="aligncenter size-full wp-image-1136" title="opcode-arm" src="http://www.coding.com.br/wp-content/uploads/2010/06/opcode-arm.png" alt="" width="304" height="194" /></p>
At my laptop (x86):
<p style="padding-left: 30px;"><img class="aligncenter size-full wp-image-1133" title="output" src="http://www.coding.com.br/wp-content/uploads/2010/06/opcodes1.png" alt="" width="306" height="194" /></p>
<span style="font-family: Consolas, Monaco, 'Courier New', Courier, monospace; font-size: small;"><span style="line-height: 18px; white-space: pre;"><span style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; font-size: small;"><span style="line-height: 19px; white-space: normal;"> </span></span></span></span>
<p style="text-align: center;"></p>
Download the script <a href="http://gist.github.com/raw/452170/db097f735c52ffd733d2060603c203982d53b79f/stats_opcode.py" target="_blank">here</a>.