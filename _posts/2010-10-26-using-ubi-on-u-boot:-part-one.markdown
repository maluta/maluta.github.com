---
layout: post
title: using ubi on u-boot: part one
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">UBI stands for <em>Unsorted Block Images</em>. The <a href="http://kernelnewbies.org/Linux_2_6_22#head-1c99f2ac9780815fe6dad0420fbe2869a7a687a5" target="_blank">shortest</a> description for UBI is "LVM for NAND flash memory devices" and if you don't know yet how it's works I recommend check this <a href="http://www.linux-mtd.infradead.org/doc/ubi.ppt " target="_blank">presentation</a>. I intend here describe my use with u-boot, starting with the steps to flash an kernel image. First of all, if you not defined MTDPARTS_DEFAULT on you u-boot config file, you must define (or redefine) on u-boot terminal.</p>

<pre style="text-align: left;">&gt; setenv mtdparts mtdparts=nand0:0x80000@0x0(uboot),0x400000@0x80000(kernel),-@0x480000(root)</pre>
If you type <strong>mtd</strong><strong> </strong> you I'll see:
<pre>device nand0 &lt;nand0&gt;, # parts = 3
 #: name        size        offset        mask_flags
 0: uboot     0x00080000    0x00000000    0
 1: kernel    0x00400000    0x00080000    0
 2: root      0x1fb80000    0x00480000    0</pre>
<p style="text-align: left;">UBI deal with volume and not partitions. Let's create one.</p>

<pre style="text-align: left;">&gt; ubi part kernel</pre>
If you got some <a href="https://acassis.wordpress.com/2009/10/29/creating-an-error-number-table/" target="_blank">-22</a> error, like:
<p style="padding-left: 30px;"><em>UBI error: ubi_read_volume_table: the layout volume was not found
UBI error: ubi_init: cannot attach mtd1
UBI error: ubi_init: UBI error: cannot initialize UBI, error -22
UBI init error -22</em></p>
you need <a href="http://lkml.org/lkml/2007/3/23/199" target="_blank">erase</a> the NAND region [ <strong>nand erase 0x00080000 0x400000 </strong>] and <em>ubi part</em> command again<strong>. </strong>

Next step is create the volume:
<pre>&gt; ubi create kernel_vol
Creating dynamic volume kernel_vol of size <strong>3354624</strong></pre>
<p style="text-align: justify;">The value in bold is the max size of that volume in bytes (~3MB). Note that is less than the 4MB (0x400000) defined in mtdparts. This happens because UBI works with logical blocks instead (LEB) of physical ones (PEB).</p>
<p style="text-align: justify;">In order to write the kernel you need transfer the image to u-boot. Since Ethernet  isn't working in my board I choose between <a href="http://www.coding.com.br/embarcado/accessing-u-boot-with-picocom-to-transfer-files-via-serial-interface/" target="_blank">serial</a> or mmc.  As serial is too slow to large files I opted to write the image on FAT partition on SD card and load through:</p>

<pre>&gt; mmcinfo
&gt; fatload mmc 0 ${loadaddr} uImage</pre>
The output will be something like
<p style="padding-left: 30px;"><em>reading uImage
2845120 bytes read</em></p>
Finally write it:
<pre>&gt; ubi write ${loadaddr} kernel_vol 0x2b69c0</pre>
You can check if everything went fine comparing
<pre>&gt; ubi read 0x90AC0000 kernel_vol
&gt; cmp.b ${loadaddr} 0x90ac0000  0x2b69c0
Total of 2845120 bytes were the same</pre>
0x90AC0000 is some place on RAM different from ${loadaddr} (check using echo ${loadaddr}).