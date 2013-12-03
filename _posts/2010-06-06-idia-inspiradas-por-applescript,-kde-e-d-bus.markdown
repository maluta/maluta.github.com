---
layout: post
title: idia inspiradas por applescript, kde e d-bus
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;"><em>Tudo come�ou numa tentativa que fiz para automatizar uma tarefa�- reiniciar o AirPort no MacOSX -�em 10 minutos no Google consegui as informa��es necess�rias para fazer um script na linguagem AppleScript. Isso me fez pensar em algumas coisas sobre a interatividade que obtemos nos ambientes atuais e as possibilidades nos ambientes livres. </em></p>
<p style="text-align: justify;"></p>
<p style="text-align: justify;">Veja um exemplo feito no <em><a href="http://developer.apple.com/applescript/" target="_blank">AppleScript</a></em> simples para mostrar a janela com as prefer�ncias de rede (<em>System Preferences -&gt; Network</em>).</p>

<h5>Nota: (1) se o voc� for testar e seu sistema estiver em Portugu�s, lembre-se de traduzir os nomes entre aspas. �(2) Para rodar os scripts � preciso marcar a op��o <em>Enable access for assistive Devices em System Preferences -&gt; Universal Access</em></h5>
<pre lang="applescript">tell application "System Preferences"
	activate
	set current pane to pane "com.apple.preference.network"
end tell</pre>
Para desligar/ligar o AirPort:
<pre lang="applescript">tell application "System Events"
	tell process "System Preferences"
		tell window "Network"
			tell group 1
				if (exists button "Turn Airport Off") then
					click button "Turn AirPort Off"
					delay 3
				end if
				if (exists button "Turn Airport On") then
					click button "Turn AirPort On"
				end if
			end tell
		end tell
	end tell
end tell</pre>
<p style="text-align: justify;">Veja que � uma tradu��o em palavras (praticamente verbos no imperativo) do que seria o processo feito no modo gr�fico.�Se voc�programa em Python, existe um <a href="http://aurelio.net/doc/as4pp.html" target="_blank">comparativo</a>.</p>
<p style="text-align: justify;"><strong>Ambientes livres</strong></p>
<p style="text-align: justify;">E � justamente com Python que vejo uma alternativa interessante para controlar as aplica��es como o <em>System Settings.�<span style="font-style: normal;">Talvez o jeito mais f�cil de fazer isso seria atrav�s de uma comunica��o IPC como o <a href="http://techbase.kde.org/Development/Tutorials/D-Bus/Introduction" target="_blank">D-BUS</a> . Inclusive o system settings � exportado em</span> org.kde.systemsettings<span style="font-style: normal;">.</span></em></p>

<pre>$ qdbus org.kde.systemsettings</pre>
<p style="text-align: justify;">Resumindo, o acesso pode<strong> n�o</strong> ser t�o f�cil quanto no <em>AppleScript </em>mas�o "meio" j� existe em ambiente gr�ficos tal como KDE e� GNOME. O Python lida muito bem com este tipo de comunica��o e � uma sa�da para quem est� procurando um jeito para controlar seu ambiente de forma automatizada.</p>
<p style="text-align: justify;"><strong>Futuro</strong></p>
<p style="text-align: justify;">Na minha opini�o h� uma defici�ncia para (A) pessoas leigas, se quiserem, controlar seus aplicativos de forma automatizada e (B) melhorar as formas de usabilidade nas interfaces <strong>j�</strong> existentes.</p>
<p style="text-align: justify;">Fico imaginando se n�o seria interessante um investimento (e pesquisa) para criar linguagens de programa��o que herdem constru��es da "fala" para acessar aplicativos, para no futuro utilizar da "voz" humana para controlar o computador.</p>
O software livre � um terreno vasto para esse tipo de experi�ncia. Cito algumas tecnologias que tornaria isso poss�vel:
<ul>
	<li><a href="http://dbus.freedesktop.org" target="_blank">D-bus</a> para comunica��o entre os aplicativos</li>
	<li><a href="http://www.python.org" target="_blank">Python</a> como linguagem de programa��o para construir as "amarras"</li>
	<li><a href="http://www.nltk.org" target="_blank">NTLK </a> (<em>N</em><em>atural Language Toolkit</em>) para processar a linguagem</li>
</ul>
Se voc� trabalhar com algum tipo de pesquisa na �rea ou tem experi�ncia, por favor, deixe um coment�rio.

Bom come�o de semana a todos.