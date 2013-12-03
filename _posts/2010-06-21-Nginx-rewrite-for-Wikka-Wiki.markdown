---
layout: post
title: Nginx rewrite for Wikka Wiki
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



I'm posting it here, because I started a few weeks ago working with <a title="Nginx" href="http://nginx.org/" target="_blank">Nginx</a> (if you don't know that, you really should), a very powerful and <strong>fast</strong> webserver (lets leave it for another post), but I faced a problem with redirects for Wikka Wiki, I'm not a beginner on regular expressions or mod_rewrite, but sometimes we get in trouble working on something new.

I haven't found the solution for my problem (for wordpress, drupal and joomla there are so many) so I resolved it and now I'm posting if somebody can't do it or just wanna some copy/paste ;)
<pre lang="c" line="1"> location ~ ^/wiki {
 	root /path/to/wiki;
 	index wikka.php;

 	if (!-e $request_filename) {
 		rewrite ^/wiki/images/(.*)$ /images/$1 break;
		rewrite ^/wiki/templates/(.*)$ /templates/$1 break;
 		rewrite ^/wiki/3rdparty/plugins/freemind/(.*)$ /3rdparty/plugins/freemind/$1 break;
 		rewrite ^/wiki/3rdparty/plugins/wikkaedit/(.*)$ /3rdparty/plugins/wikkaedit/$1 break;
 		rewrite ^/wiki/(.*)$ /wiki/wikka.php?wakka=$1 break;
 		break;
 	}
 }
</pre>

A brief explanation:

on line 1 we setup where our wiki is located, on our case /wiki, so in line 2 we give full path to where the wiki's file are located on the filesystem and line 3 we says our index will be wikka.php once Wikka Wiki just redirect index.php to wikka.php (ok I don't mind why they don't put the contents of wikka.php on index.php and its over ;) ).

line 5-12 we configure the rewrite rules, on line 5 is the condition what to do when there is no file or symbolic link when a URL is acessed, if its matched the following rules are processed:
line 6-10: rules to ensure that static content like css, js and images won't be redirected to wikka.php.
line 11: the main rule, that will redirect all URLs to wikka.php so it process and show the output for each wiki page.

I don't why (I'm new to Nginx) even using the condition <strong>if(!-e $request_filename)</strong> I need to put the rules to ensure that static content will be reached, if I discover, I update this post, but these rules are working for me under Nginx 0.7.67 and Wikka 1.2-p1 