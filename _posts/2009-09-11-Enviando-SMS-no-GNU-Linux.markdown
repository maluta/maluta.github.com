---
layout: post
title: Enviando SMS no GNU/Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Essa semana vi no <a title="Post inspirador" href="http://mauromartins.wordpress.com/2009/09/08/mandar-sms-a-partir-do-excel/" target="_blank">blog</a> do Mauro Martins um <em>post</em> sobre mandar SMS a partir do Excel (recomendo ler l antes). Fiquei curioso, mas por opo resolvi utilizar apenas o GNU/Linux. O exemplo a seguir pode ser feito utilizando qualquer sistema Linux, a linguagem Python (com o mdulo do <a href="http://www.coding.com.br/programacao/pyserial-utilize-o-python-para-controlar-a-interface-serial/" target="_blank">PySerial</a> instalado) e um <span style="text-decoration: line-through;">celular</span> <em>smartphone</em> da Nokia (nesse caso um <a title="N95 specs" href="http://www.gsmarena.com/nokia_n95-1716.php" target="_blank">N95</a>). O primeiro passo foi conectar o cabo USB e escolher o modo <strong>PC Suite</strong>.</p>
<p style="text-align: justify;">No terminal:</p>

<pre># lsusb | grep Nokia
Bus 005 Device 004: ID 0421:04f0 Nokia Mobile Phone</pre>
<p style="text-align: justify;"> preciso carregar os mdulos necessrios, se voc precisar compilar o kernel so as opes CONFIG_USB_ACM e CONFIG_USB_SERIAL do .config</p>

<pre># modprobe cdc-acm
# modprobe usbserial vendor=0x0421 product=0x04f0</pre>
<p style="text-align: justify;">Observe que os valores dos parametros do mdulo usbserial so obtidos atravs do comando lsusb. A partir desse ponto ser criado um <em>device node</em> referenciado por /dev/ttyACM0. O cdigo  bem simples, aonde apenas instanciamos um objeto da classe PySerial e utilizamos os mtodos de escrita e leitura.</p>

<pre lang="python">import serial
ser = serial.Serial()
ser.port='/dev/ttyACM0'
ser.baudrate=19200
ser.rtscts=1
ser.timeout=3
ser.open()</pre>
<p style="text-align: justify;">Depois foi apenas usar os mtodos write() e read() para fazer a prova do conceito. Como eu no sabia a quantidade de bytes a serem recebidos "chutei" um valor (10 bytes) e especifiquei um <em>timeout</em> para sair.</p>

<pre lang="python">ser.write('AT'+'\x0d\x0a') # AT
ser.read(10)</pre>
<p style="text-align: justify;">O exemplo de envio de um SMS que o Mauro apresentou pode ser feito dessa forma, lembrando que a extenso '\x0d\x0a'  o valor hexadecimal para o terminador de linha (o equivalente a pressionar [ENTER]).</p>

<pre lang="python">ser.write('AT+CMGF=1'+'\x0d\x0a')
time.sleep(2)
ser.write('AT+CMGS="0XXYYYYYYYY"'+'\x0d\x0a')
time.sleep(2)
ser.write('www.coding.com.br'+'\x0d\x0a\x1a')
 # envia a mensagem (www.coding.com.br) para o nmero definido</pre>
<p style="text-align: justify;">Meus primeiros testes s funcionaram quando dei um atraso (no se esquea do <em>import time</em>) entre cada comando, abritrariamente escolhi 2 segundos, mas acredito que esse valor possa ser menor (fiz testes e funcionou). Passei uma boa parte da noite experimentando diversos comandos AT que encontrei no <a title="Lista de comandos AT (em ingls)" href="http://sw.nokia.com/id/95672052-6c77-488d-a055-acef77e4cdc5/AT_Command_Set_For_Nokia_GSM_And_WCDMA_Products_v1_2_en.pdf" target="_blank">manual</a>, os comandos de faziam a requisio de alguma informao: nvel do sinal, nmero de srie, fabricante, etc funcionaram, mas quando tentei fazer uma requisio da lista de contatos ou das mensagens SMS no obtive sucesso (mas  claro que fiz testes rpidos sem dar ateno merecida a documentao).</p>
<p style="text-align: justify;">Uma soluo para fazer o equivalente no Excel  exportar a planilha no formato <a title="Explicao da Wikipedia sobre o fomarto CSV" href="http://pt.wikipedia.org/wiki/Comma-separated_values" target="_blank">CSV</a> e fazer um parser (lembrando que o Python j tem um <a href="http://docs.python.org/library/csv" target="_blank">mdulo</a> pronto que faz isso) ou ento at mesmo fazer um<em> plug-in</em> para o OpenOffice ;-)</p>