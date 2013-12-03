---
layout: post
title: Acionando os mantenedores
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Se você precisar entrar em contato com o mantendor de algum sub-sistema do kernel <a href="http://www.kernel.org" target="_blank">Linux</a> mas não sabe onde procurar, utilize um <em>script</em> (get_maintainer.pl) incluído no próprio código. Um exemplo,  suponha que você utilize o sistema de arquivos <a href="http://ext4.wiki.kernel.org/index.php/Main_Page" target="_blank">ext4</a> e deseje sugerir alguma idéia. Se for um <em>bug</em> é recomendado utilizar a <a href="http://bugzilla.kernel.org/" target="_blank">plataforma</a> de submissão de bugs (bugzilla) que além de seguir uma metodologia para descrever o erro é uma forma de catalogar o problema. Estou considerando neste <em>post</em> que você ainda não é um desenvolvedor e quer achar o mantenedor pois gostaria de fazer uma sugestão ou comentário acerca da área do código-fonte que ele mantém. Este tipo de busca talvez seja mais intessante nos <em>devices drivers...</em></p>
<p style="text-align: justify;"><em><span style="font-style: normal;">Um exemplo com o ext4:</span></em></p>
<p style="text-align: justify;"><em> </em></p>
<p style="padding-left: 30px; "><strong>./scripts/get_maintainer.pl -f  fs/ext4/</strong></p>
<p style="padding-left: 60px; "><em><em>"Theodore Ts'o" &lt;tytso@...&gt;</em></em></p>
<p style="padding-left: 60px; "><em><span style="background-color: #ffffff; font-style: normal;"><em> </em></span>Aneesh Kumar K.V &lt;aneesh.kumar@...&gt; </em></p>
<p style="padding-left: 60px; "><em><span style="background-color: #ffffff; font-style: normal;"><em>Eric Sandeen &lt;sandeen@...&gt; </em></span></em></p>
<p style="padding-left: 60px; "><em><span style="background-color: #ffffff; font-style: normal;"><em> </em></span><span style="background-color: #ffffff; font-style: normal;"><em><span style="background-color: #ffffff; font-style: normal;"><em>linux-kernel@vger.kernel.org <span style="color: #ff0000;">(lembre-se de se cadastrar e sempre de copiar a lista de email junto)</span></em></span></em></span></em></p>

Um exemplo com o <em>driver</em> de video da Intel:

<span style="color: #ff0000;"><em> </em></span>

<span style="color: #ff0000;"><em> </em></span>
<p style="padding-left: 30px;"><em><strong>./scripts/get_maintainer.pl -f drivers/video/intelfb/</strong></em></p>

<em> </em>

<em> </em>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">Sylvain Meyer &lt;sylvain.meyer@worldonline.fr&gt;</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">Andrew Morton &lt;akpm@linux-foundation.org&gt;</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">Thomas Hilber &lt;sparkie@lowbyte.de&gt;</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">Stefan Husemann &lt;shusemann@googlemail.com&gt;</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">Hannes Eder &lt;hannes@hanneseder.net&gt;</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">Paul Menzel &lt;paulepanter@users.sourceforge.net&gt;</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">linux-fbdev-devel@lists.sourceforge.net</div>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 0px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">linux-kernel@vger.kernel.org</div>
<p style="padding-left: 30px; "><span style="color: #ff0000;"><em><span style="color: #000000;"><span style="font-style: normal;"> </span></span></em></span></p>
<p style="padding-left: 60px; ">Sylvain Meyer &lt;sylvain.meyer@...&gt;</p>
<p style="padding-left: 60px; ">Andrew Morton &lt;akpm@...&gt;</p>
<p style="padding-left: 60px; ">Thomas Hilber &lt;sparkie@...&gt;</p>
<p style="padding-left: 60px; ">Stefan Husemann &lt;shusemann@...&gt;</p>
<p style="padding-left: 60px; ">Hannes Eder &lt;hannes@...&gt;</p>
<p style="padding-left: 60px; ">Paul Menzel &lt;paulepanter@...&gt;</p>
<p style="padding-left: 60px; ">linux-fbdev-devel@lists.sourceforge.net</p>
<p style="padding-left: 60px; ">linux-kernel@vger.kernel.org</p>
<p style="padding-left: 30px; "></p>

<span style="background-color: #ffffff;">Dar o retorno do uso de algum programa é ótimo para o desenvolvedor e garante a qualidade do sotfware. </span>