---
layout: post
title: Assembly inline
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">I've made some code snippets about assembly inline with <a href="http://gcc.gnu.org/">GCC</a>. A <a href="http://www.google.com.br/search?sourceid=chrome&amp;ie=UTF-8&amp;q=assembly+inline+gcc">quick search</a> points to a lot of good documentation.</p>

<ul>
	<li>IBM DeveloperWorks about <em><a href="http://www.ibm.com/developerworks/linux/library/l-ia.html" target="_blank">Inline asssembly for x86 in Linux</a></em></li>
	<li>Linux Documentation Project HOWTO describin<em>g <a href="http://www.ibiblio.org/gferg/ldp/GCC-Inline-Assembly-HOWTO.html">GCC Inline Assembly</a> </em></li>
</ul>
<p style="text-align: justify;">The syntax may be confusing, if you don't understand read the documentation available. Each example are an C function with the special construct "asm" for inline assembly code. Examples:</p>

Increment an value:
<pre lang="c">void inc(int *value) {

    asm ( "incl %0"
         :"=a"(*value)
         :"0"(*value)
        );

}</pre>
Exchange to numbers:
<pre lang="c">void swap(int *x, int *y) {

    asm(""
        : "=a"(*y),"=b"(*x)
        : "a"(*x),"b"(*y)
       );

}</pre>
Copy an vector:
<pre lang="c">void vector_copy(int *v_src, int *v_dst, int *count) {

    asm("up: lodsl;"
	"    stosl;"
	"loop up;  "
	:
	: "S"(v_src), "D"(v_dst), "c"(*count)
	: "%eax"
	);

}</pre>
A simple copy:
<pre lang="c">void copy(int *from, int *to) {

     asm ("movl %1, %%eax;"
          "movl %%eax, %0;"
          :"=&amp;r"(*to)
          :"r"(*from));

}</pre>
A very simple implementation for strncpy:
<pre lang="c">void _strncpy(char *src, char *dst, int *count) {

    asm("cld;"
        "rep movsb;"
        :
        : "S"(src), // 'S' == %esi
	  "D"(dst), // 'D' == %edi
	  "c"(*count)); // 'c' == %ecx
}</pre>
If you like to try check this <a href="http://github.com/maluta/junk/blob/master/asm-inline.c">example</a>:
<pre style="padding-left: 30px;">wget http://github.com/maluta/junk/raw/master/asm-inline.c
gcc -Wall -ggdb asm-inline.c -o asm-inline
./asm-inline</pre>