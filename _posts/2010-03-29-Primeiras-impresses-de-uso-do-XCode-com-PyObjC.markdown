---
layout: post
title: Primeiras impresses de uso do XCode com PyObjC
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Estou utilizando o Mac OS X a pouco tempo com a inten��o de aprender um pouco da programa��o de interface gr�ficas. Uma op��o � utilizar o Qt que � multi-plataforma, mas resolvi fazer um teste com o que a Apple tem a oferecer. Minha escolha inicial para pegar a "id�ia" foi partir de alguma coisa que eu j� sei, para isso escolhi o <em>binding</em> PyObjC para criar aplicativos utilizando Python.</p>
<p style="text-align: justify;">O primeiro problema que eu resolvi relativamente r�pido foi a quest�o dos templates para criar um novo projeto em PyObjC. A vers�o que utilizo do XCode (3.2.1) n�o instala automaticamente, siga os passos <a href="http://ioanna.me/2009/09/installing-pyobjc-xcode-templates-in-snow-leopard/" target="_blank">aqui</a>.</p>
<p style="text-align: justify;">Resolvi fazer um programa bem simples para converter um n�mero na base decimal para base hexadecimal. Isso em Python � feito com meia linha de c�digo, mas o objetivo aqui � aprender como os componentes gr�ficos s�o acessados no c�digo. Aprendi duas coisas importantes: <strong>outlets</strong> e <strong>actions</strong>.</p>
<p style="text-align: justify;">No Interface Builder assim como no Qt Designer n�o fazemos c�digo e sim a tela. Em alguns tutoriais voc� pode encontrar refer�ncia a interface gr�fica como um arquivo com a extens�o .nib contudo as vers�es mais novas possuem a extens�o .xib (procurando diferen�as, li que o .xib gera um XML ao passo que o .nib n�o)�<a href="http://www.coding.com.br/wp-content/uploads/2010/03/hex.png">
<img class="aligncenter size-full wp-image-813" title="hex" src="http://www.coding.com.br/wp-content/uploads/2010/03/hex.png" alt="" width="163" height="232" /></a></p>
O c�digo que ir� tratar dos componentes na janela � o arquivo AppDelegate (ex.: <em>NomeDoProjeto</em>AppDelegate.py). Na janela Library ( Tools -&gt; Library ) selecionamos a aba Classes e procuramos pela classe AppDelegate.
<center>
[caption id="attachment_814" align="aligncenter" width="248" caption="Acesso as duas edits"]<a href="http://www.coding.com.br/wp-content/uploads/2010/03/outlet.png"><img class="size-medium wp-image-814" title="outlet" src="http://www.coding.com.br/wp-content/uploads/2010/03/outlet-248x300.png" alt="" width="248" height="300" /></a>[/caption]
</center>
Observe que esse processo de cria��o da interface gr�fica no IB � independente da linguagem escolhida.
<center>
[caption id="attachment_815" align="aligncenter" width="249" caption="A action � equivalente ao SLOT() no Qt"]<a href="http://www.coding.com.br/wp-content/uploads/2010/03/action.png"><img class="size-medium wp-image-815" title="action" src="http://www.coding.com.br/wp-content/uploads/2010/03/action-249x300.png" alt="" width="249" height="300" /></a>[/caption]</center>
<p style="text-align: justify;">A parte das conex�es s�o feitas segurando o control e clicando no cubo azul (na janela MainMenu.xib) da classe AppDelagete e arrastando at� o componente que voc� deseja utilizar. Aten��o na ordem:</p>

<ul style="text-align: justify;">
	<li>Outlets das caixas de texto: �clique no cubo e arraste para o componente, para cada selecione o <em>outlet</em> apropriado.</li>
	<li>Action do bot�o: clique no bot�o e arraste para o cubo, selecione a <em>action</em> apropriada</li>
</ul>
<p style="text-align: justify;">A parte que e gastei um tempo foi para acessar os <em>outlets</em>, mas depois de ver a op��o <em>Write Update Class Files </em>o problema foi resolvido (se voc� j� escreveu alguma no c�digo na classe Int2HexAppDelegate.py opte pelo <em>Merge</em> sen�o pelo <em>Replace</em>)</p>
<p style="text-align: center;"><a href="http://www.coding.com.br/wp-content/uploads/2010/03/write.png"><img class="aligncenter size-medium wp-image-822" title="write" src="http://www.coding.com.br/wp-content/uploads/2010/03/write-179x300.png" alt="" width="179" height="300" /></a></p>

<pre lang="python">from Foundation import *
from AppKit import *
import objc
class Int2HexAppDelegate (NSObject):
    edit_hexa = objc.IBOutlet()
    edit_int = objc.IBOutlet()

    @objc.IBAction
    def converte_(self, sender):
	    valor_int = self.edit_int.intValue()
	    valor_hexa = hex(valor_int)
	    self.edit_hexa.setStringValue_(str(valor_hexa))</pre>
<p style="text-align: justify;">Esse c�digo � bem simples para mostrar o conceito e tamb�m porque eu por enquanto n�o saberia fazer nada muito mais complexo que isso :p</p>
<p style="text-align: justify;">
O acesso as caixas de texto � feita pelas vari�veis (outlet) <em>edit_hexa</em> e <em>edit_int</em> e a a��o converte_ (lembre-se que o converte: do ObjectiveC vira converte_ no Python)</p>
<p style="text-align: justify;">Fiz um screencast desse exemplo, dispon�vel no <a href="http://www.youtube.com/watch?v=GZ1du3x07JI" target="_blank">Youtube</a> (como estava testando um <em>trial</em> do programa desculpem pela marca d'agua no video, selecione a qualidade de 720p, depois descobri que o QuickTime faz screencast mas j� tinha feito :-( )</p>
Espero que ajude quem pretende come�ar.