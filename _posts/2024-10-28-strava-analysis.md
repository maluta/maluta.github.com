---
layout: post
title: Strava Analysis 
desc: 
proj-url:
proj-num: 01
draft: false
---

### Extraindo os dados 


1. Acesse [strava.com/athlete/delete_your_account](https://www.strava.com/athlete/delete_your_account) e faça a solicitação dos seus dados. 

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-export.png)

Aguarde até receber um e-mail na sua 'Your Strava archive is ready for download' enviado por `no-reply@strava.com`

O arquivo final é um .zip com os seguintes arquivos:

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-export-files.png)


### Explorando os dados

Eu usei o [Jupyter Notebok](https://jupyter.org/) para fazer as análises a partir do arquivo `activities.csv`

```
df = pd.read_csv('activities.csv')
```

![](https://github.com/maluta/maluta.github.com/raw/master/images/strava-columns.png)

---

![](https://pbs.twimg.com/media/Ga59-onXsAAemX9?format=jpg&name=large)
