---
layout: post
title: Usando o subversion para sincronizar a $HOME
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Enfim postando no blog agora que n�o tenho mais <del datetime="2010-02-06T20:25:18+00:00">dor de cabe�a</del> universidade, mas vamos ao que interessa.

A muito tempo atr�s vinha procurando uma forma de sincronizar minhas configura��es de usu�rio como chaves p�blicas, scripts, hosts atrav�s de v�rias m�quinas, uma vez que tenho que manter em sincronia a minha m�quina no trabalho, notebook pessoal, desktop pessoal (fora as m�quinas virtuais).

A um tempo tentei algo como um script que utilizava scp, para sincronizar diret�rios, mas com o problema de consumo de banda (o que no Brasil � um grande problema) e sobrescrever �altera��es, resolvi adotar o rsync que j� otimizava o uso da banda enviando somente as altera��es e faz a checagem da data de modifica��o por�m ele n�o faz nenhuma verifica��o quanto ao conte�do do arquivo, e isto trazia um s�rio problema pois uma vez que houvessem altera��es em duas m�quinas, ter�amos um s�rio problema na hora de sincronizar os arquivos.

Um dia desses no trabalho, utilizando o subversion para controle de vers�o em um projeto, ele fornece backup dos arquivos, hist�rico de altera��es, otimiza o consumo de banda enviando somente altera��es e ainda por cima verifica o conte�do dos arquivos em quest�o.. Comecei a associar as coisas, e isto parecia ser uma poss�vel solu��o para o meu problema, por que n�o tentar?

Criado o reposit�rio online, ja que todas m�quinas tem acesso a internet, dei um checkout na minha $HOME para criar os diret�rios .svn de controle, a primeira coisa que fiz foi ignorar todos arquivos na minha pasta pessoal com o comando:

<pre lang="bash">svn propset svn:ignore *</pre>

Isto deve ser feito sen�o <strong>todos</strong> arquivos na HOME ser�o tratados como desconhecidos e perguntado se n�o devem ser adicionados ao controle de vers�o e n�o queremos isto, queremos fazer o controle de somente alguns arquivos/diret�rios que s�o de nosso interesse.

logo ap�s esse procedimento podemos come�ar a adicionar nossos arquivos ao controle de vers�o, como por exemplo nossa pasta .ssh e .gnupg para ter nossa chave p�blica em todas as m�quinas:

<pre lang="bash">$ svn add .ssh
$ svn add .gnupg</pre>

Caso queira ignorar algum arquivo como o known_hosts na pasta ssh proceda da seguinte forma:

<pre lang="bash">$ svn rm --keep-local known_hosts
$ svn propset svn:ignore known_hosts</pre>

Uma vez feito isto j� temos os arquivos que queremos no controle de vers�o e s� falta o commit:

<pre lang="bash">$ svn status -uv # cheque se esta tudo ok ;)
$ svn commit -m "commit inicial da home"</pre>

Estou usando a algum tempo este procedimento, e tem dado muito certo, uma vez que n�o perco meus arquivos, mantenho um registro das altera��es e tenho minhas m�quinas (virtuais) sincronizadas. happy syncin'.