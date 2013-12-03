---
layout: post
title: Busca textual em arquivos
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p>Como resolver o problema de arquivos com espaço em branco na hora de fazer uma busca textual?</p>
<p>Qualquer uma das três formas funciona:</p>
<pre>
   1. find PATH -iname FILTRO -exec grep -n PALAVRA '{}' \; -print
   2. find PATH -iname FILTRO -exec grep -n PALAVRA /dev/null '{}' \;
   3. find PATH -iname FILTRO -exec grep -Hn PALAVRA '{}' \;
</pre>
<p>Exemplo:</p>
<p>Vamos imaginar a seguinte hieraquia de pastas e arquivos:</p>
<p><a href="http://www.coding.com.br/wp-content/uploads/2009/10/tree.jpeg"><img src="http://www.coding.com.br/wp-content/uploads/2009/10/tree.jpeg" alt="" title="" width="321" height="465" class="aligncenter size-full wp-image-348" /></a><br />
De modo que o comando:</p>
<pre>
$ find . -iname "nome*"
</pre>
<p>Mostre todos os arquivos que começam com "nome"</p>
<p style="padding-left: 30px;">
<span style="color: #ff0000;"><br />
./c/c3/nome2 sobrenome2<br />
./c/c3/nome1 sobrenome1<br />
./b/b2/nome1 sobrenome1 final1<br />
./b/b3/nome2 sobrenome2<br />
./b/b1/nome1 sobrenome2 mais um pouco<br />
./a/a3/nome1 sobrenome1<br />
./a/a1/nome2 sobrenome3<br />
./a/a1/nome sobrenome<br />
./a/a1/nome1 sobrenome1<br />
</span>
</p>
<p>Para fazer a busca do algum texto dentro desses arquivos, poderiamos pensar algo como:</p>
<pre>
$ find . -iname "nome*" | xargs grep teste
</pre>
<p>Mas o espaço em branco iria atrapalhar a interpretação dos arquivos...</p>
<p style="padding-left: 30px;">
<span style="color: #ff0000;"><br />
grep: ./c/c3/nome2: No such file or directory<br />
grep: sobrenome2: No such file or directory<br />
grep: ./c/c3/nome1: No such file or directory<br />
grep: sobrenome1: No such file or directory<br />
</span>
</p>
<p style="padding-left: 30px;">
<span style="color: #ff0000;"><br />
		(...)<br />
</span>
</p>
<p style="padding-left: 30px;">
<span style="color: #ff0000;"><br />
grep: ./a/a1/nome1: No such file or directory<br />
grep: sobrenome1: No such file or directory<br />
</span>
</p>
<p>Uma das soluções está no próprio find:</p>
<pre>
$ find . -iname "nome*" -exec grep teste '{}' \;
</pre>
<p style="padding-left: 30px;">
<span style="color: #ff0000;"><br />
teste 123<br />
</span>
</p>
<p>Contudo, é importante saber o número da linha da ocorrência e o nome do arquivo, logo:</p>
<pre>
find . -iname "nome*" -exec grep -n teste '{}' \; -print
</pre>
<p style="padding-left: 30px;">
<span style="color: #ff0000;"><br />
1:teste 123<br />
./c/c3/nome2 sobrenome2<br />
</span></p>
