---
layout: post
title: Uploads de fotos no Flickr! usando API e Python
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">A API (Interface de Programação de Aplicativo) do <a href="www.flickr.com" target="_blank">Flickr!</a> é bem <a href="http://www.flickr.com/services/api/" target="_blank">documetada</a> e rapidamente você pode fazer bastante coisa. Se você desejar usar a linguagem Python como método de acesso, em linhas gerais você precisa.</p>

<ol>
	<li><a href="http://www.flickr.com/services/apps/create/" target="_blank">Criar</a> uma chave na API do Flickr!</li>
	<li>Download do <em>binding</em> para acesso a API (<a href="http://pypi.python.org/pypi/flickrapi" target="_blank">flickrapi</a>)</li>
</ol>
Nas distribuições Linux, um dos jeitos de instalar é usar o easy_install
<pre>easy_install flickrapi</pre>
<p align="justify">
Um modo eficaz para fazer o <em>upload</em> das fotos no serviço seria um <em>script</em> que varre e submete todas as imagens, por exemplo, de uma pasta definida. O exemplo abaixo recebe como parâmetro um diretório e busca por todos os arquivos com extensão .jpg. A função <em>status</em> é apenas para mostrar o andamento do <em>upload</em> e é executada como uma chamada <em>callback</em> no método flickr.upload(). Nos meus testes, precisei pegar o número definido na variável <em>token</em>, antes, executando na interface de linha de comando do Python os seguintes passos:
</p>
<pre lang="python">
>>> api_key = "<API>"
>>> secret = "<CHAVE SECRETA>"
>>> username = "<USER>"
>>> flickr = flickrapi.FlickrAPI(api_key,secret,username)
>>> (token, frob) = flickr.get_token_part_one(perms="write")
>>> print token
>>> print frob
</pre>

Na hora o <em>browser</em> padrão irá abrir e pedir para você confirmar o uso do aplicativo.

<pre lang="python">
# -*- coding: utf-8 -*-
#/bin/python 

import sys
import glob 
import flickrapi

api_key = "<API>"
secret = "<CHAVE SECRETA>"
username = "<USER>"

token="<TOKEN>"
frob=None

def status(progress, done):
	if done:
		print "Finished ;-)"
	else:
		print "At %s%%" % progress

def upload(photo):
	flickr.upload(photo, callback=status)

if __name__ == "__main__":
	
        flickr = flickrapi.FlickrAPI(api_key,secret,username)
        flickr.get_token_part_two((token,frob))

        photos = sys.argv[1]+"*.jpg"

	for photo in glob.glob(photos):
		print "Uploading: ",photo
		upload(photo)
</pre>

Um exemplo de uso:

<pre>
python upload.py /Fotos
</pre>

Utilize sua criatividade para extender essa idéia e criar aplicativos que ensinem e facilite sua vida. :-)