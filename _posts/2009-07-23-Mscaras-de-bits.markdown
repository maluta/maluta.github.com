---
layout: post
title: Mscaras de bits
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Este  um pequeno resumo para utilizar <a href="http://en.wikipedia.org/wiki/Mask_(computing)">mscara-de-bits</a> quando voc precisar armazenar <em>flags</em> booleanas em uma nica varivel inteira.Abaixo esto dois exemplos, um em C e outro em Python.
<h2>Linguagem C</h2>
<pre lang="c" escaped="true">#define FLAG_TEMPERATURA 1
#define FLAG_ALARME_1    2
#define FLAG_ALARME_2    4
#define FLAG_INTERRUPCAO 8</pre>
Lembre-se de organizar em potncias de 2.
<h3>1) Para verificar o valor utilize a lgica AND:</h3>
<pre lang="c;" escaped="true">if (flags &amp; FLAG_TEMPERATURA) {
/* ... */
}</pre>
<h3>2) Para setar em TRUE o valor, utilize a lgica OR:</h3>
<pre lang="c" escaped="true">flags |= FLAG_ALARME_1;</pre>
<h3>3) Para setar em FALSE o valor, utilize a lgica AND e NOT:</h3>
<pre lang="c" escaped="true">flags &amp;= ~FLAG_ALARME_2;</pre>
<h2>Python</h2>
<pre lang="python" escaped="true">#!/usr/bin/python

FLAG_TEMPERATURA = 1&lt;&lt;0 # 1
FLAG_ALARME_1 = 1&lt;&lt;1    # 2
FLAG_ALARME_2 = 1&lt;&lt;2    # 4
FLAG_INTERRUPCAO = 1&lt;&lt;3 # 8

# comeca setando a flag
flags = FLAG_TEMPERATURA

# verificando se a FLAG_INTERRUPCAO esta ativa
if flags &amp; FLAG_INTERRUPCAO:
	print "FLAG_INTERRUPCAO: TRUE"
else:
	print "FLAG_INTERRUPCAO: FALSE"

# anexa outra flag
flags |= FLAG_INTERRUPCAO

# verificando se a FLAG_INTERRUPCAO esta ativa
if flags &amp; FLAG_INTERRUPCAO:
	print "FLAG_INTERRUPCAO: TRUE"
else:
	print "FLAG_INTERRUPCAO: FALSE"

# a FLAG_TEMPERATURA continua como esta:
if flags &amp; FLAG_TEMPERATURA:
	print "FLAG_TEMPERATURA: TRUE"
else:
	print "FLAG_TEMPERATURA: FALSE"

# volta-se ao estado inicial (false)
flags &amp;= ~FLAG_INTERRUPCAO

# novo status da FLAG_INTERRUPO
if flags &amp; FLAG_INTERRUPCAO:
	print "FLAG_INTERRUPCAO: TRUE"
else:
	print "FLAG_INTERRUPCAO: FALSE"</pre>