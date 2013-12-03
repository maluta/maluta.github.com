---
layout: post
title: Using nandsim to mount large images
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Since I'm still using 32-bit machines I had to switch the way I mount large (&gt; 128MiB) JFFS2 images. Now I'm using NAND simulator, an extremely useful debugging and development tool which simulates NAND flashes in RAM. The main problem with mtdram is  related with space reserved to vmalloc function on 32-bits processors (an hardware dependent issue). Checking /proc/meminfo you can see the difference:</p>

<pre>32-bit: VmallocTotal:   122880 kB
64-bit: VmallocTotal:   34359738367 kB</pre>
<p style="text-align: justify;">Nandsim uses another design to access memory, it creates a slab allocation for an array to allow large chunks of memory, the following functions contains more information:</p>

<pre style="text-align: justify;">static int __init <strong>init_mtdram</strong>(void) in drivers/mtd/devices/<strong>mtdram.c</strong>
static int <strong>alloc_device</strong>(struct nandsim *ns) in drivers/mtd/nand/<strong>nandsim.c</strong></pre>
Lets remember the "original" way (using mdtram) to mount an JFFS2 image:
<pre>modprobe mtd
modprobe mtdblock
<strong>modprobe mtdram total_size=10240 erase_size=16</strong>
dd if=image.jffs2 of=/dev/mtdblock0
mount -t jffs2 /dev/mtdblock0 /mount-point</pre>
And the new one with nandsim:
<pre>modprobe mtd
modprobe mtdblock
<strong>modprobe nandsim first_id_byte=0x20 second_id_byte=0x71
</strong>dd if=image.jffs2 of=/dev/mtdblock0
mount -t jffs2 /dev/mtdblock0 /mount-point</pre>
And check both:
<pre>cat /proc/mtd
dev:    size   erasesize  name
mtd0: 08000000 00004000 "NAND simulator partition 0"
mtd1: 00400000 00004000 "mtdram test device"</pre>
<p style="text-align: justify;">With mtdram you can define any value to <em>erase_size</em> but with nandsim you need pre-defined memory parameters found in manufacturer datasheet, to select the simulated flash type one should specify ID bytes of your flasher (I've tested with pages of 512 and 2048 bytes).  For more information click <a href="http://www.linux-mtd.infradead.org/faq/nand.html#L_nand_nandsim" target="_blank">here</a>.</p>
<p style="text-align: justify;">You can use nandsim to mount another flash file systems, such as: YAFFS2, CramFS and UBIFS.</p>
<p style="text-align: justify;">As described on first paragraph, nandsim is much more than just a "mount tool". It can reproduce real condition of memory and lead developers make experiments without real hardware. I'm still learning the possibilities, if you would like to contribute leave an comment.</p>

<strong>Endianess issue</strong>

If you need convert an image from <em>big endian</em> to <em>little endian</em> (specially on x86 systems) use <strong>jffs2dump</strong>.
<pre style="text-align: justify;">jffs2dump -b big_endian.img -e new_little_endian.img</pre>