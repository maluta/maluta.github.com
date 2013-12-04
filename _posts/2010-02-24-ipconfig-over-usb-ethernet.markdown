---
layout: post
title: ipconfig over usb ethernet
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: right;"><em>I guess this post apply only if you are using Linux v.2.6.33-rc3 or above.</em></p>
<p style="text-align: justify;">You would have noted that kernel IP auto-configuration is not usable for some USB-Ethenet dongles on newer kernel because it starts before the USB devices are found. This was already discussed on LKML. I proposed a workaround adding a section on menuconfig to user increase delay (<a href="http://lkml.org/lkml/2010/2/9/420" target="_blank">patch</a>) but other developer proposed another <a href="http://marc.info/?l=linux-netdev&amp;m=126311212608318&amp;w=2" target="_blank">patch</a> to configure this delay at runtime rather than at compile time. This patches weren' t applied to mainline (to further information check link). I decided post here because I take some time to configure my NFS rootfs due this delay. My tests were made using BeagleBoard and USB-Ethernet dongle based on ASIX 8877x.</p>