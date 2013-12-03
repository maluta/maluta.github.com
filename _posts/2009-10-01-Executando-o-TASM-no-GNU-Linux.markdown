---
layout: post
title: Executando o TASM no GNU-Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">A série de utilitários <em>Turbo</em> da Borland foi muito popular nos 80 e 90. Havia o <em>Turbo Assembler</em>, <em>Turbo Liker</em>, <em>Turbo C</em>, <em>Turbo Debugger</em>, etc; A versão que preciso utilizar tem <span style="text-decoration: line-through;">retrições no endereçamento da memória</span> roda no modo do MS-DOS. Hoje, sem o qemu/virtualbox para utilizar o Windows, resolvi partir para o Wine e obtive o seguinte erro:</p>

<pre style="padding-left: 30px; text-align: justify;"># wine TASM.EXE
err:dosmem:DOSMEM_MapDosLayout Need full access to the first megabyte for DOS mode</pre>
<p style="text-align: justify;">Lembrei então do programa <a href="http://www.dosemu.org" target="_blank">dosemu</a>. A instalação (está presente na maioria dos gerenciadores de pacotes) e uso são simples. Após a execução você é direcionado a um <em>prompt</em> (igual ao <em>command</em> no Windows) que executa o <a href="http://www.freedos.org/" target="_blank">FreeDOS</a>. A partir deste ponto é ir até a partição com permissão de escrita - no meu caso D: - que reflete o diretório /root do  sistema.</p>


[caption id="" align="aligncenter" width="582" caption="Executando o Turbo Debugger 2.0 no DOSEMU"]<img class="size-full wp-image-464" title="tasm rodando no linux" src="http://www.coding.com.br/wp-content/uploads/2009/10/3972507943_12b58d3b30_o.png" alt="tasm rodando no linux" width="582" height="346" />[/caption]

Alguns pontos:
<ul>
	<li style="text-align: justify;">É possivel utilizar o DOSEMU com o usuário <a href="http://dosemu.sourceforge.net/docs/README/1.1.3.7/runasuser.html" target="_blank">normal</a>.</li>
	<li style="text-align: justify;">Usar o 'edit' é perda te tempo, prefira <a href="http://www.vim.org" target="_blank">outras</a> opções e utilize o <em>prompt</em> somente para invocar os comandos.</li>
	<li style="text-align: justify;">Se realmente não precisasse, nunca iria usar este programa, hoje em dia há opções <strong>bem</strong> melhores como o GNU Assembler (<a href="http://en.wikipedia.org/wiki/GNU_Assembler" target="_blank">gas</a>) ou até mesmo o <a href="http://www.coding.com.br/programacao/depurando-programas-em-assembly-no-gnulinux-parte-1/" target="_blank">nasm</a>.</li>
</ul>