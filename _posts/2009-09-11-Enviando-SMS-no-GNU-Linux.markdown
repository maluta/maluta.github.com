---
layout: post
title: Enviando SMS no GNU/Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Essa semana vi no <a title="Post inspirador" href="http://mauromartins.wordpress.com/2009/09/08/mandar-sms-a-partir-do-excel/" target="_blank">blog</a> do Mauro Martins um <em>post</em> sobre mandar SMS a partir do Excel (recomendo ler l� antes). Fiquei curioso, mas por op��o resolvi utilizar apenas o GNU/Linux. O exemplo a seguir pode ser feito utilizando qualquer sistema Linux, a linguagem Python (com o m�dulo do <a href="http://www.coding.com.br/programacao/pyserial-utilize-o-python-para-controlar-a-interface-serial/" target="_blank">PySerial</a> instalado) e um <span style="text-decoration: line-through;">celular</span> <em>smartphone</em> da Nokia (nesse caso um <a title="N95 specs" href="http://www.gsmarena.com/nokia_n95-1716.php" target="_blank">N95</a>). O primeiro passo foi conectar o cabo USB e escolher o modo <strong>PC Suite</strong>.</p>
<p style="text-align: justify;">No terminal:</p>

<pre># lsusb | grep Nokia
Bus 005 Device 004: ID 0421:04f0 Nokia Mobile Phone</pre>
<p style="text-align: justify;">� preciso carregar os m�dulos necess�rios, se voc� precisar compilar o kernel s�o as op��es CONFIG_USB_ACM e CONFIG_USB_SERIAL do .config</p>

<pre># modprobe cdc-acm
# modprobe usbserial vendor=0x0421 product=0x04f0</pre>
<p style="text-align: justify;">Observe que os valores dos parametros do m�dulo usbserial s�o obtidos atrav�s do comando lsusb. A partir desse ponto ser� criado um <em>device node</em> referenciado por /dev/ttyACM0. O c�digo � bem simples, aonde apenas instanciamos um objeto da classe PySerial e utilizamos os m�todos de escrita e leitura.</p>

<pre lang="python">import serial
ser = serial.Serial()
ser.port='/dev/ttyACM0'
ser.baudrate=19200
ser.rtscts=1
ser.timeout=3
ser.open()</pre>
<p style="text-align: justify;">Depois foi apenas usar os m�todos write() e read() para fazer a prova do conceito. Como eu n�o sabia a quantidade de bytes a serem recebidos "chutei" um valor (10 bytes) e especifiquei um <em>timeout</em> para sair.</p>

<pre lang="python">ser.write('AT'+'\x0d\x0a') # AT
ser.read(10)</pre>
<p style="text-align: justify;">O exemplo de envio de um SMS que o Mauro apresentou pode ser feito dessa forma, lembrando que a extens�o '\x0d\x0a' � o valor hexadecimal para o terminador de linha (o equivalente a pressionar [ENTER]).</p>

<pre lang="python">ser.write('AT+CMGF=1'+'\x0d\x0a')
time.sleep(2)
ser.write('AT+CMGS="0XXYYYYYYYY"'+'\x0d\x0a')
time.sleep(2)
ser.write('www.coding.com.br'+'\x0d\x0a\x1a')
 # envia a mensagem (www.coding.com.br) para o n�mero definido</pre>
<p style="text-align: justify;">Meus primeiros testes s� funcionaram quando dei um atraso (n�o se esque�a do <em>import time</em>) entre cada comando, abritrariamente escolhi 2 segundos, mas acredito que esse valor possa ser menor (fiz testes e funcionou). Passei uma boa parte da noite experimentando diversos comandos AT que encontrei no <a title="Lista de comandos AT (em ingl�s)" href="http://sw.nokia.com/id/95672052-6c77-488d-a055-acef77e4cdc5/AT_Command_Set_For_Nokia_GSM_And_WCDMA_Products_v1_2_en.pdf" target="_blank">manual</a>, os comandos de faziam a requisi��o de alguma informa��o: n�vel do sinal, n�mero de s�rie, fabricante, etc funcionaram, mas quando tentei fazer uma requisi��o da lista de contatos ou das mensagens SMS n�o obtive sucesso (mas � claro que fiz testes r�pidos sem dar aten��o merecida a documenta��o).</p>
<p style="text-align: justify;">Uma solu��o para fazer o equivalente no Excel � exportar a planilha no formato <a title="Explica��o da Wikipedia sobre o fomarto CSV" href="http://pt.wikipedia.org/wiki/Comma-separated_values" target="_blank">CSV</a> e fazer um parser (lembrando que o Python j� tem um <a href="http://docs.python.org/library/csv" target="_blank">m�dulo</a> pronto que faz isso) ou ent�o at� mesmo fazer um<em> plug-in</em> para o OpenOffice ;-)</p>