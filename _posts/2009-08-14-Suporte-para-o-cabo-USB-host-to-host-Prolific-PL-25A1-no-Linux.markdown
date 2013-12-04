---
layout: post
title: Suporte para o cabo USB host-to-host Prolific (PL-25A1) no Linux
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">O protocolo USB estabelece um padro mestre-escravo de comunicao, de modo que uma comunicao entre dois <em>hosts</em> (ex.: computadores PC) atravs de um cabo ponto-a-ponto no funcionar. Para resolver, existem cabos conversores (comercialmente j encontrei nomes como uplink, netlink, etc) que fazem esta adaptao.</p>
<p style="text-align: justify;">Um dos controladores encontrados nestes cabos  o <a title="PL 25A1" href="http://www.prolific.com.tw/eng/files/PL-25A1%20Product%20Brochure%20101306.pdf" target="_blank">PL-25A1</a> da <a href="http://www.prolific.com.tw/" target="_blank">Prolific</a> que est presente em diversos modelos. Nos sistemas GNU/Linux h um mdulo (plusb.ko) que ainda <strong>no</strong> d suporte, mas j existe o <a title="Patch para cabos com o controlador PL-25A1" href="http://www.mail-archive.com/netdev@vger.kernel.org/msg61926.html" target="_blank">patch</a> (se quiser o arquivo j alterado clique <a href="http://www.coding.com.br/wiki/Prolific25A1" target="_blank">aqui</a>). Com o cabo conectado a porta USB veja qual o fabricante.</p>

<pre style="text-align: justify;"># lsusb
Bus 001 Device 002: ID 067b:25a1 Prolific Technology, Inc. PL25A1 Host-Host Bridge</pre>
Meus testes foram usando o Linux 2.6.29.6-217.2.3.fc11.i586 (Fedora 11). Para instalar o novo mdulo, o primeiro passo  renomear o antigo:
<pre># cd /lib/modules/`uname -r`/kernel/drivers/net/usb/
# mv plusb.ko plusb.ko.orig</pre>
Na pasta onde est o cdigo-fonte (plusb.c) compile e carrege o mdulo no sistema.
<pre style="text-align: justify;"># make -C /lib/modules/`uname -r`/build M=`pwd` modules
# insmod plusb.ko</pre>
<p style="text-align: justify;"></p>
<p style="text-align: justify;">Uma vez que o mdulo esteja funcionando, voc ter uma nova interface de rede usbX (para ver utilize ifconfig -a). Para enviar e recever pacotes, escolha um endereo de IP para os <em>endpoints</em> e comece a utilizar normalmente.</p>

<pre style="text-align: justify;">usb0 Link encap:Ethernet HWaddr EE:08:2C:4C:79:5B 
          inet addr:192.168.0.10 Bcast:192.168.0.255 Mask:255.255.255.0
          inet6 addr: fe80::ec08:2cff:fe4c:795b/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST MTU:1500 Metric:1
          RX packets:94 errors:0 dropped:0 overruns:0 frame:0
          TX packets:63 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:12458 (12.1 KiB) TX bytes:11304 (11.0 KiB)</pre>
<p style="text-align: justify;">Acredito que as prximas verses do <em>kernel</em> fornecido pelas distribuies j iro trazer este suporte (quem ver o <em>patch</em> constatar que  mnima as alteraes necessrias).</p>

<p style="text-align: justify;">Este cabo custa em mdia R$ 70,00   bem til para transferir dados entre dois computadores quando no h interface de rede disponvel. Ainda no pesquisei os tipos de transferncias que o cabo permite, especialmente a transferncia  iscrona<em>.
</em>