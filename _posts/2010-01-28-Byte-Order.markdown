---
layout: post
title: Byte Order
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



In the book about <em>Linux Kernel Programming</em> the author<em> Robert Love</em> demonstrated a trick to check your hardware <em>endianness</em>.
<pre lang="c">int x = 1;
if (*(char *)&x == 1)
/* little endian */
else
/* big endian */</pre>
<p style="text-align: justify;">Using <a href="http://gcc.gnu.org">GCC</a> you can use <strong>-mbig-endian </strong>or <strong>-mlittle-endian</strong> to generate appropriate endianess. Remember to check man pages section on your architecture (i.e: i386 and x86-64 <span style="text-decoration: underline;">don't</span> implement this option whilst IA-64 and ARM yes)</p>
<p style="text-align: justify;">One interesting point regards on byte swapping. Suppose that you have a file that starts with 0x<span style="color: #ff0000;">aabb</span><span style="color: #000080;">ccdd</span> referring to little endian and 0x<span style="color: #000080;">ddcc</span><span style="color: #ff0000;">bbaa</span> referring to big endian (note that I took these values and order arbitrarily). In order to use one kind of byte order in your code we need check what endianness your file was generated and if necessary rectify. This C++ code exemplifies.</p>

<pre lang="cpp">
class Endian {

     int _byteSwapped;

public:

     Endian(unsigned long dw) {

        if (0xaabbccddL == dw) _byteSwapped = 1;
        else if (0xddccbbaaL == dw)  _byteSwapped = 0; 
        else throw "error";
   
     }

     long rectify(long dw) const {

        if (!_byteSwapped) return dw;
        char result[4] = {((char*) &dw)[3],((char*) &dw)[2],((char*) &dw)[1],((char*) &dw)[0]};
        return (*((long*) result));

     }
};
</pre>

Another way to do byte swapping is using an macro. The following example swap two bytes:

<pre lang="c">
#define SwapTwoBytes(data) ( (((data) >> 8) & 0x00FF) | (((data) << 8) & 0xFF00) )
</pre>

<p style="text-align: justify;">One of the best practices is provide one software that will work correctly no matter which processor Endian-architecture the code is executed on, eliminating the need to rewrite the code. Intel has a interesting <a href="http://www.intel.com/design/intarch/papers/endian.pdf">paper</a> on Converting Endian-specific to Endian-neutral Code (pg. 15-16).</p>