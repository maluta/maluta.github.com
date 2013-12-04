---
layout: post
title: libusb-1.0 with STLinux (sh4 platform)
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;"><a title="STLinux " href="http://www.stlinux.com/drupal/" target="_blank">STLinux</a> Distribution comes with <a title="libusb web-site" href="http://www.libusb.org/" target="_blank">libusb</a>-0.1 to access USB interface in user-space, it works but the new version implements new features (i.e asynchronous interface). Note that libusb-1.0 is not backwards compatible with libusb-0.1 although you can have both libusb versions present on the same system without conflict.</p>
<p style="text-align: justify;">Select one mirror <a title="Download libusb-1.0.2" href="http://ufpr.dl.sourceforge.net/project/libusb/libusb-1.0/libusb-1.0.2/libusb-1.0.2.tar.bz2" target="_blank">near</a> to you and set your cross compiler to produce an object SH4-compatible. I'm using some <a href="http://www.coding.com.br/wiki/BuildingGuidelines">building guidelines</a> to organize my files.</p>

<pre>  CC=sh4-linux-gcc ./configure --host=sh4-linux --prefix=$(cd ../install &amp;&amp; pwd)
  make
  make install</pre>
<p style="text-align: justify;">I prefer use a different folder to especific libs so I've copied the contents of install/ to target rootfs directory</p>

<ul>
	<li>Headers (libusb.h and libusbi.h) in /usr/local/include</li>
	<li>Shared libs (libusb-1.0.so.0.0.0) in /usr/local/lib/</li>
</ul>
And made a symbolic link to system lib folder.
<pre>  ln -s /usr/local/lib/libusb-1.0.so.0.0.0 /usr/lib/libusb-1.0.so.0</pre>
<p style="text-align: justify;">Finally, check some code using new library. My test code was lsusb.c from examples/ in libusb-1.0.2 directory.</p>

<pre>  sh4-linux-gcc lsusb.c -o lsusb -lusb-1.0</pre>