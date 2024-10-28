---
layout: post
title: Strava Analysis 
desc: 
proj-url:
proj-num: 01
draft: false
---

Recentemente eu [publiquei no meu LinkedIn um post](https://www.linkedin.com/posts/maluta_explorando-meus-dados-de-corrida-no-strava-activity-7256346546974171137-bTp6?utm_source=share&utm_medium=member_desktop) com uma animação sobre o uso dos meus tênis de corrida ao longo do tempo. 

<iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7256346498265714689?compact=1" height="399" width="710" frameborder="0" allowfullscreen="" title="Embedded post"></iframe>

Abaixo, vou resumir minhas etapa desse processo.

# Extraindo os dados 

A primeira coisa que fiz foi extrair os dados. Embora o Strava [acesso via API](https://developers.strava.com/docs/reference/), esse processo pode ser mais complexo. Para esta análise, optei por exportar meus dados diretamente do Strava, o que é um método mais simples e atendeu minhas necessidades.

Para exportar você precisa acessar o link [strava.com/athlete/delete_your_account](https://www.strava.com/athlete/delete_your_account) e fazer a solicitação dos seus dados. 

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-export.png)

Aguarde até receber um e-mail na sua `Your Strava archive is ready for download` (se não encontrar, tente filtrar pelo e-mail `no-reply@strava.com`)

O arquivo final é um .zip com os seguintes arquivos:

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-export-files.png)


# Explorando os dados com código

Todo código que utilizei pode ser [acessado aqui](https://github.com/maluta/maluta.github.com/blob/master/labs/strava/Strava%20Analysis.ipynb)

Para facilitar eu usei a linguagem Python via [Jupyter Notebok](https://jupyter.org/) para fazer as análises a partir do arquivo `activities.csv`

```
df = pd.read_csv('activities.csv')
df.columns
```

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-columns.png)


Outra dica importante: lembre-se de filtrar apenas as atividades específicas desejadas, principalmente se você também registra outros esportes.

```
run_df = df[df['Activity Type'] == 'Run']
```

Com esse dataset de atividades do Strava, podemos ver algumas colunas indicando o tênis usado em cada atividade. A minha ideia a partir disso foi tentar agrupar os dados por tênis e analisar métricas como a distância total percorrida, número de atividades, etc;

Inicialmente, considerei utilizar as informações da coluna `Activity Gear`, onde é registrado o nome do tênis cadastrado no Strava. No entanto, percebi que essa lista estava incompleta (eu cheguei até abrir um chamado no suporte do Strava para investigar um possível bug).

Minha solução foi combinar as informações das colunas `Gear` e `Activity Gear` para criar **manualmente** um dicionário que relaciona o ID de cada tênis com o respectivo nome.

Primeiro eu exportei os IDs dos tênis listados.

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-shoes-id.png)


Em seguida, verifiquei quais atividades estavam presentes na lista e quais não estavam. Para as atividades não identificadas, utilizei a coluna `Activity ID` para reconstruir a URL correspondente no Strava. Com isso, acessei a interface da plataforma para conferir qual tênis foi utilizado em cada atividade.

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-shoes-match.png)

Com isso, consegui montar meu dicionário.

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-shoes-dict.png)

E finalmente, fazer a relação entre eles:

```
run_df['Gear Name'] = run_df['Gear'].map(shoes_dict)
```

# Construindo a animação

Para criar a animação, utilizei o serviço online Flourish (utilizei a versão gratuita da plataforma).

Além de ajustar os parâmetros, utilizei o código para reorganizar os dados, pois, no Flourish, o "tempo" precisa ser apresentado em formato de colunas.

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-flourish-data.png)


### O resultado final:

[public.flourish.studio/visualisation/20001712](https://public.flourish.studio/visualisation/20001712)


---
>>> acesse o [notebook aqui](https://github.com/maluta/maluta.github.com/blob/master/labs/strava/Strava%20Analysis.ipynb) <<<



Outra análise:
![](https://pbs.twimg.com/media/Ga59-onXsAAemX9?format=jpg&name=large)
