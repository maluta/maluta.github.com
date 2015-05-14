---
layout: post
title: Erros na Codecademy em Português
---

Desde do ano passado o [Programaê!](http://programae.org.br) esta conduzindo esforços para tradução de plataformas de ensino de programação para a língua portuguesa. A **Codecademy** é um dos parceiros de conteúdo do Programaê! e atualmente existem 6 cursos traduzidos.

![](/images/cc_courses.png)

Em meados de 2014 passamos um *pente fino* para corrigir eventuais erros de tradução na plataforma. Pessoalmente revisei o [curso de python](http://www.codecademy.com/pt-BR/tracks/python), na época detectei (e corrigi) MUITOS erros.

Contudo, recentemente navegando pelos [fórums](http://www.codecademy.com/pt-BR/forums/python-beginner-pt-BR-dbiwk/0) da Codecademy ainda vejo muita gente reportando problemas bem como em outras redes. Aparentemente algum deploy quebrou as traduções.

Antes de continuar meu *post* eu peço encarecidamente: **reportem os erros**.
Usem o próprio fórum da Codecademy, a área de comentários deste post ou até mesmo me contactar no [twitter](http://www.twitter.com/maluta).

**Dicas**

A Codecademy utiliza um algoritmo baseado em expressao regulares para verificar se você acertou ou não. Isso gera uma série de problemas do tipo: *"meu código esta certo mas ainda sim acusa erro!"*

A título de exemplo, na trilha de Python o exercicio [Um Dia no Supermercado (8/13)](http://www.codecademy.com/pt-BR/courses/python-beginner-pt-BR-dbiwk/1/3?curriculum_id=53594ed4fed2a85327000001) a descrição da atividade diz:

Como no exemplo acima, exiba a chave juntamente com suas informações de preço e ações. Exiba a resposta no seguinte formato:

{% highlight python %}
  apple
  price: 2
  stock: 0
{% endhighlight %}

Como no exemplo acima, já que sabemos que os dicionários prices e stock têm as mesmas chaves, você pode acessar o dicionário stock enquanto está percorrendo prices.

**Quando for exibir, você pode usar a sintaxe do exemplo acima.**

A saida correta:
![](/images/cc.png)

Agora imagine eu dê um simples espaço no primeiro ``print``.

![](/images/cc1.png)

Note que já foi acusado um erro por um simples espaço, a mesma coisa iria acontecer se eu trocasse a palavra.

Isso acontece pois o algorítmo que verifica se a saida esta correta (ou não) depente do uso da palavra correta para validar o exercício.

![](/images/cc2.png)


Portanto, façam os exercícios da Codecademy respeitando os nomes de variáveis e as frases definidas. Não é o melhor dos mundo mas é o como a plataforma foi estruturada. 

E novamente, por favor, continuem reportando os problemas.
