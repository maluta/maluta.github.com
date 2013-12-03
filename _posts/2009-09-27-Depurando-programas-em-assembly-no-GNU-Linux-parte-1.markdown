---
layout: post
title: Depurando programas em assembly no GNU/Linux (parte 1)
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Embora eu particularmente <a href="http://www.ibm.com/developerworks/linux/library/l-gas-nasm.html">prefira</a> a sintaxe AT&amp;T à Intel. Estou <a href="http://www.unifei.edu.br">tendo</a> que aprender a usá-la (e bem). Para os estudos optei pelo <a href="http://www.nasm.us/">NASM</a>, <a href="http://www.gnu.org/software/binutils/">GNU ld</a> e o <a href="http://www.gnu.org/software/gdb/">GDB</a>. Um processo simples, descrito abaixo:</p>

<p style="padding-left: 30px;">#<strong>nasm</strong> -g -f elf <span style="color: #000000;">programa.asm </span>
#<strong>ld</strong> <span style="color: #000000;">programa.o</span>
#<strong>gdb</strong> -q <span style="color: #000000;">a.out</span>

Vamos fazer um pequeno programa teste que carrega no registro <em>ecx</em> o valor da variável (var1) e em <em>edx</em> seu endereço:
<pre lang="asm">section .data

   var1 dd 40

section .text

   global _start

   _start:
      nop
      nop
      mov   ecx, [var1]
      lea   edx, [var1]

   _exit:
      mov   eax, 1
      int   80h</pre>
Dentro do gdb:
<pre>(gdb) break 11
Breakpoint 1 at 0x80480a1: file teste.asm, line 11.
(gdb) r
Starting program: /home/maluta/coding/a.out
Breakpoint 1, _start () at teste.asm:11
11            nop
(gdb) print var1
$1 = 40
(gdb) info registers ecx edx
ecx            0x0      0
edx            0x0      0</pre>
Adicionamos um <a href="http://sourceware.org/gdb/current/onlinedocs/gdb_6.html#SEC34">breakpoint</a> (eu precisei inserir duas instruções <em>nop</em> para o gdb realmente para no ponto) e verificamos os valores de <strong>var1</strong>, <strong>ecx</strong> e <strong>edx</strong>.
<pre>(gdb) si
_start () at teste.asm:12
12            mov   ecx, [var1]
(gdb) si
_start () at teste.asm:13
13            lea   edx, [var1]
(gdb) info registers ecx
ecx            0x28     40
(gdb) si
_exit () at teste.asm:16
16            mov   eax, 1
(gdb) info registers edx
edx            0x80490b8        134516920</pre>
E por fim, verificamos o conteúdo no endereço definido em edx.
<pre>(gdb) print *0x80490b8
$2 = 40</pre>
<p style="text-align: justify;">Algumas considerações:</p>

<ul style="text-align: justify;">
	<li style="text-align: justify;">O <a href="http://www.gnu.org/software/ddd/">Data Diplay Debugger</a> (DDD) é um <em>front-end</em> muito bom para o GDB que pode ser utilizado ao invés da interface de linha de comando.</li>
</ul>
<ul style="text-align: justify;">
	<li style="text-align: justify;">O após <em>label</em> <strong>_exit </strong>há uma chamada a uma <em>syscall</em> (adivinha qual?) do <a href="http://www.kernel.org">kernel</a>. Passa-se o valor (no registro eax) e chama uma interrupção (80h).  A verdadeira "diversão" está em associar essas syscalls (write, fork, execve, ...) mas isto é para outro <em>post</em>... Por enquanto vou lidar com os diferentes modos de endereçamento e operações lógicas e aritméticas.</li>
</ul>