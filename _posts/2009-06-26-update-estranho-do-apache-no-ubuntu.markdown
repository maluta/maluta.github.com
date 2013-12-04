---
layout: post
title: Update Estranho do Apache no Ubuntu
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



"Hoje apareceu para fazer a atualiza��o para uma nova vers�o do Apache, mas perae, j� o fiz semana retrasada isso!", voc� tamb�m se fez essa pergunta, pois �..
O Ubuntu <a href="http://www.ubuntu.com/usn">USN</a> publicou no dia 12 de junho um <a href="http://www.ubuntu.com/usn/usn-787-1">security notice</a> referente ao Apache e que deveria atualizar para a vers�o 2.2.8-1ubuntu0.8 (isso no 8.04LTS) e hoje me aparece dispon�vel um pacote vers�o 2.2.8-1ubuntu0.9, sem publica��o no USN sobre este pacote.

Verificando o <a href="http://changelogs.ubuntu.com/changelogs/pool/main/a/apache2/apache2_2.2.8-1ubuntu0.9/changelog">changelog</a>, encontrei a seguinte info:

apache2 (2.2.8-1ubuntu0.9) hardy-proposed; urgency=low

  * debian/patches//101_fix-spinning-mod_proxy.dpatch: Fix mod_proxy
    with SSL using all the CPU. (LP: #306293)

 -- Chuck Short <zulcss@ubuntu.com>  Fri, 13 Feb 2009 15:43:29 +0000


�, pelo visto s� temos security update, quando temos um CVE envolvido, e quem usa Apache (ainda mais em uma vers�o LTS) vai dando apt-get update && apt-get upgrade toda noite pra n�o ter uma bela surpresa.

ps: Adoro atualiza��o autom�tica de servi�os, principalmente quando eles n�o voltam na reinicializa��o autom�tica.
