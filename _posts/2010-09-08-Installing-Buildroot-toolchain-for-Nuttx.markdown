---
layout: post
title: Installing Buildroot toolchain for Nuttx
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">On my <a href="http://www.coding.com.br/embarcado/compiler-for-nuttx/" target="_blank">previous</a> post I discussed some stats using Buildroot toolchain to build Nuttx. Today I'll add the necessary steps to build on Ubuntu. Ubuntu is<em> de-facto</em> GNU/Linux distribution (although I'm Gentoo user) and many users, from different areas, uses it [they are not necessary command line experts] so I decided to publish my <em>raw</em> tutorial. If you are familiarized installing files from source-code you probably won't need this...</p>

<h2>1. Dependencies</h2>
<p style="padding-left: 30px;">$ sudo apt-get install libncurses5-dev
$ sudo apt-get install bison
$ sudo apt-get install flex
$ sudo apg-get install libgmp3-dev
$ sudo apg-get install libmpc-dev
$ sudo apg-get install libmpfr-dev
$ sudo apg-get install binutils-dev</p>

<h2>2. Download</h2>
<p style="padding-left: 30px;">$ mkdir Nuttx
$ cd Nuttx</p>
<p style="padding-left: 30px;">$ wget http://sourceforge.net/projects/nuttx/files/nuttx/nuttx-5.10/nuttx-5.10.tar.gz/download
$ wget http://sourceforge.net/projects/nuttx/files/buildroot/buildroot-1.8/buildroot-1.8.tar.gz/download</p>
<p style="padding-left: 30px;">$ ls
buildroot-1.8.tar.gz nuttx-5.10.tar.gz</p>

<h2>3. Install</h2>
<p style="padding-left: 30px;">$ tar zxf buildroot-1.8.tar.gz
$ tar zxf nuttx-5.10.tar.gz</p>
<p style="padding-left: 30px;">$ cd misc/
$ ln -s ../nuttx-5.10 nuttx</p>
You need define some Nuttx files before:
<p style="padding-left: 30px;">$ cd nuttx/
$ cd tools/
$ ./configure.sh nucleus2g/nsh # or ./configure &lt;board-name&gt;
$ cd -</p>
<p style="padding-left: 30px;">$ cd ../misc</p>
I'm building a <em>toolchain</em> for arm cortex-m3 but check configs/ to other configuration files.
<p style="padding-left: 30px;">$ cd buildroot-1.8/
$ cp configs/cortexm3-defconfig-4.3.3 .
$ mv cortexm3-defconfig-4.3.3 .config</p>
<p style="padding-left: 30px;">$ make menuconfig
[If you don't have any changes, just click on 'exit' and save the configuration]</p>
<p style="padding-left: 30px;">$ make
[will download and build all necessary files]</p>
<p style="padding-left: 30px;">$ cd build_arm_nofpu/staging_dir/bin
$ export PATH=`pwd`:$PATH
$ cd -</p>
<p style="padding-left: 30px;">$ cd ../nuttx
[use normally]</p>
I usually create an script to (re)define the $PATH for necessary building tools, something like:
<p style="padding-left: 30px;">$ echo "export PATH=\""$PATH"\"" &gt; compiler.sh</p>
<p style="padding-left: 30px;"></p>
<p style="padding-left: 30px;"></p>
<p style="padding-left: 30px;"></p>