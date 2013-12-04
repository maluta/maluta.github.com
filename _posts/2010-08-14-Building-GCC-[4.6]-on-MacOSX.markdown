---
layout: post
title: Building GCC [4.6] on MacOSX
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">The objective here is describe a didactic way to build GNU GCC on MacOSX.  In order to compile GCC you need three libraries: GMP, MPFR and MPC. To organize I usually create folders for each purpose. In this case, three, respectively: <em>source</em>, <em>build</em> and <em>install</em>. [It's not a rule].  My original enviroment is MacOSX 10.6.4 and gcc version 4.2.1 (Apple Inc. build 5659). All files will be on GCC folder, the description below shows:</p>
<p style="padding-left: 30px;">$ mkdir ~/Projects/GCC # <em>compiler + libs</em>
$ mkdir ~/Projects/GCC/libs # <em>gmp, mpfr and mp</em>c
$ mkdir ~/Projects/GCC/libs/files <em># downloaded files</em>
$ mkdir ~/Projects/GCC/libs/install <em># store libs objects and include</em></p>
<strong>Step #1 - Download</strong>
<p style="padding-left: 30px;">$ cd ~/Projects/GCC/libs/files
$ wget ftp://ftp.gmplib.org/pub/gmp-5.0.1/gmp-5.0.1.tar.bz2
$ wget http://www.mpfr.org/mpfr-current/mpfr-3.0.0.tar.bz2
$ wget http://www.multiprecision.org/mpc/download/mpc-0.8.2.tar.gz</p>
<strong>Step #2 - Unpack </strong>
<p style="padding-left: 30px;">$ cd ~/Projects/GCC/libs/
$ tar jxvf files/gmp-5.0.1.tar.bz2
$ tar jxvf files/mpfr-3.0.0.tar.bz2
$ tar zxvf files/mpc-0.8.2.tar.gz</p>
<strong>Step #3 - Build: GMP</strong>
<p style="padding-left: 30px;">$ cd ~/Projects/GCC/libs/</p>
<p style="padding-left: 30px;">$ mkdir gmp-build
$ cd gmp-build
$ ../gmp-5.0.1/configure --prefix=$(cd ../install &amp;&amp; pwd)
$ make install</p>
<em>Note 1: I'm using with ABI=64</em>
<em>Note 2 : Maybe you'll get some unresolved symbols to GMP and MPFR on linking time, never mind. </em>

<em></em><strong>Step #4 - Build: MPFR</strong>
<p style="padding-left: 30px;">$ cd ~/Projects/GCC/libs/</p>
<p style="padding-left: 30px;">$ mkdir mpfr-build
$ cd mpfr-build
$ ../mpfr-3.0.0/configure --prefix=$(cd ../install &amp;&amp; pwd) --with-gmp=~/Projects/GCC/libs/install
$ make install</p>
<em>Note: Before prefix and with-xxx there are two hyphen (not one as showed). It's an Wordpress issue, I don't know how to avoid concatenation. </em>

<strong>Step #5 - Build: MPC</strong>
<p style="padding-left: 30px;">$ cd ~/Projects/GCC/libs/</p>
<p style="padding-left: 30px;">$ mkdir mpc-build
$ cd mpc-build
$ ../mpc-0.8.2/configure --prefix=$(cd ../install &amp;&amp; pwd) --with-gmp=~/Projects/GCC/libs/install --with-mprf=~/Projects/GCC/libs/install
$ make install</p>
<p style="padding-left: 30px;">Problems? If something goes wrong...</p>
<p style="padding-left: 30px;"><em>../../mpc-0.8.2/src/mpc.h:25:17: error: gmp.h: No such file or directory
../../mpc-0.8.2/src/mpc.h:26:18: error: mpfr.h: No such file or directory</em></p>
<p style="padding-left: 30px;">I fixed by adding symbolic links:</p>
<p style="padding-left: 30px;">$ cd  ~/Projects/GCC/libs/mpc-0.8.2/src/
$ ln -s ../../install/include/mpf2mpfr.h .
$ ln -s ../../install/include/mpfr.h .
$ ln -s ../../install/include/gmp.h .</p>
<strong>Step #6 - Download &amp; Build GCC (~4.6)</strong>
<p style="text-align: justify;">I used GCC from git (fda0037801fb258a2191aba59e1e9f0df019e3b6) and I don't know if it will work on newer versions. You'll have to try. Sorry. [Howto: <a href="http://gcc.gnu.org/wiki/GitMirror" target="_blank">GitMirror</a>]. Use <em>git checkout </em>to specify one commit.</p>
<p style="padding-left: 30px;">$ cd ~/Projects/GCC/</p>
<p style="padding-left: 30px;">$ git clone git://gcc.gnu.org/git/gcc.git</p>
<p style="padding-left: 30px;">$ mkdir build
$ mkdir install</p>
<p style="padding-left: 30px;">$ cd build
$ ../gcc/configure --prefix=$(cd ../install/ &amp;&amp; pwd) --with-gmp=/Users/maluta/Projects/GCC/libs/install --with-mpfr=/Users/maluta/Projects/GCC/libs/install --with-mpc=/Users/maluta/Projects/GCC/libs/install --disable-checking  --enable-werror --enable-languages=c</p>
<p style="padding-left: 30px;">$ make
$ make install</p>
<strong>Step #7 - Test</strong>

The binary files will be placed in ~/Projects/GCC/install/bin
<p style="padding-left: 30px;">$  ~/Projects/GCC/install/bin
$  ./gcc -v</p>
<p style="padding-left: 30px;">Using built-in specs.
COLLECT_GCC=./gcc
COLLECT_LTO_WRAPPER=/Users/maluta/Projects/GCC/install/libexec/gcc/x86_64-apple-darwin10.4.0/4.6.0/lto-wrapper
Target: x86_64-apple-darwin10.4.0
Configured with: ../gcc/configure --prefix=/Users/maluta/Projects/GCC/install --with-gmp=/Users/maluta/Projects/GCC/libs/install --with-mpfr=/Users/maluta/Projects/GCC/libs/install --with-mpc=/Users/maluta/Projects/GCC/libs/install --disable-checking --enable-werror --enable-languages=c
Thread model: posix
gcc version 4.6.0 20100508 (experimental) (GCC)</p>
<p style="text-align: justify;">Although I focused on OSX build/installation the steps described are the same to any architecture. Build an compiler - especially a cross-compiler (no that case) - demands time and patience to understand many particularities.</p>
<p style="padding-left: 30px;">Enjoy ;-)</p>