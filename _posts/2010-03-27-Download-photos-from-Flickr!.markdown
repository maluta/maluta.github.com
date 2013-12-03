---
layout: post
title: Download photos from Flickr!
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">I think that one problem regarding creating a <em>script</em> to download photos form Flickr is getting copyrighted material. Suppose that you want all photos from Itajubá city. You can use Flickr API or an YQL request, as follows:</p>

<pre>select * from flickr.photos.search where text="itajubá"</pre>
<p style="text-align: justify;">My first try to get license information was showing the pertinent part of JSON output. You could see that there isn't a field telling that, but if you look at documentation there's a "license" parameter.</p>

<blockquote>"farm": "5",
"id": "4458853758",
"isfamily": "0",
"isfriend": "0",
"ispublic": "1",
"owner": "76062736@N00",
"secret": "9edcd7aea8",
"server": "4003",
"title": "Clube"</blockquote>
Flickr! has seven options to licensing your photo (again I didn't found in documentation, I tried each one)
<ul>
	<li>None (All rights reserved) [ license="0" ]</li>
	<li>Attribution-NonCommercial-ShareAlike Creative Commons [ license="1" ]</li>
	<li>Attribution-NonCommercial Creative Commons [ license="2" ]</li>
	<li>Attribution-NonCommercial-NoDerivs Creative Commons [ license="3" ]</li>
	<li>Attribution Creative Commons [ license="4" ]</li>
	<li>Attribution-ShareAlike Creative Commons [ license="5" ]</li>
	<li>Attribution-NoDerivs Creative Commons [ license="6" ]</li>
</ul>
My friend was looking to a way to download all photos from Yahoo! Open Hack Brazil so I decided to create a quick way to get theses photos (respecting copyrighted material). My <a href="http://developer.yahoo.com/yql/console/?q=select%20*%20from%20flickr.photos.search%20where%20text%3D%22Cat%22%20limit%200#h=select%20*%20from%20flickr.photos.search%280%2C2000%29%20where%20tags%3D%22brhackday%22%20and%20license%3D%221%2C2%2C3%2C4%2C5%2C6%22">query</a> looks like:
<pre>select * from flickr.photos.search(0,2000) where tags="brhackday" and license="1,2,3,4,5,6"</pre>
<p style="text-align: justify;">After tests I put the URL from YQL virtual console in my Python code (that parses JSON) and generate a Shell Script to download (using curl/wget)</p>

<pre lang="python">import simplejson
import urllib 

f = open("download.sh","w+")
f.write("#!/bin/sh\n")
i = 0
while True:

	url_base="http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20flickr.photos.search(" + str(i) 
+ "%2C" + str(i+100) +")%20where%20tags%3D%22brhackday%22%20and%20license%3D%221%2C2%2C3%2C4%2C5%2C6%22
&format=json" 	

	rest = simplejson.load(urllib.urlopen(url_base))['query']

        if rest['count'] == '0':
		f.close()
		exit() 

	photos = rest['results']['photo'] 

	for photo in photos:
		id = photo['id']
		owner = photo['owner']
		d = "curl -s http://www.flickr.com/photos/%s/%s/sizes/o 
| egrep \"<p><img src=\" 
| sed 's/<p>//g ; s/<br \/>//g ; s/<\/p>//g ; s/<img src=\"//g ; s/\" \/>//g' 
| xargs wget ;" % (owner, id)
		f.write(d+'\n')
		i += 100

f.close()</pre>
<p style="text-align: justify;">Probably If you cut &amp; paste the code they will not work due some indentation issue, so I published in gist <a href="http://gist.github.com/346413">here</a>.</p>
The usage I simple:
<pre>$ python flickr-d.py
$ sh download.sh</pre>
This was a extremely simple workaround but I expect you enjoy!