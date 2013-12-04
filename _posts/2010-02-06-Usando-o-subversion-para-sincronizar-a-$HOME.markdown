---
layout: post
title: Usando o subversion para sincronizar a $HOME
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Enfim postando no blog agora que no tenho mais <del datetime="2010-02-06T20:25:18+00:00">dor de cabea</del> universidade, mas vamos ao que interessa.

A muito tempo atrs vinha procurando uma forma de sincronizar minhas configuraes de usurio como chaves pblicas, scripts, hosts atravs de vrias mquinas, uma vez que tenho que manter em sincronia a minha mquina no trabalho, notebook pessoal, desktop pessoal (fora as mquinas virtuais).

A um tempo tentei algo como um script que utilizava scp, para sincronizar diretrios, mas com o problema de consumo de banda (o que no Brasil  um grande problema) e sobrescrever alteraes, resolvi adotar o rsync que j otimizava o uso da banda enviando somente as alteraes e faz a checagem da data de modificao porm ele no faz nenhuma verificao quanto ao contedo do arquivo, e isto trazia um srio problema pois uma vez que houvessem alteraes em duas mquinas, teramos um srio problema na hora de sincronizar os arquivos.

Um dia desses no trabalho, utilizando o subversion para controle de verso em um projeto, ele fornece backup dos arquivos, histrico de alteraes, otimiza o consumo de banda enviando somente alteraes e ainda por cima verifica o contedo dos arquivos em questo.. Comecei a associar as coisas, e isto parecia ser uma possvel soluo para o meu problema, por que no tentar?

Criado o repositrio online, ja que todas mquinas tem acesso a internet, dei um checkout na minha $HOME para criar os diretrios .svn de controle, a primeira coisa que fiz foi ignorar todos arquivos na minha pasta pessoal com o comando:

<pre lang="bash">svn propset svn:ignore *</pre>

Isto deve ser feito seno <strong>todos</strong> arquivos na HOME sero tratados como desconhecidos e perguntado se no devem ser adicionados ao controle de verso e no queremos isto, queremos fazer o controle de somente alguns arquivos/diretrios que so de nosso interesse.

logo aps esse procedimento podemos comear a adicionar nossos arquivos ao controle de verso, como por exemplo nossa pasta .ssh e .gnupg para ter nossa chave pblica em todas as mquinas:

<pre lang="bash">$ svn add .ssh
$ svn add .gnupg</pre>

Caso queira ignorar algum arquivo como o known_hosts na pasta ssh proceda da seguinte forma:

<pre lang="bash">$ svn rm --keep-local known_hosts
$ svn propset svn:ignore known_hosts</pre>

Uma vez feito isto j temos os arquivos que queremos no controle de verso e s falta o commit:

<pre lang="bash">$ svn status -uv # cheque se esta tudo ok ;)
$ svn commit -m "commit inicial da home"</pre>

Estou usando a algum tempo este procedimento, e tem dado muito certo, uma vez que no perco meus arquivos, mantenho um registro das alteraes e tenho minhas mquinas (virtuais) sincronizadas. happy syncin'.