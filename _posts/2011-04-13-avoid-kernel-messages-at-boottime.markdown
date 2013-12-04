---
layout: post
title: avoid kernel messages at boottime
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Linux embedded normally don't behave as the same in desktop system, maybe instead <em>login</em> at your device you need only run a specific application - for example - by just modifying an start script. Although easily... one requisite that I faced these days was avoid boot messages from kernel, accomplished by changing <a href="http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob_plain;f=Documentation/kernel-parameters.txt;h=cc85a927819070bef71e5802204b0f07cfb76973;hb=d77d9597ad8f2bd381a5168005a21e82df6f18eb" target="_blank">kernel parameters</a>:</p>
<p style="padding-left: 30px; text-align: justify;">setenv bootargs '<strong>console=<span style="color: #ff0000;">none</span> </strong>root=/dev/mmcblk0p<span style="color: #ff0000;">X</span> rootwait init=/sbin/init'</p>
But this parameter broke the output of my start code (a shell script) located on /etc/rc.d/...
<p style="text-align: justify;">Checking for solutions I go back to <em>getty</em> and added two parameters "<strong>-l</strong>" and "<strong>-n</strong>" to specify your program (or <em>script</em>) and prompt for <em>nologin</em>.</p>
$ cat /etc/inittab
<p style="padding-left: 30px;">::sysinit:/etc/rc.d/rcS
::respawn:/sbin/getty -L <span style="color: #ff0000;">ttymxc0</span> 115200 vt100 <strong>-l </strong><span style="color: #ff0000;">/path/to/your/program</span><strong> -n </strong>
::ctrlaltdel:/sbin/reboot
::shutdown:/etc/rc.d/rcS stop
::restart:/sbin/init</p>
Now I can see the serial output without kernel boot messages.