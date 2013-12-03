---
layout: post
title: Stellaris EKK-LM3S9b96 Evaluation Kit (1)
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">O <a href="http://blogdoje.com.br/2010/01/29/texas-instruments-design-stellaris-2010-contest" target="_blank">blog do Jê</a> foi um dos canais brasileiros que anunciou o concurso promovido pela Texas Instruments e a revista Circuit Cellar. Como sempre tive curiosidade nos microcontroladores de 32bits da ARM resolvi me inscrever no concurso para <em>receber</em> o KIT. Com uma proposta semelhante (mas sem o concurso) a NXP, a um tempo atrás, distribuiu alguns microcontroladores da família LPC. Conheço muitos "hobbistas" que pediram as amostras mas assim que chegaram os custos para fazer uma placa (mesmo que um <em>design</em> simples para testar a funcionalidade) tornou o projeto inviável. A idéia do kit de desenvolvimento, na minha opinião, tende a popularizar melhor o uso (principalmente para quem gosta de fuçar).</p>
<a href="http://www.coding.com.br/wp-content/uploads/2010/04/4493235551_3214e1f7fd.jpg"><img class="aligncenter size-medium wp-image-865" title="Caixa com o kit" src="http://www.coding.com.br/wp-content/uploads/2010/04/4493235551_3214e1f7fd-300x225.jpg" alt="" width="300" height="225" /></a>Sinceramente já tinha esquecido da inscrição quando chegou na minha casa na semana passada... e só consegui fazer o <em>hands on</em> neste final de semana.
<p style="text-align: center;"><img class="aligncenter" title="Itens dentro da caixa" src="http://www.coding.com.br/wp-content/uploads/2010/04/4493464217_41d7caa412.jpg" alt="" width="500" height="375" /></p>
<p style="text-align: justify;">Veio com todas o itens para você começar a desenvolver, a placa principal com a MCU fabricada pela <a href="http://www.luminarymicro.com/" target="_blank">Luminary</a> é a maior na foto, sendo a outra basicamente a interface USB com o computador (utiliza o chip da FTDI). Imagino que seja possível aproveitar em outros projetos. No kit há essencialmente:</p>

<ul>
	<li>80-MHz LM3S9B96 MCU</li>
	<li>Ethernet MAC+PHY</li>
	<li>CAN</li>
	<li>USB OTG,</li>
	<li>SafeRTOS na ROM, com uma cópia limitada do Keil RealView Microcontroller Development Kit</li>
	<li>cables (USB e rede)</li>
	<li>CD com documentação e software</li>
	<li>Pendrive de 256MB</li>
</ul>
<p style="text-align: justify;">Vou descrever aqui as novidades que for aprendendo. A meta é testar no final de semana o SafeRTOS.  Acredito que a presença do PHY Ethernet vai permitir implementações interessantes. Se você tiver alguma idéia sugira nos comentários.</p>
<p style="text-align: justify;"></p>
<p style="text-align: justify;"></p>