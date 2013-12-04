---
layout: post
title: Bsico de ponteiros com o GDB
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Esse  um pequeno lembrete para quem quer pegar o conceito de ponteiro rpido.  to simples que nem programa direito voc vai precisar, s seguir sua intuio e o GDB ;-)</p>

<strong>1. Bsico</strong>

Vamos comear com um cdigo muito simples.

<pre lang="c">
#include <stdio.h>
int main(int argc, char *argv[]) {
int *ptr = NULL;
int variavel_A;
int variavel_B;
variavel_A = 5;
variavel_B = 18;
return 0;
}
</pre>
<p style="text-align: justify;">Usar o menor comando do GCC para compilar e linkar o programa. A sada (o executvel) chamar a.out, se voc quiser outro nome adicione "-o &lt;nome&gt;" no final do comando.</p>

<strong>gcc -ggdb basico.c </strong>
<p style="text-align: justify;">E iniciar o depurador, lembre-se que o texto em <span style="color: red; ">(vermelho)</span>  comentrio e <strong>negrito</strong>  um comando para voc digiar na CLI (<em>command-line interface</em>) do GDB.</p>

<div class="indent"><tt></tt>

<tt>maluta@coding ~ $ gdb -q a.out</tt>
<tt>(gdb) <strong>l</strong> <span style="color: red; ">(lista o cdigo)</span></tt>
<tt>1       #include &lt;stdio.h&gt;</tt>
<tt>2</tt>
<tt>3 </tt>
<tt>4       int main(int argc, char *argv[]) {</tt>
<tt>5</tt>
<tt>6               int *ptr = NULL;</tt>
<tt>7               int variavel_A;</tt>
<tt>8               int variavel_B;</tt>
<tt>9</tt>
<tt>10              variavel_A = 5;</tt>
<tt>(gdb)</tt>
<tt>11              variavel_B = 18;</tt>
<tt>12</tt>
<tt>13              return 0;</tt>
<tt>14</tt>
<tt>15      }</tt>
<tt>(gdb) <strong>break </strong>13  <span style="color: red; ">(inserir um breakpoint na linha 13)</span></tt>
<tt>Breakpoint 1 at 0x80483c6: file basico.c, line 13.</tt>

<tt>(gdb) <strong>r</strong> <span style="color: red; ">(run - inicia o programa)</span></tt>
<tt>Starting program: /home/maluta/a.out</tt>
<tt>Breakpoint 1, main () at basico.c:13</tt>
<tt>13              return 0;</tt>
<span style="color: red; "><tt>(Mostra o que tem na variavel_A)</tt></span>
<tt>(gdb) <strong>print</strong> variavel_A</tt>
<tt>$1 = 5</tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(Mostra o que tem na variavel_B)</tt></span><tt></tt>
<tt>(gdb) <strong>print</strong> variavel_B</tt>
<tt>$2 = 18</tt>
<span style="color: red; "><tt>(Imprime o contedo do endereo definido em ptr)</tt></span><tt></tt>
<tt>(gdb) <strong>print</strong> *ptr </tt>
<tt>Cannot access memory at address 0x0 <span style="color: red; ">(ooops... essa no  uma posio vlida!)</span></tt>
<tt>(gdb) <strong>print</strong> ptr <span style="color: red; "> (mas  claro que ptr guarda um valor...)</span></tt>
<tt>$3 = (int *) 0x0 <span style="color: red; ">(que  NULL)</span></tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(E qual o endereo da varivel_A?)</tt></span>
<tt>(gdb) <strong>print</strong> &amp;variavel_A</tt>
<tt>$4 = (int *) <span style="color: green; ">0xbfbc0ddc</span></tt>
<tt>(gdb) <strong>print</strong> *variavel_A <span style="color: red; ">(Podemos ver que no conseguimos acessar a variavel_A como um ponteiro pois ela guarda um endereo invlido)</span></tt>
<tt>Cannot access memory at address 0x5</tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(O endereo da varivel_B)</tt></span><tt></tt>
<tt>(gdb) <strong>print</strong> &amp;variavel_B</tt>
<tt>$5 = (int *) 0xbfbc0de0</tt>
<span style="color: red; "><tt>(Vamos fazer ptr apontar para a variavel_A)</tt></span><tt></tt>
<tt>(gdb) <strong>set</strong> ptr=<span style="color: green; ">0xbfbc0ddc</span> </tt>
<tt>(gdb) <strong>print</strong> *ptr <span style="color: red; ">(e mostrar o seu contedo)</span></tt>
<tt>$6 = 5</tt>
<span style="color: red; "><tt>(Vamos fazer ptr apontar para a variavel_B)</tt></span><tt></tt>
<tt>(gdb) <strong>set</strong> ptr=&amp;variavel_B</tt>
<tt>(gdb) <strong>print</strong> *ptr</tt>
<tt>$7 = 18</tt>
<tt>(gdb)</tt>
<tt></tt></div>

<strong>2. Intermedirio</strong>

Vamos dar mais um passo.

<!--start GeSHi-->
<pre lang="c">#include 
#include  /* malloc() */
#include  /* strncpy */
int main(int argc, char *argv[]) {

        char *nome;

        nome = malloc(10*sizeof(char));
        strncpy(nome,"tiago",5);
        return 0;
}</pre>
<tt>maluta@coding ~ $ gdb -q a.out</tt>
<tt>(gdb) <strong>l</strong></tt>
<tt>1       #include &lt;stdio.h&gt;</tt>
<tt>2       #include &lt;stdlib.h&gt; /* malloc() */</tt>
<tt>3       #include &lt;string.h&gt; /* strncpy */</tt>
<tt>4       int main(int argc, char *argv[]) {</tt>
<tt>5</tt>
<tt>6</tt>
<tt>7               char *nome;</tt>
<tt>8</tt>
<tt>9               nome = malloc(10*sizeof(char));</tt>
<tt>10</tt>
<tt>(gdb) <strong>break</strong> 9</tt>
<tt>Breakpoint 1 at 0x8048421: file intermediario.c, line 9.</tt>
<tt>(gdb) <strong>r</strong></tt>
<tt>Starting program: /home/maluta/a.out</tt>
<tt>Breakpoint 1, main () at basico.c:9</tt>
<tt>9               nome = malloc(10*sizeof(char));</tt>
<tt>(gdb) <strong>print</strong> nome</tt>
<tt>$1 = 0xb80b1190 "U\211WVS\207" <span style="color: red; ">(LIXO)</span></tt>
<tt>(gdb) <strong>n</strong> <span style="color: red; ">(next - executa a prxima instruo)</span></tt>
<tt>11              strncpy(nome,"tiago",5);</tt>
<tt>(gdb) <strong>n</strong></tt>
<tt>15              return 0;</tt>
<tt>(gdb) <strong>print</strong> nome <span style="color: red; ">(texto copiado)</span></tt>
<tt>$2 = 0x804b008 "tiago"</tt>
<tt>(gdb) <strong>x/5x</strong> nome <span style="color: red; ">(conteudo em hexa)</span></tt>
<tt>0x804b008:      0x74    0x69    0x61    0x67    0x6f</tt>
<tt>(gdb) <strong>x/5c</strong> nome <span style="color: red; ">(conteudo em ascii)</span></tt>
<tt>0x804b008:      116 't' 105 'i' 97 'a'  103 'g' 111 'o'</tt>
<span style="color: red; "><tt>(Vamos mudar a primeira letra da string)</tt></span><tt></tt>
<tt>(gdb) <strong>set</strong> {char}nome='T' </tt>
<tt>(gdb) <strong>x/5x</strong> nome</tt>
<tt>0x804b008:      0x54    0x69    0x61    0x67    0x6f</tt>
<tt>(gdb) <strong>x/5c</strong> nome</tt>
<tt>0x804b008:      84 'T'  105 'i' 97 'a'  103 'g' 111 'o'</tt>
<span style="color: red; "><tt>(Vamos colocar um espao em branco na segunda posio)</tt></span><tt></tt>
<tt>(gdb) <strong>set</strong> {char}(nome+1)=' ' <span style="color: red; ">(lembre-se que o ndice comea em zero)</span></tt>
<tt>(gdb) <strong>print</strong> nome</tt>
<tt>$11 = 0x804b008 "T ago"</tt>
<tt>(gdb) <strong>x/5x</strong> nome</tt>
<tt>0x804b008:      0x54    0x20    0x61    0x67    0x6f</tt>
<tt>(gdb) <strong>x/5c</strong> nome</tt>
<tt>0x804b008:      84 'T'  32 ' '  97 'a'  103 'g' 111 'o'</tt>
<tt> <span style="color: red; ">(Voc pode ver o contedo da varivel com deslocamento 'offset')</span></tt>
<tt>(gdb) <strong>print</strong> nome+3</tt>
<tt>$17 = 0x804b00b "go"</tt>
<tt></tt>
<p style="text-align: justify;">Meu amigo Antnio (aka John) fez um exemplo do uso de classes em C, vamos utiliz-lo por aqui. Para mostrar o ponteiro para funo, s vou adicionar uma funo/mtodo <em>subtraiMinhaClasse</em> no cdigo.</p>

<pre lang="c">#include 

struct MinhaClasse{
    int a;
    int b;
    int (*soma)();
};

int somaMinhaClasse(struct MinhaClasse *this){
    return (*this).a + (*this).b;
}

int subtraiMinhaClasse(struct MinhaClasse *this){
    return (*this).a - (*this).b;
}

void construtorMinhaClasse(struct MinhaClasse *this){
    this-&gt;soma = somaMinhaClasse;
}

int main(){

    int resposta;
    struct MinhaClasse objeto;
    construtorMinhaClasse(&amp;objeto);

    objeto.a = 33;
    objeto.b = 15;

    resposta = objeto.soma();

    printf("%i",resposta);

return 0;
}</pre>
<div class="indent"><tt></tt>

<tt>(gdb) <strong>break</strong> 34</tt>

<tt>Breakpoint 1 at 0x8048425: file john.c, line 34.</tt>

<tt>(gdb) <strong>r</strong></tt>

<tt>Starting program: /home/maluta/a.out</tt>

<tt>Breakpoint 1, main () at john.c:34</tt>

<tt>29              printf("%i",resposta);</tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(Vamos ver o que tem na struct)</tt></span><tt></tt>

<tt>(gdb) <strong>print</strong> objeto</tt>

<tt>$1 = {a = 33, b = 15, soma = 0x80483d0 &lt;somaMinhaClasse&gt;}</tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(Bem como o valor contido em resposta)</tt></span><tt></tt>

<tt>(gdb) <strong>print</strong> resposta</tt>

<tt>$2 = 48</tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(Qual o endereo da funo somaMinhaClasse?)</tt></span><tt></tt>

<tt>(gdb) <strong>print</strong> somaMinhaClasse</tt>

<tt>$3 = {int (struct MinhaClasse *)} 0x80483d0 &lt;somaMinhaClasse&gt;</tt></div>
<div class="indent"><span style="color: red; "><tt>(Que interessante... objeto.soma e somaMinhaClasse tem o mesmo endereo?)</tt></span><tt></tt>

<tt>(gdb) <strong>print</strong> objeto.soma</tt>

<tt>$4 = (int (*)()) 0x80483d0 &lt;somaMinhaClasse&gt;</tt></div>
<div class="indent"><span style="color: red; "><tt>(E a funo subtraiMinha classe est sozinha?)</tt></span><tt></tt>

<tt>(gdb) <strong>print</strong> subtraiMinhaClasse</tt>

<tt>$5 = {int (struct MinhaClasse *)} 0x80483e3 &lt;subtraiMinhaClasse&gt;</tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(Que tal conect-la a algum?)</tt></span><tt></tt>

<tt>(gdb) <strong>set</strong> objeto.soma=subtraiMinhaClasse</tt>

<span style="color: red; "><tt>(E lgico ver o resultado!)</tt></span><tt></tt>

<tt>(gdb) <strong>print</strong> objeto.soma()</tt>

<tt>$6 = 18</tt>

<span style="color: red; "><tt>(O novo par de objeto.soma ;-))</tt></span><tt></tt>

<tt>(gdb) <strong>print</strong> objeto.soma</tt>

<tt>$8 = (int (*)()) 0x80483e3 &lt;subtraiMinhaClasse&gt;</tt></div>
<tt>
</tt>
<div class="indent"><span style="color: red; "><tt>(No gostei! Quero voltar para o que tinha antes)</tt></span><tt></tt>

<tt>(gdb) <strong>set</strong> objeto.soma=somaMinhaClasse</tt>

<tt>(gdb) <strong>print</strong> objeto.soma()</tt>

<tt>$9 = 48</tt>

<tt></tt></div>
<!--closing page content-->