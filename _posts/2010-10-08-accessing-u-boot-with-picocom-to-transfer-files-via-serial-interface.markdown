---
layout: post
title: accessing u-boot with picocom to transfer files via serial interface
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">There is a how-to with <a href="https://acassis.wordpress.com/2009/10/23/transfering-file-to-u-boot-over-serial/">minicom</a> too, this is using picocom to transfer files via serial interface (ymodem). First start with some parameters, in this case I'm using ttyUSB0.</p>

<pre style="padding-left: 30px;">$ picocom --baud 115200 --send-cmd="sb -vv" --receive-cmd="rb -vvv" /dev/ttyUSB0</pre>
Then:
<pre style="padding-left: 30px;">U-Boot &gt; <strong>loady</strong>
## Ready for binary (ymodem) download to 0x90800000 at 115200 bps...</pre>
Type <strong>C-a C-s</strong> and choose the file.
<pre style="padding-left: 30px;">*** file: /tftpboot/uImage
sb -vv /tftpboot/uImage
Sending: uImage
Ymodem sectors/kbytes sent:   0/ 0kRetry 0: NAK on sector
Retry 0: NAK on sector
Bytes Sent:2203904   BPS:7800
Sending:Transfer complete*** exit status: 0
0(STX)/0(CAN) packets, 6 retries
## Total Size      = 0x0021a0e4 = 2203876 Bytes
U-Boot &gt;</pre>
* The sb and rb utility are on lrzsz package [ $sudo apt-get install lrzsz ]

** Other <a href="http://casper.berkeley.edu/wiki/Setting_Up_BORPH_on_ROACH" target="_blank">reference </a>