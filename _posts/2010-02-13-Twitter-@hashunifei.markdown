---
layout: post
title: Twitter @hashunifei
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p align="justify">
Sempre tive curiosidade de fazer um agregador para o Twitter, ou seja, criar um usuário que fizesse o <em>retwitt</em> de todos os termos que aparecem sobre determinada palavra. Para fazer um teste resolvi criar um usuário chamado <a href="http://www.twitter.com/hashunifei">@hashunifei</a> que irá agregar o que pessoal escrever sobre a <a href="http://www.unifei.edu.br">UNIFEI</a> (Universidade Federal de Itajubá) incluindo o nome antigo ;-)

Seguindo a filosofia <em>code less, create more</em> decidi fazer um <em>script</em> em Python que acessa a <a href="http://apiwiki.twitter.com/">API</a> do Twitter. Depois só configurar algum agendador de tarefas (ex.: <a href="http://en.wikipedia.org/wiki/Cron">cron</a>) para executar o programa de tempos em tempos. Para evitar que a cada busca os mesmos <em>twitts</em> sejam publicados há um arquivo chamado <em>.hashunifei</em> que grava o número de identificação (id) das mensagens publicadas. 
</p>
<pre lang="python"> 
# -*- coding: utf-8 -*-
# Tiago Maluta <maluta@unifei.edu.br> 

import simplejson, urllib
import twitter 

list_id = []
api = twitter.Api(username='USUARIO', password='SENHA')

SEARCH_BASE = 'http://search.twitter.com/'
url = SEARCH_BASE + "search.json?q=UNIFEI+OR+efei"

def publish(user,text):
	twitt = "RT @"+user+" "+text
	if len(twitt) > 140:
		twitt = twitt[:140]
	api.PostUpdates(twitt)

result = simplejson.load(urllib.urlopen(url))['results']

with open(".hashunifei","r+") as f:
    data = f.read()
    list_id = data.split(",") 

f = open(".hashunifei","a")
for twitt in result:

	text = twitt['text']
	user = twitt['from_user']
	
	if user != "hashunifei":
		id = str(twitt['id'])
		if id not in list_id:	
			list_id.append(id)
			f.write(id+',')
			publish(user,text)
f.close() 
</pre>

Se quiser testar o código-fonte (lembre-se de mudar o usuário e senha e a palavra da busca)
<blockquote>
$ touch .hashunifei
$ wget <a href="http://github.com/maluta/junk/raw/master/hashunifei.py">http://github.com/maluta/junk/raw/master/hashunifei.py</a>
</blockquote>

Limitações: A mensagem é truncada em 140 caracteres (limite do twitter). 

Eu sinceramente não sei se é assim que o pessoal faz, foi a primeira idéia que tive..., se o pessoal que entende de <em>web</em> quiser colaborar seria ótimo.

