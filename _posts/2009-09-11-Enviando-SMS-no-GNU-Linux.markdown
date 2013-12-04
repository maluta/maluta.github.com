---
layout: post
title: Enviando SMS no GNU/Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Essa semana vi no <a title="Post inspirador" href="http://mauromartins.wordpress.com/2009/09/08/mandar-sms-a-partir-do-excel/" target="_blank">blog</a> do Mauro Martins um <em>post</em> sobre mandar SMS a partir do Excel (recomendo ler lá antes). Fiquei curioso, mas por opção resolvi utilizar apenas o GNU/Linux. O exemplo a seguir pode ser feito utilizando qualquer sistema Linux, a linguagem Python (com o módulo do <a href="http://www.coding.com.br/programacao/pyserial-utilize-o-python-para-controlar-a-interface-serial/" target="_blank">PySerial</a> instalado) e um <span style="text-decoration: line-through;">celular</span> <em>smartphone</em> da Nokia (nesse caso um <a title="N95 specs" href="http://www.gsmarena.com/nokia_n95-1716.php" target="_blank">N95</a>). O primeiro passo foi conectar o cabo USB e escolher o modo <strong>PC Suite</strong>.</p>
<p style="text-align: justify;">No terminal:</p>

<pre># lsusb | grep Nokia
Bus 005 Device 004: ID 0421:04f0 Nokia Mobile Phone</pre>
<p style="text-align: justify;">É preciso carregar os módulos necessários, se você precisar compilar o kernel são as opções CONFIG_USB_ACM e CONFIG_USB_SERIAL do .config</p>

<pre># modprobe cdc-acm
# modprobe usbserial vendor=0x0421 product=0x04f0</pre>
<p style="text-align: justify;">Observe que os valores dos parametros do módulo usbserial são obtidos através do comando lsusb. A partir desse ponto será criado um <em>device node</em> referenciado por /dev/ttyACM0. O código é bem simples, aonde apenas instanciamos um objeto da classe PySerial e utilizamos os métodos de escrita e leitura.</p>

<pre lang="python">import serial
ser = serial.Serial()
ser.port='/dev/ttyACM0'
ser.baudrate=19200
ser.rtscts=1
ser.timeout=3
ser.open()</pre>
<p style="text-align: justify;">Depois foi apenas usar os métodos write() e read() para fazer a prova do conceito. Como eu não sabia a quantidade de bytes a serem recebidos "chutei" um valor (10 bytes) e especifiquei um <em>timeout</em> para sair.</p>

<pre lang="python">ser.write('AT'+'\x0d\x0a') # AT
ser.read(10)</pre>
<p style="text-align: justify;">O exemplo de envio de um SMS que o Mauro apresentou pode ser feito dessa forma, lembrando que a extensão '\x0d\x0a' é o valor hexadecimal para o terminador de linha (o equivalente a pressionar [ENTER]).</p>

<pre lang="python">ser.write('AT+CMGF=1'+'\x0d\x0a')
time.sleep(2)
ser.write('AT+CMGS="0XXYYYYYYYY"'+'\x0d\x0a')
time.sleep(2)
ser.write('www.coding.com.br'+'\x0d\x0a\x1a')
 # envia a mensagem (www.coding.com.br) para o número definido</pre>
<p style="text-align: justify;">Meus primeiros testes só funcionaram quando dei um atraso (não se esqueça do <em>import time</em>) entre cada comando, abritrariamente escolhi 2 segundos, mas acredito que esse valor possa ser menor (fiz testes e funcionou). Passei uma boa parte da noite experimentando diversos comandos AT que encontrei no <a title="Lista de comandos AT (em inglês)" href="http://sw.nokia.com/id/95672052-6c77-488d-a055-acef77e4cdc5/AT_Command_Set_For_Nokia_GSM_And_WCDMA_Products_v1_2_en.pdf" target="_blank">manual</a>, os comandos de faziam a requisição de alguma informação: nível do sinal, número de série, fabricante, etc funcionaram, mas quando tentei fazer uma requisição da lista de contatos ou das mensagens SMS não obtive sucesso (mas é claro que fiz testes rápidos sem dar atenção merecida a documentação).</p>
<p style="text-align: justify;">Uma solução para fazer o equivalente no Excel é exportar a planilha no formato <a title="Explicação da Wikipedia sobre o fomarto CSV" href="http://pt.wikipedia.org/wiki/Comma-separated_values" target="_blank">CSV</a> e fazer um parser (lembrando que o Python já tem um <a href="http://docs.python.org/library/csv" target="_blank">módulo</a> pronto que faz isso) ou então até mesmo fazer um<em> plug-in</em> para o OpenOffice ;-)</p>