---
layout: post
title: Resumindo histórico de conversas no WhatsApp com LLMs
desc: 
proj-url:
proj-num: 01
draft: false
---

### Sumarizando Conversas no WhatsApp com Inteligência Artificial

*Como eu faço para gerar um resumo de conversas no WhatsApp?*

**1. Extração das Conversas**

Inicialmente, é preciso exportar a conversa desejada diretamente do aplicativo do WhatsApp. 

Para tal, acesse o menu através de `⋮ → Mais opções → Mais → Exportar conversa` para obter o arquivo com o histórico de mensagens. O histórico da sua conversa será enviado em formato .zip e pode ser encaminhado por diferentes meios, eu geralmente tenho anexado a um e-mail.

<iframe width="560" height="315" src="https://www.youtube.com/embed/BekPIIZ0o5g?si=m2bHkJmRcLCZrAIB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Veja aqui mais detalhes de [como fazer](https://faq.whatsapp.com/1180414079177245/) esse processo.


**1.1 Segmentação do histórico** (Opcional)

Para concentrar em uma janela de tempo específica, você pode editar o arquivo texto com o histórico da conversa.

No meu caso, eu utilizo um script em Python que lê o conteúdo exportado e cria um novo arquivo contendo apenas as mensagens de um período pré-determinado, como os últimos 7 dias. Embora seja possível "pedir" para o LLM fazer essa segmentação, essa etapa é particularmente é útil para "economizar tokens" e focar a análise em dados mais relevantes ou recentes.


**2. Análise das Mensagens usando IA**

Depois de exportar o arquivo, eu inicio o processo de análise em si. Se for a primeira vez, será um processo é bastante interativo, com várias interações a partir de um prompt inicial, até alcançar o resultado ideal.

> Veja um exemplo de [prompt](https://docs.google.com/document/d/1epgEfimlHJHnlZtCizDTGm6NrDS-H3vgnnJjysuaOkY/edit) que uso para sumarizar um grupo que fala sobre IA e Educação.

Algumas notas:

- Com base nos testes realizados, recomendo a utilização de modelos avançados como o GPT-4 ou Gemini 1.5. Estes modelos possuem maior capacidade para processar e compreender o contexto das conversas, o que facilita uma análise mais detalhada e a geração de insights significativos. 

- Para lidar com históricos com muitas mensagens, recomendo o uso do AI Studio ([aistudio.google.com](https://aistudio.google.com)). Este serviço (até então gratuito) é um dos poucos que oferece uma interface simples e eficaz para trabalhar com grandes janelas de contexto, suportando até 1 milhão de tokens. *Nota: Nos meus testes tenho gostado dos resutaldos usando o Gemini 1.5 Pro.*


**3. Compartilhamento dos Resultados**

Após a análise, faço as edições necessárias nos resumos gerados, dependdo do lugar onde eu vou postar eu faço ajustes para formatar o texto em markdown, HTML ou outro formato.

> Veja um [exemplo](https://sites.google.com/view/aprendizados-ia-educacao/home/semana-2705-0306) usando o Google Sites a partir do [prompt](https://docs.google.com/document/d/1epgEfimlHJHnlZtCizDTGm6NrDS-H3vgnnJjysuaOkY/edit) mencionado anteriormente.