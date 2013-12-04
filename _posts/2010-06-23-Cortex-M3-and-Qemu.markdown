---
layout: post
title: Cortex-M3 and Qemu
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Just a small tip to test code generated for ARM Cortex-M3 using QEmu:

<span style="color: #2040a0;">$ arm</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">none</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">eabi</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">gcc</span> <span style="color: #2040a0;">main</span>.<span style="color: #2040a0;">c</span> <span style="color: #4444ff;">-</span><span style="color: #2040a0;">ggdb</span> <span style="color: #4444ff;">-</span><span style="color: #2040a0;">mcpu</span><span style="color: #4444ff;">=</span><span style="color: #2040a0;">cortex</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">m3</span> <span style="color: #4444ff;">-</span><span style="color: #2040a0;">mthumb</span> <span style="color: #4444ff;">-</span><span style="color: #2040a0;">T</span> <span style="color: #2040a0;">generic</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">m</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">hosted</span>.<span style="color: #2040a0;">ld</span>
<span style="color: #2040a0;">$ qemu</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">arm</span> <span style="color: #4444ff;">-</span><span style="color: #2040a0;">cpu</span> <span style="color: #2040a0;">cortex</span><span style="color: #4444ff;">-</span><span style="color: #2040a0;">m3</span> ./<span style="color: #2040a0;">a</span>.<span style="color: #2040a0;">out</span>
<p style="text-align: justify;">You can download Code Sourcery toolchain <a href="http://www.codesourcery.com/sgpp/lite/arm/portal/release1294" target="_blank">here</a> and QEmu <a href="http://wiki.qemu.org/Download" target="_blank">here</a> (alsoavailable from packagemanagement system of your favorite Linux distribution). Just unpack the toolchain associating the arm-201XqX/binwith your $PATH and run qemu.</p>