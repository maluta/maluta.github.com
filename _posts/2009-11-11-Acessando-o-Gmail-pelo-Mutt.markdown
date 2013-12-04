---
layout: post
title: Acessando o Gmail pelo Mutt
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Para acessar seus <em>emails</em> da conta do GMAIL no modo texto, utilizando o <a title="mutt website" href="http://www.mutt.org/" target="_blank">mutt</a>, adicione ao arquivo ~/.muttrc</p>

<pre style="text-align: justify;">
set imap_user = "USERNAME@gmail.com"
set imap_pass = "PASSWORD"
set spoolfile = imaps://imap.gmail.com:993/INBOX
set folder = imaps://imap.gmail.com:993
set record="imaps://imap.gmail.com/[Gmail]/Sent Mail"
set postponed="imaps://imap.gmail.com/[Gmail]/Drafts"
set header_cache="~/.mutt/cache/headers"
set message_cachedir="~/.mutt/cache/bodies"
set certificate_file=~/.mutt/certificates

set move = no

set sort = 'threads'
set sort_aux = 'last-date-received'
set imap_check_subscribed

ignore "Authentication-Results:"
ignore "DomainKey-Signature:"
ignore "DKIM-Signature:"
ignore "Received:"
ignore "Return-Path"
ignore "MIME-Version"
ignore "X-Spam-Details"
ignore "Received-SPF"
ignore "List-Id"
ignore "List-Unsubscribe"
ignore "List-Post"
ignore "List-Help"
ignore "List-Subscribe"
ignore "Content-Type"
ignore "Content-Transfer-Encoding"
ignore "Sender"
ignore "Errors-To"
ignore "X-BeenThere"
ignore "X-Mailman-Version"
ignore "Precedence"
ignore "List-Archive"
ignore "X-MIME-Autoconverted"
ignore "Message-ID"
ignore "Delivered-To"
ignore "User-Agent"
ignore "X-Spam-Score"
ignore "X-Spam-OrigSender"
ignore "X-Spam-Bar"
ignore "In-Reply-To"
ignore "References"
ignore "X-System-Of-Record"


hdr_order Date From To Cc
</pre>