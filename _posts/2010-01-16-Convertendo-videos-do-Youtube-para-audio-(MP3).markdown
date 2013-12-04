---
layout: post
title: Convertendo videos do Youtube para audio (MP3)
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: left;">Programas necessários:</p>

<ul>
	<li>Alguma distribuição GNU/Linux</li>
	<li><a href="http://www.mplayerhq.hu" target="_blank">mplayer</a></li>
	<li><a title="Lame project" href="http://lame.sourceforge.net" target="_blank">lame</a> (caso queria converter para mp3)</li>
	<li><a href="http://www.vorbis.com " target="_blank">vorbis-tools</a> (caso queira converter para ogg)</li>
</ul>
<p style="text-align: justify;">Os videos do YouTube, normalmente qualquer conteúdo Flash, fica armazenados na pasta <strong>/tmp</strong> do sistema operacional na forma FlashXXXX (exemplo: FlashaOiW6k). Para cada arquivo flash existirá um arquivo correspondente, para descobrir de qual se trata utilize o mplayer, no console (cd /tmp):</p>

<pre style="text-align: justify;">mplayer FlashaOiW6k</pre>
<p style="text-align: justify;">Após descobrir o arquivo, vamos primeiro converter o arquivo para <strong>wav </strong>e depois para algum formato mais compacto.</p>

<pre>mplayer FlashaOiW6k<span style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; line-height: 19px; white-space: normal; font-size: 13px; "> -novideo -ao pcm:file=musica.wav</span></pre>
<span style="font-family: Consolas, Monaco, 'Courier New', Courier, monospace; line-height: 18px; font-size: 12px; white-space: pre; "><span style="font-family: Georgia, 'Times New Roman', 'Bitstream Charter', Times, serif; line-height: 19px; white-space: normal; font-size: 13px; ">Convertendo para <strong>mp3</strong>:</span></span>
<div id="_mcePaste" style="position: absolute; left: -10000px; top: 159px; width: 1px; height: 1px; overflow-x: hidden; overflow-y: hidden;">lame -V2 input.wav output.mp3</div>
<pre>lame -V2 musica.wav musica.mp3</pre>
<div></div>
Ou <strong>ogg</strong>:
<pre>oggenc musica.wav</pre>
No final temos os seguintes tamanhos para cada arquivo, considerando uma música de 4 minutos.
<ul>
	<li>8.9M    FlashaOiW6k</li>
	<li>21.0M    saida.wav</li>
	<li>2.4M   saida.mp3</li>
	<li>1.5M   saida.ogg</li>
</ul>
Este procedimento provavelmente irá funcionar para qualquer conteúdo Flash (ex. outros sites de video) que fique armazenado na tmp.