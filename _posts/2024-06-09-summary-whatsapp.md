---
layout: post
title: Sumarizando conversar no Whatsapp com IA
desc: 
proj-url:
proj-num: 01
draft: false
---

### Sumarizando Conversas no WhatsApp com Inteligência Artificial

*Como eu faço para gerar um resumo de conversas no WhatsApp?*

**1. Extração da Conversa**

Inicialmente, é preciso exportar a conversa desejada diretamente do aplicativo do WhatsApp. 

Para tal, acesse o menu através de `⋮ → Mais opções → Mais → Exportar conversa` para obter o arquivo com o histórico de mensagens. O histórico da sua conversa será enviado em formato .zip e anexado a um e-mail.

Veja aqui mais detalhes de [como fazer](https://faq.whatsapp.com/1180414079177245/) esse processo.


**1.1 Segmentação** (Opcional)

Para focar em uma janela de tempo específica, utilizo um script em Python que me permite criar um novo arquivo contendo apenas as mensagens de um período determinado, como os últimos 7 dias. Embora seja possível "pedir" para o LLM fazer essa segmentação, essa etapa é particularmente é útil para "economizar tokens" e focar a análise em dados mais relevantes ou recentes.


**2. Análise das Mensagens**

Depois de exportar o arquivo, eu inicio várias interações a partir de um prompt inicial. Se for a primeira vez, será um processo é bastante interativo, envolvendo diversos ajustes até alcançar o resultado ideal.

> Veja um exemplo de [prompt](https://docs.google.com/document/d/1epgEfimlHJHnlZtCizDTGm6NrDS-H3vgnnJjysuaOkY/edit) que uso para sumarizar um grupo que fala sobre IA e Educação.

Algumas notas:

- Com base nos testes realizados, recomendo a utilização de modelos avançados como o GPT-4 ou Gemini 1.5. Estes modelos possuem maior capacidade para processar e compreender o contexto das conversas, o que facilita uma análise mais detalhada e a geração de insights significativos.

Para lidar com históricos de dados extensos, recomendo o uso do AI Studio ([aistudio.google.com](https://aistudio.google.com)). Este serviço é um dos poucos que oferece uma interface simples e eficaz para trabalhar com grandes janelas de contexto, suportando até 1 milhão de tokens.


**3. Compartilhamento dos Resultados**

Após a análise, faço as edições necessárias nos resumos gerados, dependdo do lugar onde eu vou postar eu faço ajustes para formatar o texto em markdown, HTML ou outro formato.
