---
layout: post
title: mtd partitions tips
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



there are two<em> tips </em>when initializing MTD partition struct:
<ul>
	<li>use <a href="http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=include/linux/mtd/partitions.h;h=2b54316591d2b4231070a08dec7b6ad33a061ad3;hb=ff8b16d7e15a8ba2a6086645614a483e048e3fbf" target="_blank">MTDPART_OFS_APPEND </a> to define <em>.offset</em></li>
	<li>1024 multiple to <em>.size</em> (4MB = 4194304 bytes or 4 * 1024 * 1024)</li>
</ul>
<strong>static</strong> <strong>struct</strong> <span style="color: #2040a0;">mtd_partition</span> <span style="color: #2040a0;">nand_flash_partitions</span><span style="color: #4444ff;">[</span><span style="color: #4444ff;">]</span> <span style="color: #4444ff;">=</span> <span style="color: #4444ff;"><strong>{</strong></span>
<span style="color: #4444ff;"><strong>{</strong></span>
.<span style="color: #2040a0;">name</span> <span style="color: #4444ff;">=</span> <span style="color: #008000;">"bootloader"</span>,
.<span style="color: #2040a0;">offset</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">0</span>,
.<span style="color: #2040a0;">size</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">3</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span><span style="color: #4444ff;"><strong>}</strong></span>,
<span style="color: #4444ff;"><strong>{</strong></span>
.<span style="color: #2040a0;">name</span> <span style="color: #4444ff;">=</span> <span style="color: #008000;">"nand.kernel"</span>,
.<span style="color: #2040a0;">offset</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">MTDPART_OFS_APPEND</span>,
.<span style="color: #2040a0;">size</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">5</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span><span style="color: #4444ff;"><strong>}</strong></span>,
<span style="color: #4444ff;"><strong>{</strong></span>
.<span style="color: #2040a0;">name</span> <span style="color: #4444ff;">=</span> <span style="color: #008000;">"nand.rootfs"</span>,
.<span style="color: #2040a0;">offset</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">MTDPART_OFS_APPEND</span>,
.<span style="color: #2040a0;">size</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">256</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span><span style="color: #4444ff;"><strong>}</strong></span>,
<span style="color: #4444ff;"><strong>{</strong></span>
.<span style="color: #2040a0;">name</span> <span style="color: #4444ff;">=</span> <span style="color: #008000;">"nand.userfs1"</span>,
.<span style="color: #2040a0;">offset</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">MTDPART_OFS_APPEND</span>,
.<span style="color: #2040a0;">size</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">256</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span> <span style="color: #4444ff;">*</span> <span style="color: #ff0000;">1024</span><span style="color: #4444ff;"><strong>}</strong></span>,
<span style="color: #4444ff;"><strong>{</strong></span>
.<span style="color: #2040a0;">name</span> <span style="color: #4444ff;">=</span> <span style="color: #008000;">"nand.userfs2"</span>,
.<span style="color: #2040a0;">offset</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">MTDPART_OFS_APPEND</span>,
.<span style="color: #2040a0;">size</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">MTDPART_SIZ_FULL</span><span style="color: #4444ff;"><strong>}</strong></span>,
<span style="color: #4444ff;"><strong>}</strong></span><span style="color: #4444ff;">;</span>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 122px; width: 1px; height: 1px; overflow: hidden;">&lt;strong&gt;static&lt;/strong&gt; &lt;strong&gt;struct&lt;/strong&gt; &lt;span style="color: #2040a0;"&gt;mtd_partition&lt;/span&gt; &lt;span style="color: #2040a0;"&gt;nand_flash_partitions&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;[&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;]&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;&lt;strong&gt;{&lt;/strong&gt;&lt;/span&gt;
&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;{&lt;/strong&gt;&lt;/span&gt;
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;&amp;amp;nbname&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #008000;"&gt;"bootloader"&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;offset&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;0&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;size&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;3&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;}&lt;/strong&gt;&lt;/span&gt;,
&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;{&lt;/strong&gt;&lt;/span&gt;
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;name&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #008000;"&gt;"nand.kernel"&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;offset&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #2040a0;"&gt;MTDPART_OFS_APPEND&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;size&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;5&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;}&lt;/strong&gt;&lt;/span&gt;,
&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;{&lt;/strong&gt;&lt;/span&gt;
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;name&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #008000;"&gt;"nand.rootfs"&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;offset&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #2040a0;"&gt;MTDPART_OFS_APPEND&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;size&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;256&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;}&lt;/strong&gt;&lt;/span&gt;,
&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;{&lt;/strong&gt;&lt;/span&gt;
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;name&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #008000;"&gt;"nand.userfs1"&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;offset&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #2040a0;"&gt;MTDPART_OFS_APPEND&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;size&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;256&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;*&lt;/span&gt; &lt;span style="color: #ff0000;"&gt;1024&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;}&lt;/strong&gt;&lt;/span&gt;,
&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;{&lt;/strong&gt;&lt;/span&gt;
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;name&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #008000;"&gt;"nand.userfs2"&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;offset&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #2040a0;"&gt;MTDPART_OFS_APPEND&lt;/span&gt;,
&amp;nbsp;&amp;nbsp;&amp;nbsp;&amp;nbsp;.&lt;span style="color: #2040a0;"&gt;size&lt;/span&gt; &lt;span style="color: #4444ff;"&gt;=&lt;/span&gt; &lt;span style="color: #2040a0;"&gt;MTDPART_SIZ_FULL&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;}&lt;/strong&gt;&lt;/span&gt;,
&lt;span style="color: #4444ff;"&gt;&lt;strong&gt;}&lt;/strong&gt;&lt;/span&gt;&lt;span style="color: #4444ff;"&gt;;&lt;/span&gt;</div>