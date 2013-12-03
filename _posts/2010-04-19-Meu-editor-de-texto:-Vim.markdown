---
layout: post
title: Meu editor de texto: Vim
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">O <a href="http://www.vim.org" target="_blank">vim</a> é a um bom tempo meu principal editor para a programação.  Além de utilizá-lo para todas as operações "básicas" de um editor de texto, vou apresentar rapidamente algumas coisas que fazem ele tão útil para mim.</p>
<strong>1) Integração com  o ctags </strong>Ctrl+] e Ctrl+t
<p style="padding-left: 30px; text-align: justify;">Muito útil para projetos com vários arquivos onde é preciso navegar pela definições. Primeiro é preciso gerar a lista de <em>tags</em> do diretório com  o código-fonte.</p>

<pre style="padding-left: 30px;">ctags -R .</pre>
<p style="padding-left: 30px;">Se uma definição se encontra em mais de um lugar, posiciono o cursor no nome da função/definição e entro com o comando <em>:ts</em> ao invés do <em>Ctrl+]</em></p>
<strong>2) Tabs </strong>(:tabe) <strong>e split </strong>(:split ou :vsplit)
<p style="padding-left: 30px;">Utilizo para abrir vários arquivos em abas. Para movimentar entre ele utilizo "&lt;n&gt;gt" ou simplemente "<em>gt</em>". Já o [v]split divide a tela, para alterar o foco uso o comando <em>Ctrl+w w</em></p>
<p style="padding-left: 30px;"><a href="http://www.coding.com.br/wp-content/uploads/2010/04/vim-tabs.png"><img class="aligncenter size-full wp-image-914" src="http://www.coding.com.br/wp-content/uploads/2010/04/vim-tabs.png" alt="" width="293" height="132" /></a></p>
<strong>3) Shell (:sh)</strong>
<p style="padding-left: 30px;">Acessar a <em>shell</em> do sistema sem fechar o editor, retorno digitando <em>exit</em></p>
<strong>4) Integração com o make </strong>(:make) <strong>e grep</strong> (:grep)

<strong>5) Tabs remotas</strong>
<p style="padding-left: 30px; text-align: justify;">Este recurso só é ativado se o vim foi compilado com o parâmetro <em>clientserver</em> (no caso do Gentoo é a opção <em>vim-with-x</em>). Permite que eu abra uma única instância do vim e a medida que for abrindo os arquivos eles são visualizados nessa instância. Veja como é simples:</p>
<p style="padding-left: 30px;">Cria-se um servidor:</p>

<pre style="padding-left: 30px;">vim --servername coding</pre>
<p style="padding-left: 30px;">Verifica-se os servidores disponíveis:</p>

<pre style="padding-left: 30px;">vim --serverlist
CODING</pre>
<p style="padding-left: 30px;">Aproveitando, um <em>alia</em>s para facilitar a vida:</p>

<pre style="padding-left: 30px;">alias v="vim --servername CODING --remote-tab"</pre>
<p style="padding-left: 30px;">Depois é editar o arquivo normalmente:</p>

<pre style="padding-left: 30px;">v bla.c</pre>
<strong>6) Lista de definições</strong>
<p style="padding-left: 30px;">Uma pequena personalização no arquivo ~/.vimrc e um <em>plug-in </em>chamado <a href="http://vim-taglist.sourceforge.net/" target="_blank">taglist</a></p>

<pre style="padding-left: 30px;">let Tlist_Ctags_Cmd="/usr/bin/ctags"
let Tlist_WinWidth = 50
map &lt;F5&gt; :TlistToogle&lt;cr&gt;</pre>
<p style="padding-left: 30px;">Os comandos são auto-explicativos. O &lt;F5&gt; alterna a visibilidade da lista.</p>
<a href="http://www.coding.com.br/wp-content/uploads/2010/04/vim-tlist.png">
<img class="aligncenter size-full wp-image-915" src="http://www.coding.com.br/wp-content/uploads/2010/04/vim-tlist.png" alt="" width="535" height="430" /></a>
<p style="text-align: justify;">Lembre-se: toda documentação do vim está acessível no próprio editor, basta <em>:help comando</em>. É importante ler a documentação para aprender. Minha intenção não é apresentar todos os modos de utilização, o objetivo deste <em>post</em> é apenas mostrar algumas possibilidades de uso.</p>
:wq