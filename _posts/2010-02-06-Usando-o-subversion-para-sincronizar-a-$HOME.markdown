---
layout: post
title: Usando o subversion para sincronizar a $HOME
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Enfim postando no blog agora que não tenho mais <del datetime="2010-02-06T20:25:18+00:00">dor de cabeça</del> universidade, mas vamos ao que interessa.

A muito tempo atrás vinha procurando uma forma de sincronizar minhas configurações de usuário como chaves públicas, scripts, hosts através de várias máquinas, uma vez que tenho que manter em sincronia a minha máquina no trabalho, notebook pessoal, desktop pessoal (fora as máquinas virtuais).

A um tempo tentei algo como um script que utilizava scp, para sincronizar diretórios, mas com o problema de consumo de banda (o que no Brasil é um grande problema) e sobrescrever  alterações, resolvi adotar o rsync que já otimizava o uso da banda enviando somente as alterações e faz a checagem da data de modificação porém ele não faz nenhuma verificação quanto ao conteúdo do arquivo, e isto trazia um sério problema pois uma vez que houvessem alterações em duas máquinas, teríamos um sério problema na hora de sincronizar os arquivos.

Um dia desses no trabalho, utilizando o subversion para controle de versão em um projeto, ele fornece backup dos arquivos, histórico de alterações, otimiza o consumo de banda enviando somente alterações e ainda por cima verifica o conteúdo dos arquivos em questão.. Comecei a associar as coisas, e isto parecia ser uma possível solução para o meu problema, por que não tentar?

Criado o repositório online, ja que todas máquinas tem acesso a internet, dei um checkout na minha $HOME para criar os diretórios .svn de controle, a primeira coisa que fiz foi ignorar todos arquivos na minha pasta pessoal com o comando:

<pre lang="bash">svn propset svn:ignore *</pre>

Isto deve ser feito senão <strong>todos</strong> arquivos na HOME serão tratados como desconhecidos e perguntado se não devem ser adicionados ao controle de versão e não queremos isto, queremos fazer o controle de somente alguns arquivos/diretórios que são de nosso interesse.

logo após esse procedimento podemos começar a adicionar nossos arquivos ao controle de versão, como por exemplo nossa pasta .ssh e .gnupg para ter nossa chave pública em todas as máquinas:

<pre lang="bash">$ svn add .ssh
$ svn add .gnupg</pre>

Caso queira ignorar algum arquivo como o known_hosts na pasta ssh proceda da seguinte forma:

<pre lang="bash">$ svn rm --keep-local known_hosts
$ svn propset svn:ignore known_hosts</pre>

Uma vez feito isto já temos os arquivos que queremos no controle de versão e só falta o commit:

<pre lang="bash">$ svn status -uv # cheque se esta tudo ok ;)
$ svn commit -m "commit inicial da home"</pre>

Estou usando a algum tempo este procedimento, e tem dado muito certo, uma vez que não perco meus arquivos, mantenho um registro das alterações e tenho minhas máquinas (virtuais) sincronizadas. happy syncin'.