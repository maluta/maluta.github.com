---
layout: post
title: Simple C macro for debugging
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



A little trick if you use <em>printf</em> to debug information in your code and don't like to comment/uncomment. 
<pre lang="c">
#include <stdio.h>

#define dprintf if (debug) printf

const char debug = 1; /* or 0 if you want disable debug */ 

int main(int argc, char *argv[] ) {
     dprintf ("debug message");
     return 0;
}
</pre>
<p align="justify">
Remember that using <em>printf</em> is just one way to debug your code and an excess can impair the efficiency to analyze the situation or catch bugs. If you need start your program, specifying anything that might affect its behavior; make your program stop on specified conditions; examine what has happened, when your program has stopped or change things in your program, so you can experiment with correcting the effects of one bug and go on to learn about another; use programs such as <a href="http://www.gnu.org/software/gdb/">GDB</a> or <a href="http://valgrind.org/">Valgrind</a> (especially to memory management issues)
</p>