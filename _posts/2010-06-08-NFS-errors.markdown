---
layout: post
title: NFS errors
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



If you use NFS to mount your root filesystem you should probably faced with this problem:
<blockquote>Root-NFS: Unable to get mountd port number from server, using default
Root-NFS: Server returned error -5 while mounting /my/nfs/server/path/
VFS: Unable to mount root fs via NFS, trying floppy.</blockquote>
<p style="text-align: justify;">The <strong>-5 </strong>and<strong> -13 </strong>are the most common on my daily usage, but I always forgot what this number means... So, I decided to get it from source by checking <em>nfs-utils </em>package. The following values where extracted  from <em>utils/mount/error.c</em>.</p>

<pre>EPERM  ........................................ -1

ENOENT ........................................ -2

EIO ........................................... -3

ENXIO ......................................... -4

<strong>EACCESS ....................................... -5 </strong>

EEXIST ........................................ -6

ENODEV ........................................ -7

ENOTDIR ....................................... -8

EISDIR ........................................ -9

EINVAL ........................................ -10

EFBIG ......................................... -11

ENOSPC  ....................................... -12

<strong>EROFS ......................................... -13</strong>

ENAMETOOLONG .................................. -14

ENOTEMPTY ..................................... -15

EDQUOT ........................................ -16

ESTALE ........................................ -17

EWFLUSH ....................................... -18
</pre>
Knowing what each error status means allow you quick fix the problems.