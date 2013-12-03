---
layout: post
title: BeagleBoard and Ubuntu 11.04 (beta 1) headless install
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Ubuntu <a href="https://wiki.ubuntu.com/ARM/OMAP" target="_blank">OMAP</a> team is doing a really good job by adding a <em><a href="https://wiki.ubuntu.com/ARM/OMAPHeadlessInstall" target="_blank">headless installation</a></em> of 11.04 <a href="http://cdimage.ubuntu.com/ubuntu-headless/releases/11.04/beta-1/" target="_blank">release</a>. I had a good impression trying on BeagleBoard (revC) and the process is straightforward (read the documentation)<em> but</em> I needed made a slight change at u-boot <em>bootcmd</em> env, so I decided share:</p>
<p style="padding-left: 30px;">mmc init
<strong>mmc rescan 0</strong>
fatload mmc 0 0x82000000 boot.scr
source 0x82000000</p>
After install... I put a usb/ethernet dongle and got fully supported by APT syncing from <a href="http://ports.ubuntu.com" target="_blank">ports.ubuntu.com</a> :-)
<p style="text-align: center;"><img class="aligncenter" title="BeagleBoard + USB/Ethernet dongle" src="http://farm5.static.flickr.com/4105/5612224154_5f56dcd14c.jpg" alt="My Beagle setup" width="500" height="375" /></p>
<p style="text-align: left;">I suggest try it.</p>