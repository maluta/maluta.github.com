---
layout: post
title: Baixo Desempenho Intel Ubuntu 9.04
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Já tentou as dicas para o problema de regressão de desempenho das placas intel (driver: intel) no Ubuntu 9.04 e mesmo assim continua com baixo desempenho?

tente adicionar a linha Option      "XAANoOffscreenPixmaps", na sua section "Device", ficando assim:

<em>Section "Device"
Identifier  "Configured Video Device"
Option      "XAANoOffscreenPixmaps"
EndSection</em>

