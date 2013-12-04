---
layout: post
title: latex + bibtex
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: right;"><em>Tá tudo certo e nada funciona?</em></p>
Supondo que você tenha dois arquivos.
<ol>
	<li>artigo.tex</li>
	<li>biblio.bbl</li>
</ol>
E está tendo erros quando tenta fazer uma citação (<em>\cite{Autor}</em>), tipo:
<ul>
	<li>LaTeX Warning: There were undefined references.</li>
	<li>LaTeX Warning: Citation `XXXX' on page n undefined on input line N.</li>
</ul>
Isso acontece pois alguns arquivos precisam ser gerados (basicamente o <em>aux</em>, <em>bbl</em> e <em>blg</em>) e há uma dependência circular. A solução é simples:
<pre lang="bash">pdflatex artigo.tex
bibtex all
pdflatex artigo.tex
pdflatex artigo.tex</pre>