---
layout: post
title: A brief on "designated initializers"
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">The GNU Compiler Collection (GCC) for C language doesn't initialize variables <em>zeroed.</em> For simple variables types like <em>int</em> or <em>float</em> is just equal to 0 or 0.0 respectively. Now, suppose that you have a "large" <em>struct</em> and doesn't want to set each member  individually... you could just type "={0}" which means that the first member is explicitly initialized to zero and  the remaining members are implicitly initialized, also zero. Let's see an example:</p>
<strong>typedef</strong> <strong>struct</strong>
<span style="color: #4444ff;"><strong>{</strong></span>
<strong> int</strong> <span style="color: #2040a0;">a</span><span style="color: #4444ff;">;</span>
<strong> char</strong> <span style="color: #2040a0;">c</span><span style="color: #4444ff;">;</span>
<strong> char</strong> <span style="color: #2040a0;">s</span><span style="color: #4444ff;">[</span><span style="color: #ff0000;">10</span><span style="color: #4444ff;">]</span><span style="color: #4444ff;">;</span>
<strong> int</strong> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">ptr</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span> <span style="color: #2040a0;">data</span><span style="color: #4444ff;">;</span>

When you initialize with:

<span style="color: #2040a0;">data</span> <span style="color: #2040a0;">d</span><span style="color: #4444ff;"><strong></strong></span><span style="color: #4444ff;"><strong></strong></span><span style="color: #4444ff;">;</span>

You got some random value like:

{a = -1208298748, c = -12 '\364', s = "\317\372\267\230\353\377\277\351\203\004", ptr = 0xb7e94cc5}

When you type:

<span style="color: #2040a0;">data</span> <span style="color: #2040a0;">d</span> <span style="color: #4444ff;">=</span> <span style="color: #4444ff;"><strong>{</strong></span><span style="color: #ff0000;">0</span><span style="color: #4444ff;"><strong>}</strong></span><span style="color: #4444ff;">;</span>

You'll have each struct member initialized to <em>zero</em>.

{a = 0, c = 0 '\000', s = "\000\000\000\000\000\000\000\000\000", ptr = 0x0}

You can learn much more about <a href="http://gcc.gnu.org/onlinedocs/gcc/Designated-Inits.html" target="_blank">designated inits</a> [section 6.26] on GCC docs.