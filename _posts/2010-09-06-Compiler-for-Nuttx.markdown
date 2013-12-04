---
layout: post
title: Compiler for Nuttx
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">I was following this <a href="http://article.gmane.org/gmane.comp.embedded.nuttx/102" target="_blank">thread</a> on Nuttx maillist on recommended compiler to build <a href="http://nuttx.sf.net">Nuttx RTOS</a>. As a matter of practicality I guess that many users use CodeSourcery <em><a href="http://www.codesourcery.com/public/gnu_toolchain/arm-none-linux-gnueabi/arm-2010q1-202-arm-none-linux-gnueabi.bin" target="_blank">arm-none-linux-gnueabi</a> </em>but today I decided test the code generated for Cortex-M3 (LPC1768) using the <em>toolchain</em> from <a href="http://sourceforge.net/projects/nuttx/files/buildroot/buildroot-1.8/" target="_blank">Buildroot</a>. As Greg Nutt said (text adapted):</p>

<blockquote><em>They were configured using OABI [old arm ABI], but I prefer them because (1) they are not EABI and reliably link code with -O3 or -Os, making it up to half the size, and (2) include nuttx "built in" -- they really should be called arm-nuttx-gcc tools.</em></blockquote>
Here my stats (<a href="http://www.coding.com.br/wp-content/uploads/2010/09/defconfig.txt" target="_blank">defconfig</a>):
<p style="padding-left: 30px;">$ arm-none-eabi-size nutt
text         data   bss       dec        hex      filename
71000     324    2248   73572   11f64   nuttx</p>
<p style="padding-left: 30px;">$ arm-elf-size nuttx
text         data    bss      dec         hex     filename
56172     330    2248   58750    e57e   nuttx</p>
<p style="text-align: justify;">The final .bin has an <em>delta</em> of 16K. As I'm using one <a href="http://en.wikipedia.org/wiki/Wiggler_(JTAG)" target="_blank">parallel</a> JTAG (flash rates @ 0.2 KiB/S) this means almost <strong>1 minute</strong> reduction in each flash <a href="http://openocd.berlios.de/doc/html/Flash-Commands.html#Flash-Commands" target="_blank"><em>write_image</em></a>. If you check <a href="http://nuttx.cvs.sourceforge.net/viewvc/nuttx/nuttx/configs/nucleus2g/nsh/Make.defs?revision=1.2&amp;view=markup" target="_blank">Make.defs</a> note that MAXOPTIMIZATION for CodeSourcery isn't using <em>optimize for size</em> option (-Os). As explained on config/&lt;board&gt;/<a href="http://nuttx.cvs.sourceforge.net/viewvc/nuttx/nuttx/configs/nucleus2g/README.txt?revision=1.6&amp;view=markuphttp://nuttx.cvs.sourceforge.net/viewvc/nuttx/nuttx/configs/nucleus2g/README.txt?revision=1.6&amp;view=markup" target="_blank">README.txt</a> it doesn't work with this kind of optimization level [tested with 2009q1].</p>