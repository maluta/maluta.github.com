---
layout: post
title: linux booting on ubifs partitions
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">UBIFS is relatively new on embedded systems but my guess is that they'll <a href="http://free-electrons.com/pub/conferences/2008/elce/flash-filesystems.pdf" target="_blank">become the standard</a> on embedded market. To start, the first step is enable UBIFS support in kernel. I exaggerated on some <em>debug</em> options, fell free to avoid:</p>
<p style="padding-left: 30px;">CONFIG_MTD_UBI=y
CONFIG_MTD_UBI_WL_THRESHOLD=4096
CONFIG_MTD_UBI_BEB_RESERVE=1
CONFIG_MTD_UBI_DEBUG=y
CONFIG_MTD_UBI_DEBUG_MSG=y
CONFIG_UBIFS_FS=y
CONFIG_UBIFS_FS_LZO=y
CONFIG_UBIFS_FS_ZLIB=y</p>
<p style="text-align: justify;">Next I used a simple<em> rootfs</em> - basically <a href="http://www.busybox.net/" target="_blank">busybox</a> + <a href="http://git.infradead.org/mtd-utils.git" target="_blank">mtd-utils</a> - to create/format the partitions, suppose that you kernel <a href="http://www.coding.com.br/embarcado/mtd-partitions-tips/" target="_blank">divided</a> the memory in the following parts:</p>
<p style="padding-left: 30px;"># cat /proc/mtd
mtd0: 00300000 00020000 "bootloader" *
mtd1: 00500000 00020000 "nand.kernel" **
mtd2: 00100000 00020000 "nand.ramdisk"
<strong>mtd3: 06400000 00020000 "nand.system"</strong></p>
*,** The<em> bootloade</em>r and <em>nand.kernel</em> I flashed via u-boot.

1. <strong>The first time
</strong>
<p style="text-align: justify;">This is only needed when you create the partition for the first time. Steps are erasing the flash, detaching the UBI [if it was previously attached], format on UBI model, attach again, creating the volume (specifying a name) and finally mounting.<strong>
</strong></p>

<pre style="padding-left: 30px;">flash_eraseall /dev/mtd3

ubidetach /dev/ubi_ctrl -m 3
ubiformat /dev/mtd3 -y
ubiattach /dev/ubi_ctrl -m 3
ubimkvol /dev/ubi0 -N system -m
mount -t ubifs ubi0:<strong>system</strong> /mnt/ubi

[ copy your rootfs ]

umount /mnt/ubi</pre>
<strong>system</strong> is the name that I choose for partition, could be any.

2. <strong> Editing</strong>

Suppose that you need edit some files on your UBIFS , then you only need:
<pre style="padding-left: 30px;">ubiattach /dev/ubi_ctrl -m 3
mount -t ubifs ubi0:system /mnt/ubi</pre>
3. <strong>Boot</strong>

In order to boot, you need add some parameters to u-boot.
<pre style="padding-left: 30px;">setenv bootargs 'console=ttymxc0,115200 <strong>rootfstype=ubifs ubi.mtd=3 root=ubi0:system</strong> init=...'</pre>