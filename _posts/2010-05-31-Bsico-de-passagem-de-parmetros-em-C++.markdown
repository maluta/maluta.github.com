---
layout: post
title: Bsico de passagem de parmetros em C++
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: right;"><em>para no acontecer certos erros que vi por a...</em></p>
Em C++ h <strong>trs</strong> maneiras de passar um parmetro para uma funo, as tradicionais herdadas da linguagem C: <em>valor </em>e <em>ponteiro</em>; alm da novidade: a passagem por <em>referncia. </em>Para ilustrar veja o seguinte exemplo, passar uma estrutura de dados "grande" (neste caso aproximadamente 10 kilobytes) para uma funo:

<span style="color: #0000ff;"><strong>#include<span style="color: #008000;">&lt;iostream&gt;</span></strong></span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;string.h&gt;</span> </strong></span>

<strong>using</strong> <strong>namespace</strong> <span style="color: #2040a0;">std</span><span style="color: #4444ff;">;</span>

<strong>struct</strong> <span style="color: #2040a0;">Big</span> <span style="color: #4444ff;"><strong>{</strong></span>
<strong> char</strong> <span style="color: #2040a0;">text</span><span style="color: #4444ff;">[</span><span style="color: #ff0000;">10000</span><span style="color: #4444ff;">]</span><span style="color: #4444ff;">;</span>
<strong> int</strong> <span style="color: #2040a0;">id</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span><span style="color: #4444ff;">;</span>

<strong>void</strong> <span style="color: #2040a0;">f1</span><span style="color: #4444ff;">(</span> <span style="color: #2040a0;">Big</span> <span style="color: #2040a0;">v</span> <span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>
<span style="color: #2040a0;"> cout</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">v</span>.<span style="color: #2040a0;">text</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">endl</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;"> cout</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #008000;">"Ox"</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">hex</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">v</span>.<span style="color: #2040a0;">id</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">endl</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<strong>void</strong> <span style="color: #2040a0;">f2</span><span style="color: #4444ff;">(</span> <strong>const</strong> <span style="color: #2040a0;">Big</span> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">v</span> <span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>
<span style="color: #2040a0;"> cout</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">v</span><span style="color: #4444ff;">-</span><span style="color: #4444ff;">&gt;</span><span style="color: #2040a0;">text</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">endl</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;"> cout</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #008000;">"Ox"</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">hex</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">v</span><span style="color: #4444ff;">-</span><span style="color: #4444ff;">&gt;</span><span style="color: #2040a0;">id</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">endl</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<strong>void</strong> <span style="color: #2040a0;">f3</span><span style="color: #4444ff;">(</span> <strong>const</strong> <span style="color: #2040a0;">Big</span> <span style="color: #4444ff;">&amp;</span><span style="color: #2040a0;">v</span> <span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>
<span style="color: #2040a0;"> cout</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">v</span>.<span style="color: #2040a0;">text</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">endl</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;"> cout</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #008000;">"Ox"</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">hex</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">v</span>.<span style="color: #2040a0;">id</span> <span style="color: #4444ff;">&lt;</span><span style="color: #4444ff;">&lt;</span> <span style="color: #2040a0;">endl</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<strong>int</strong> <span style="color: #2040a0;">main</span><span style="color: #4444ff;">(</span><strong>int</strong> <span style="color: #444444;">/*argc*/</span>, <strong>char</strong> <span style="color: #4444ff;">*</span> <span style="color: #444444;">/*argv*/</span><span style="color: #4444ff;">[</span><span style="color: #4444ff;">]</span><span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>

<span style="color: #2040a0;"> Big</span> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">b0</span> <span style="color: #4444ff;">=</span> <strong>new</strong> <span style="color: #2040a0;">Big</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;"> Big</span> <span style="color: #2040a0;">b1</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;"> Big</span> <span style="color: #4444ff;">&amp;</span><span style="color: #2040a0;">b2</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">b1</span><span style="color: #4444ff;">;</span>

<span style="color: #2040a0;"> strcpy</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">b0</span><span style="color: #4444ff;">-</span><span style="color: #4444ff;">&gt;</span><span style="color: #2040a0;">text</span>,<span style="color: #008000;">"asdfg asdfg asdf asdf asdf asdf"</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;"> strcpy</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">b1</span>.<span style="color: #2040a0;">text</span>,<span style="color: #008000;">"azsxd azsxd azsxd azsxd azsxd azsxd"</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>

<span style="color: #2040a0;"> b0</span><span style="color: #4444ff;">-</span><span style="color: #4444ff;">&gt;</span><span style="color: #2040a0;">id</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">0xbc</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;"> b1</span>.<span style="color: #2040a0;">id</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">0xde</span><span style="color: #4444ff;">;</span>

<span style="color: #2040a0;"> f2</span><span style="color: #4444ff;">(</span> <span style="color: #2040a0;">b0</span> <span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span> <span style="color: #444444;">/* pointer */</span>
<span style="color: #2040a0;"> f1</span><span style="color: #4444ff;">(</span> <span style="color: #2040a0;">b1</span> <span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span> <span style="color: #444444;">/* value */</span>
<span style="color: #2040a0;"> f3</span><span style="color: #4444ff;">(</span> <span style="color: #2040a0;">b2</span> <span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span> <span style="color: #444444;">/* reference */</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<span style="color: #4444ff;"><strong>
</strong></span>

Veja o cdigo <em>assembly</em> gerado pelo compilador (g++) para cada um dos trs casos:

<strong>1) Ponteiro</strong>
<pre lang="asm">mov    -0xc(%ebp),%eax
mov    %eax,(%esp)
call   0x8048885</pre>
<strong>2) Valor</strong>
<pre lang="asm">movl   $0x0,-0x2728(%ebp)
lea    -0x2720(%ebp),%eax
mov    %eax,-0x272c(%ebp)
jmp    0x8048a36
mov    -0x272c(%ebp),%ecx
mov    -0x2728(%ebp),%edx
movzbl (%ecx,%edx,1),%eax
mov    -0x2728(%ebp),%edx
mov    %al,(%esp,%edx,1)
addl   $0x1,-0x2728(%ebp)
cmpl   $0x2714,-0x2728(%ebp)
jb     0x8048a16
call   0x80488fe</pre>
<strong>3) Referncia</strong>
<pre lang="asm">mov    -0x8(%ebp),%eax
mov    %eax,(%esp)
call   0x804880c</pre>
Talvez seja importante:
<ul>
	<li>Se voc prefere a sintaxe da intel? Mude no GDB: <em>set disassembly-flavor intel</em></li>
	<li>No precisa ser muito esperto para ver que a passagem por valor  a pior de todas, veja quanto cdigo <em>assembly</em> foi gerado [#fail]</li>
	<li>A passagem por referncia  inclusive mais eficiente pois aloca no %ebp (<em>base pointer</em>) [8 bytes ao invs de 12 bytes do ponteiro].</li>
	<li>A passagem por referncia prov a eficincia da passagem por ponteiros com a clareza da passagem por valor.</li>
</ul>