---
layout: post
title: Erros na Codecademy em Português
---

Em 2014 o [Programaê!](http://programae.org.br) começou a traduzir plataformas de ensino de programação para a língua portuguesa. Estão neste portfólio o Scratch, Code.org, o currículo de ciência da computação da Khan Academy bem como a **Codecademy**, na qual comentarei um pouco neste *post*.

Atualmente existem 6 cursos traduzidos dentro da Codecademy (e já temos um previsão de outros).

![](/images/cc_courses.png)

Depios da tradução ainda houve um momento de passar um *pente fino* para corrigir eventuais erros de tradução. Pessoalmente revisei o [curso de python](http://www.codecademy.com/pt-BR/tracks/python), na época detectei (e corrigi) MUITOS erros.

Os erros mais comuns eram:

- erros de sintaxe/concordância na descrição e instruções dos exercícios
- erros na verificação dos exercícios (ex. a inscrição pede para escrever ``print "Ola Mundo"`` e o algorimo que verifica espera ``print "Hello World"``)
- erros do tipo: *o código esta certo mas porque acusa erro?*

Recentemente revisitando os [fórums](http://www.codecademy.com/pt-BR/forums/python-beginner-pt-BR-dbiwk/0) da Codecademy notei muita gente reportando problemas. Aparentemente algum *deploy* ds CC quebrou as traduções.

Antes de continuar meu *post* eu peço encarecidamente: **REPORTEM os erros**.
Vamos fortalecer nossa comunidade, o Programaê! é um movimento, vamos construir um conteúdo de qualidade, sempre grátis, para todos.  

Usem o próprio fórum da Codecademy, a área de comentários aqui ou [twitter](http://www.twitter.com/maluta).

Dito isso, vou tentar ajudar os usuário a resolver um dos erros, que penso eu, ser o mais comum.

**O código esta certo mas porque acusa erro?**

A Codecademy utiliza um algoritmo baseado em expressões regulares e condicionais simples (``if``) para verificar se você acertou ou não.

A título de exemplo, na trilha de Python o exercicio [Um Dia no Supermercado (8/13)](http://www.codecademy.com/pt-BR/courses/python-beginner-pt-BR-dbiwk/1/3?curriculum_id=53594ed4fed2a85327000001) pede na descrição da atividade:

*Como no exemplo acima, exiba a chave juntamente com suas informações de preço e ações. Exiba a resposta no seguinte formato:*

{% highlight python %}
  apple
  price: 2
  stock: 0
{% endhighlight %}

*Como no exemplo acima, já que sabemos que os dicionários prices e stock têm as mesmas chaves, você pode acessar o dicionário stock enquanto está percorrendo prices.*

*Quando for exibir, você pode usar a sintaxe do exemplo acima.*

A saída correta:
![](/images/cc.png)

Agora imagine um simples espaço no primeiro ``print``...

![](/images/cc1.png)

Note que ocorre um erro por um simples espaço, a mesma coisa iria acontecer se eu trocasse a palavra.

Isso acontece pois o algoritmo que verifica se a saída esta correta (ou não) é amarrado com a palavra pré-definida. Segue o exemplo do código que verifica o exercício:

![](/images/cc2.png)

Portanto, minha dica é: façam os exercícios da Codecademy respeitando os nomes de variáveis e as frases definidas. Longe de ser o melhor dos mundo mas é o como a plataforma foi estruturada.

Mais dúvidas estou a disposição e reforço, por favor, **continuem reportando os problemas.**
