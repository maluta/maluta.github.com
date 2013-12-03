---
layout: post
title: MyHDL: trazendo o Python para o mundo das FPGAs
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: right;">From Python to silicon</p>
<p style="text-align: justify;"><em>Depois de uma longa história estou participando de <span style="text-decoration: line-through;">dois</span></em><em> um </em><em><a href="http://www.inatel.br/icc/cursos-abertos">curso aberto</a></em><em> sobre hardware: um abordando </em><a href="http://en.wikipedia.org/wiki/VHDL"><em>VHDL</em></a><em> </em><em><span style="text-decoration: line-through;">e outro </span></em><a href="http://en.wikipedia.org/wiki/Verilog"><em><span style="text-decoration: line-through;">Verilog</span></em></a><em>. Até aí nada de novo,</em><em> quando... </em><a href="http://twitter.com/maluta/status/11915212954" target="_blank"><em>descobri</em></a><em> algo interessante. Algo que realmente motivou <span style="text-decoration: line-through;">a mudar minha rotina de trabalho para (durante alguns dias)</span></em><em><span style="text-decoration: line-through;"> levantar as 7h.</span> a escrever sobre o assunto aqui no blog. :p</em></p>
<p style="text-align: justify;"><em><span style="font-style: normal;"><strong>MyHDL</strong></span></em></p>
<p style="text-align: justify;">Em poucas palavras, é um pacote para o Python que permite utilizá-lo para descrever e verificar uma linguagem de descrição de <em>hardware</em>. Além disso você pode converter seu código Pyhton em Verilog ou VHDL, automaticamente, para gravar numa CPLD ou FPGA. Para quem quiser aprender, o tutorial mais completo está na <a href="http://www.myhdl.org/doc/0.6" target="_blank">documentação</a> oficial do projeto. Há também uma <a href="http://www.cin.ufpe.br/~cinlug/wiki/index.php/Hardware_myhdl_python" target="_blank">introdução</a> muito boa em português feito pela UFPE.</p>
<p style="text-align: justify;">Não vou fazer um tutorial, apenas transcreverei os exemplos utilizados em sala de aula para Pythom, produzir os testes e os equivalentes em VHDL e Verilog. Um dos primeiros exercícios era descrever um multiplexador de 4 entradas.</p>

<pre lang="python">from myhdl import *  

def Mux(dout, din_1, din_2, din_3, din_4, sel):

	@always_comb
	def muxLogic():

		if sel == 0x0:
			 dout.next = din_1
		if sel == 0x1:
			 dout.next = din_2
		if sel == 0x2:
			 dout.next = din_3
		if sel == 0x3:
			 dout.next = din_4

	return muxLogic

def convert():
	dout, din_1, din_2, din_3, din_4  = [Signal(intbv(0)[8:]) for i in range(5)]
	sel =   Signal(intbv(0)[2:])
	toVHDL(Mux, din_1, din_2, din_3, din_4, dout, sel)
	toVerilog(Mux, din_1, din_2, din_3, din_4, dout, sel)

convert()</pre>
<p style="text-align: justify;">As funções <em>toVHDL()</em> e <em>toVerilog()</em> produzem arquivos Mux.vhd ou Mux.v respectivamente (o nome é o mesmo da função definida).</p>
<p style="text-align: justify;">Aguardem os próximos <em>posts</em> onde vou apresentar o <em>test case</em> para este e os novos exercícios que forem sugeridos em sala.</p>