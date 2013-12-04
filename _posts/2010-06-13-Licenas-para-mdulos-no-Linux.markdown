---
layout: post
title: Licenas para mdulos no Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



O arquivo <em>/usr/src/linux/include/linux/module.h</em> define as licenças aceitáveis para um módulo (ou <em>driver</em>) seja reconhecido como software livre.
<ul>
	<li><strong>GPL</strong> - <em>GNU Public License v2 or later</em></li>
	<li><strong>GPL v2</strong> - <em>GNU Public License v2</em></li>
	<li><strong>GPL and additional rights</strong> - <em>GNU Public License v2 rights and more</em></li>
	<li><strong>Dual BSD/GPL</strong> - <em>GNU Public License v2  or BSD license choice</em></li>
	<li><strong>Dual MIT/GPL</strong> - <em>GNU Public License v2 or MIT license choice</em></li>
	<li><strong>Dual MPL/GPL</strong> -<em> GNU Public License v2 or Mozilla license choice</em></li>
</ul>
<div id="_mcePaste">Também há um espaço (infelizmente) para licenças proprietárias:</div>
<div>
<ul>
	<li><strong>Proprietary <em>- </em></strong><em>Non free products
</em></li>
</ul>
</div>
Como vocês podem notar, há componentes que podem ser definidos com licenças duplas, contudo quando executado no Linux apenas a GPL é relevante. Algumas razões para definir a licença:
<ol>
	<li><span id="result_box" class="short_text"><span>O </span><em>modinfo</em><span> pode  mostrar informações para usuários que desejam avaliar as licenças dos módulos sua instalação.</span></span></li>
	<li><span id="result_box" class="short_text"><span><span id="result_box" class="short_text">A comunidade  pode ignorar relatórios de <em>bugs</em> dos módulos proprietários.</span></span></span></li>
	<li><span id="result_box" class="short_text"><span><span id="result_box" class="short_text">Os fabricantes podem fazer o mesmo com suas próprias políticas.</span></span></span></li>
</ol>
Para inserir a licença, basta colocar no seu código-fonte a macro  "MODULE_LICENCE". Exemplo:
<pre>  MODULE_LICENCE("GPL");</pre>
Lembre-se que alguns recursos do <em>kernel</em> são disponíveis apenas se seu código é livre.

Um exemplo é o <strong>sysfs</strong> (através da macro EXPORT_SYMBOL_GPL) que por questões de manutenção e consistência exige que você licencie seu módulo em alguma licença compatível com a GPL.