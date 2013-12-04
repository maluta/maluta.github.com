---
layout: post
title: Licenas para mdulos no Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



O arquivo <em>/usr/src/linux/include/linux/module.h</em> define as licenas aceitveis para um mdulo (ou <em>driver</em>) seja reconhecido como software livre.
<ul>
	<li><strong>GPL</strong> -<em>GNU Public License v2 or later</em></li>
	<li><strong>GPL v2</strong> -<em>GNU Public License v2</em></li>
	<li><strong>GPL and additional rights</strong> -<em>GNU Public License v2 rights and more</em></li>
	<li><strong>Dual BSD/GPL</strong> -<em>GNU Public License v2or BSD license choice</em></li>
	<li><strong>Dual MIT/GPL</strong> -<em>GNU Public License v2or MIT license choice</em></li>
	<li><strong>Dual MPL/GPL</strong> -<em> GNU Public License v2or Mozilla license choice</em></li>
</ul>
<div id="_mcePaste">Tambm h um espao (infelizmente) para licenas proprietrias:</div>
<div>
<ul>
	<li><strong>Proprietary <em>- </em></strong><em>Non free products
</em></li>
</ul>
</div>
Como vocs podem notar, h componentes que podem ser definidos com licenas duplas, contudo quando executado no Linux apenas a GPL  relevante. Algumas razes para definir a licena:
<ol>
	<li><span id="result_box" class="short_text"><span>O </span><em>modinfo</em><span> pode  mostrar informaes para usurios que desejam avaliar as licenas dos mdulos sua instalao.</span></span></li>
	<li><span id="result_box" class="short_text"><span><span id="result_box" class="short_text">A comunidade  pode ignorar relatrios de <em>bugs</em> dos mdulos proprietrios.</span></span></span></li>
	<li><span id="result_box" class="short_text"><span><span id="result_box" class="short_text">Os fabricantes podem fazer o mesmo com suas prprias polticas.</span></span></span></li>
</ol>
Para inserir a licena, basta colocar no seu cdigo-fonte a macro "MODULE_LICENCE". Exemplo:
<pre>MODULE_LICENCE("GPL");</pre>
Lembre-se que alguns recursos do <em>kernel</em> so disponveis apenas se seu cdigo  livre.

Um exemplo  o <strong>sysfs</strong> (atravs da macro EXPORT_SYMBOL_GPL) que por questes demanuteno e consistncia exige que voc licencie seu mdulo em alguma licena compatvel com a GPL.