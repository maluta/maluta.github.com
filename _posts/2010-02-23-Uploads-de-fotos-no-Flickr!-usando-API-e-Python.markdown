---
layout: post
title: Uploads de fotos no Flickr! usando API e Python
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">A API (Interface de Programa��o de Aplicativo) do <a href="www.flickr.com" target="_blank">Flickr!</a> � bem <a href="http://www.flickr.com/services/api/" target="_blank">documetada</a> e rapidamente voc� pode fazer bastante coisa. Se voc� desejar usar a linguagem Python como m�todo de acesso, em linhas gerais voc� precisa.</p>

<ol>
	<li><a href="http://www.flickr.com/services/apps/create/" target="_blank">Criar</a> uma chave na API do Flickr!</li>
	<li>Download do <em>binding</em> para acesso a API (<a href="http://pypi.python.org/pypi/flickrapi" target="_blank">flickrapi</a>)</li>
</ol>
Nas distribui��es Linux, um dos jeitos de instalar � usar o easy_install
<pre>easy_install flickrapi</pre>
<p align="justify">
Um modo eficaz para fazer o <em>upload</em> das fotos no servi�o seria um <em>script</em> que varre e submete todas as imagens, por exemplo, de uma pasta definida. O exemplo abaixo recebe como par�metro um diret�rio e busca por todos os arquivos com extens�o .jpg. A fun��o <em>status</em> � apenas para mostrar o andamento do <em>upload</em> e � executada como uma chamada <em>callback</em> no m�todo flickr.upload(). Nos meus testes, precisei pegar o n�mero definido na vari�vel <em>token</em>, antes, executando na interface de linha de comando do Python os seguintes passos:
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

Na hora o <em>browser</em> padr�o ir� abrir e pedir para voc� confirmar o uso do aplicativo.

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

Utilize sua criatividade para extender essa id�ia e criar aplicativos que ensinem e facilite sua vida. :-)