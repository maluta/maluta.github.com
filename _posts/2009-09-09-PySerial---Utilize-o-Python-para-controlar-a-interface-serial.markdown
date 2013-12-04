---
layout: post
title: PySerial - Utilize o Python para controlar a interface serial
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Embora seja uma tecnologia antiga ainda  utilizada amplamente, muitos dos projetos eletrnicos no estilo "faa voc mesmo" utilizam o protocolo de comunicao serial. Este <em>post</em> mostra como  possvel (e fcil) utilizar a linguagem <a title="Site da linguagem Python" href="http://www.python.org" target="_blank">Python</a> para fazer a interface com a porta serial (RS232) seja no Windows, GNU/Linux, *BSD, Solaris, etc. Com o PySerial dentro de um sistema embarcado pode-se fazer coisas muito interessante como direcionamento do fluxo de dados e coleta de dados para depurao.</p>

<strong>1. Instalao</strong>
<p style="text-align: justify;">Consideraremos a utilizao algum sistema operacional GNU (com a linguagem Python instalada) para o desenvolvimento, a instalao do mdulo  feita atravs do gerenciador de pacotes da sua distribuio ou pelo <em>easy_install</em></p>

<pre>easy_install pyserial</pre>
<strong>2. Uso</strong>
<p style="text-align: justify;">Se voc no possuir onde testar utilize o prprio cabo serial: faa um curto entre os pinos 2 (RX) e 3 (TX).</p>
<p style="text-align: justify;">Abra um programa para acessar a serial como o <a href="http://www.jls-info.com/julien/linux/" target="_blank">gtkterm</a> (modo grfico) ou <a href="https://alioth.debian.org/projects/minicom/" target="_blank">minicom</a> (modo texto) e veja que o que voc digitar ir ecoar.  Para os exemplos utilizaremos o gtkterm e o primeiro ser para escrita.</p>

<pre>#!/usr/bin/python
import serial
ser = serial.Serial(0)	        # abre a primeira serial que encontrar
                                # (/dev/ttySX). No Windows seria a COMX.
print ser.portstr		# mostra a porta utilizada
ser.write("hello")	        # envia
ser.close()			# fecha a porta</pre>
<p style="text-align: justify;">Aps rodar esse exemplo voc ir ver no gtkterm o texto "hello". Agora vamos ver como fazer uma leitura:</p>

<pre>#!/usr/bin/python
import serial
ser = serial.Serial(0)
ser.read()			# espera 1 byte (um caracter)
ser.close()</pre>
<p style="text-align: justify;">O programa ficar travado esperando receber algum dado da serial (veja o parmetro timeout). Ao utilizar o gtkterm e o cabo em curto no ir funcionar muito bem para enviar muitos bytes (teste feito com o conversor USB/Serial), mas  possvel fazer a prova do conceito. Se voc digitar uma letra no gtkterm ir v-la na interface de linha de comando do Python.</p>

<strong>3. Parmetros</strong>
<p style="text-align: justify;">At agora no falamos dos parmetros da porta serial, eles vo depender muito do equipamento que voc ir se conectar. Por padro o construtor define os seguintes valores:</p>

<pre>ser = serial.Serial(
    port=None,			# nmero do <em>device</em>, a numerao comea no zero
 	               		# Se algo falhar, o usurio pode
                                # espeficiar a string do device (/dev/ttyX, COMX,
                                # etc). Se nada  especificado um objeto com a
                                # porta fechada e no configurada  criado.
    baudrate=9600,		# <em>baud rate</em>
    bytesize=EIGHTBITS,		# nmero de <em>databits</em>
    parity=PARITY_NONE,		# bit de paridade
    stopbits=STOPBITS_ONE,	# nmero de bits de parada 
    timeout=None,		# ajusta um timeout, coloque "None" para no haver
    xonxoff=0,			# ativa controle de fluxo por software
    rtscts=0,			# ativa controle de fluxo RTS/CTS
    interCharTimeout=None	# Inter-character timeout, "None" para desabilitar
)</pre>
<p style="text-align: justify;">Veja que se no preenchermos nada ele ir utilizar os valores padro. Pode-se ajustar os valores no construtor da classe ou ento separadamente, por exemplo, para reajustar o <em>timeout</em> faa:</p>

<pre style="text-align: justify;">ser.timeout=3	# Aguarda 3 segundos quando for fazer
                # um read() ou at completar o tamanho em bytes
                # especificado.</pre>
<p style="text-align: justify;">No mbito geral  importante definir os valores de <em>port</em>, <em>baudrate</em> e o <em>timeout</em>, embora em muitas aplicaes embarcadas e modens o acesso aos pinos de controle RTS/CTS so essenciais . Os mtodos mais populares para as instncias so:</p>

<pre># abre a porta serial
open()
# fecha a porta imediadamente
close()
# muda o baudrate
setBaudrate(baudrate)
# l "size" caracteres , por padro l 1 byte
read(size=1)
# escrever um dado na porta serial
write(s)
# limpa o buffer de entrada, desconsidera todo o contedo
flushInput()
# limpa o buffer da sada, interrompe a sada.
flushOutput()</pre>
Exemplo:
<pre>&gt;&gt;&gt; import serial
&gt;&gt;&gt; ser = serial.Serial(0)
&gt;&gt;&gt; ser
Serial(port='/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=None,
xonxoff=0, rtscts=0, dsrdtr=0)
&gt;&gt;&gt; print ser.isOpen()
True</pre>
<strong>4. Dicas</strong>
<p style="text-align: justify;">Estas dicas so arbitrrias, so pequenas partes que fui utilizando ao longo do tempo e tentei organiz-las aqui.</p>

<ul>
	<li style="text-align: justify;">Para enviar um contedo hexadecimal utilze \x, por exemplo, para enviar o caracter '1' e '2' faa ser.write('\x31\x32')</li>
</ul>
<ul>
	<li style="text-align: justify;"><a title="Exemplo de funes para converso de bases numricas" href="http://www.coding.com.br/wiki/BaseConversion" target="_blank">Converso de bases </a></li>
</ul>
<ul>
	<li>Pode-se converter para outras bases entre 2 e 36 utilizando int(), exemplo:</li>
</ul>
<pre style="padding-left: 30px;">&gt;&gt;&gt; print int('g',18)
16</pre>
<ul>
	<li style="text-align: justify;"> No GNU/Linux, se voc utilizar algum conversor USB/Serial e seu sistema produzir um erro ao tentar iniciar a porta pelo construtor  serial.Serial(0)   porqu o device /dev/ttyUSBX no foi encontrado, uma soluo  a abordagem abaixo.</li>
</ul>
<pre style="padding-left: 30px;">import serial
import glob

def scan():
    """busca por portas disponveis, retorna uma lista de dispositivos"""
    return glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyS*')

ser = serial.Serial(scan()[0])</pre>
<ul>
	<li style="text-align: justify;">Sobre os conversores USB/Serial: normalmente as distribuies entregam o Linux (kernel) com o suporte aos conversores seriais. Se o seu kernel no suportar ou voc tem alguma particularidade, veja no menu de configurao:</li>
</ul>
<pre style="padding-left: 30px;">Device Drivers  ---&gt;
        Character devices  ---&gt;
                Serial drivers  ---&gt;</pre>
<ul>
	<li>Utilize o PyQT ou PyGTK para incrementar a interface com o usurio.</li>
</ul>
<p style="text-align: justify;">Como uma aplicao  especfica para cada caso, preferiu-se no dar nenhum detalhe do uso particular, acredito que o objetivo  motivar o leitor a acessar a documentao disponvel e procurar fazer os prprios testes. Na referncia h bons exemplos e rapidamente voc ir fazer seus programas utilizando a serial. Com Python nem a imaginao  o limite ;-)</p>

<a title="Site do projeto PySerial " href="http://pyserial.wiki.sourceforge.net/pySerial" target="_blank">http://pyserial.wiki.sourceforge.net/pySerial</a>