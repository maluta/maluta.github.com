---
layout: post
title: Licenas para mdulos no Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



O arquivo <em>/usr/src/linux/include/linux/module.h</em> define as licen�as aceit�veis para um m�dulo (ou <em>driver</em>) seja reconhecido como software livre.
<ul>
	<li><strong>GPL</strong> -�<em>GNU Public License v2 or later</em></li>
	<li><strong>GPL v2</strong> -�<em>GNU Public License v2</em></li>
	<li><strong>GPL and additional rights</strong> -�<em>GNU Public License v2 rights and more</em></li>
	<li><strong>Dual BSD/GPL</strong> -�<em>GNU Public License v2��or BSD license choice</em></li>
	<li><strong>Dual MIT/GPL</strong> -�<em>GNU Public License v2�or MIT license choice</em></li>
	<li><strong>Dual MPL/GPL</strong> -<em> GNU Public License v2�or Mozilla license choice</em></li>
</ul>
<div id="_mcePaste">Tamb�m h� um espa�o (infelizmente) para licen�as propriet�rias:</div>
<div>
<ul>
	<li><strong>Proprietary <em>- </em></strong><em>Non free products
</em></li>
</ul>
</div>
Como voc�s podem notar, h� componentes que podem ser definidos com licen�as duplas, contudo quando executado no Linux apenas a GPL � relevante. Algumas raz�es para definir a licen�a:
<ol>
	<li><span id="result_box" class="short_text"><span>O </span><em>modinfo</em><span> pode  mostrar informa��es para usu�rios que desejam avaliar as licen�as dos m�dulos sua instala��o.</span></span></li>
	<li><span id="result_box" class="short_text"><span><span id="result_box" class="short_text">A comunidade  pode ignorar relat�rios de <em>bugs</em> dos m�dulos propriet�rios.</span></span></span></li>
	<li><span id="result_box" class="short_text"><span><span id="result_box" class="short_text">Os fabricantes podem fazer o mesmo com suas pr�prias pol�ticas.</span></span></span></li>
</ol>
Para inserir a licen�a, basta colocar no seu c�digo-fonte a macro �"MODULE_LICENCE". Exemplo:
<pre>��MODULE_LICENCE("GPL");</pre>
Lembre-se que alguns recursos do <em>kernel</em> s�o dispon�veis apenas se seu c�digo � livre.

Um exemplo � o <strong>sysfs</strong> (atrav�s da macro EXPORT_SYMBOL_GPL) que por quest�es de�manuten��o e consist�ncia exige que voc� licencie seu m�dulo em alguma licen�a compat�vel com a GPL.