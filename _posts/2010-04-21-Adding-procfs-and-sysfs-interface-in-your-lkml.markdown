---
layout: post
title: Adding procfs and sysfs interface in your lkml
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">Hi. This post will show how to add two <strong>important</strong> things about device model in your linux kernel module (lkml). Sysfs is the user-space manifestation of the kernel's structured device model. It's similar to procfs in that both are in-memory filesystem containing information about kernel data structures. Basically:</p>

<ul>
	<li>procfs is a generic window into kernel internals</li>
	<li>sysfs is specific to device model</li>
</ul>
Information such as process descriptors and sysctls parameters belong to procfs and not sysfs. Note that:Sysfs is not a replacement for procfs.

Lets create two useless (in a practical way) that presents the "idea" behind these constructions.

<strong>1. Procfs</strong>
<p style="text-align: justify;">The snippet below creates a <em>/proc/coding</em> allowing read or write some content.</p>

<pre><span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/kernel.h&gt;</span></strong></span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/module.h&gt;</span></strong></span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/init.h&gt;</span></strong></span>

<span style="color: #444444;">/* for proc_dir_entry and create_proc_entry */</span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/proc_fs.h&gt;</span></strong></span>

<span style="color: #444444;">/* For sprintf and snprintf */</span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/string.h&gt;</span></strong></span>

<span style="color: #444444;">/* For copy_from_user */</span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/uaccess.h&gt;</span></strong></span>

<strong>static</strong> <strong>char</strong> <span style="color: #2040a0;">internal_buffer</span><span style="color: #4444ff;">[</span><span style="color: #ff0000;">256</span><span style="color: #4444ff;">]</span><span style="color: #4444ff;">;</span>

<strong>int</strong> <span style="color: #2040a0;">buf_read</span><span style="color: #4444ff;">(</span><strong>char</strong> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">buf</span>, <strong>char</strong> <span style="color: #4444ff;">*</span><span style="color: #4444ff;">*</span><span style="color: #2040a0;">start</span>, <span style="color: #2040a0;">off_t</span> <span style="color: #2040a0;">offset</span>, <strong>int</strong> <span style="color: #2040a0;">count</span>, <strong>int</strong> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">eof</span>, <strong>void</strong> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">data</span><span style="color: #4444ff;">)</span>
<span style="color: #4444ff;"><strong>{</strong></span>
	<strong>int</strong> <span style="color: #2040a0;">len</span><span style="color: #4444ff;">;</span>
	<span style="color: #2040a0;">len</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">snprintf</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">buf</span>, <span style="color: #2040a0;">count</span>, <span style="color: #008000;">"%s"</span>, <span style="color: #2040a0;">internal_buffer</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>
	<strong>return</strong> <span style="color: #2040a0;">len</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<strong>static</strong> <strong>int</strong> <span style="color: #2040a0;">buf_write</span><span style="color: #4444ff;">(</span><strong>struct</strong> <span style="color: #2040a0;">file</span> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">file</span>, <strong>const</strong> <strong>char</strong> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">buf</span>, <strong>unsigned</strong> <strong>long</strong> <span style="color: #2040a0;">count</span>, <strong>void</strong> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">data</span><span style="color: #4444ff;">)</span>
<span style="color: #4444ff;"><strong>{</strong></span>
	<strong>if</strong><span style="color: #4444ff;">(</span><span style="color: #2040a0;">count</span> <span style="color: #4444ff;">&gt;</span> <span style="color: #ff0000;">255</span><span style="color: #4444ff;">)</span> <span style="color: #444444;">/* to avoid overflowwwwwwwwww */</span>
		<span style="color: #2040a0;">count</span> <span style="color: #4444ff;">=</span> <span style="color: #ff0000;">255</span><span style="color: #4444ff;">;</span>

	<span style="color: #444444;">/* Copies data from user space to kernel space */</span>
	<span style="color: #2040a0;">copy_from_user</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">internal_buf</span>, <span style="color: #2040a0;">buf</span>, <span style="color: #2040a0;">count</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>

	<span style="color: #444444;">/* inserting NULL to end the string */</span>
	<span style="color: #2040a0;">internal_buf</span><span style="color: #4444ff;">[</span><span style="color: #2040a0;">count</span><span style="color: #4444ff;">]</span> <span style="color: #4444ff;">=</span> <span style="color: #008000;">'<span style="color: #77dd77;">\0</span>'</span><span style="color: #4444ff;">;</span>
	<strong>return</strong> <span style="color: #2040a0;">count</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<strong>int</strong> <span style="color: #2040a0;">__init</span> <span style="color: #2040a0;">proc_init</span><span style="color: #4444ff;">(</span><strong>void</strong><span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>
	<span style="color: #444444;">/* Simple */</span>
	<strong>struct</strong> <span style="color: #2040a0;">proc_dir_entry</span> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">de</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">create_proc_entry</span><span style="color: #4444ff;">(</span><span style="color: #008000;">"coding"</span>, <span style="color: #ff0000;">0667</span>, <span style="color: #ff0000;">0</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>

	<span style="color: #444444;">/* Set pointers to our functions */</span>
	<span style="color: #2040a0;">de</span><span style="color: #4444ff;">-</span><span style="color: #4444ff;">&gt;</span><span style="color: #2040a0;">read_proc</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">buf_read</span><span style="color: #4444ff;">;</span> <span style="color: #444444;">/* reading */</span>
	<span style="color: #2040a0;">de</span><span style="color: #4444ff;">-</span><span style="color: #4444ff;">&gt;</span><span style="color: #2040a0;">write_proc</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">buf_write</span><span style="color: #4444ff;">;</span> <span style="color: #444444;">/* writing */</span> 

	<span style="color: #444444;">/* We initialize our internal_buffer with some text. */</span>
	<span style="color: #2040a0;">sprintf</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">internal_buffer</span>, <span style="color: #008000;">"www.coding.com.br"</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>
	<strong>return</strong> <span style="color: #ff0000;">0</span> <span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<strong>void</strong> <span style="color: #2040a0;">__exit</span> <span style="color: #2040a0;">proc_cleanup</span><span style="color: #4444ff;">(</span><strong>void</strong><span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>

	<span style="color: #444444;">/* We delete our entry */</span>
	<span style="color: #2040a0;">remove_proc_entry</span><span style="color: #4444ff;">(</span><span style="color: #008000;">"coding"</span>, <span style="color: #2040a0;">NULL</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>

<span style="color: #4444ff;"><strong>}</strong></span>

<span style="color: #2040a0;">module_init</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">proc_init</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;">module_exit</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">proc_cleanup</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>

<span style="color: #2040a0;">MODULE_LICENSE</span><span style="color: #4444ff;">(</span><span style="color: #008000;">"GPL"</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span></pre>
<strong>2. Sysfs</strong>

This example only creates a <em>/sys/class/&lt;module-name&gt; </em>directorywith nothing inside. This may not be clear now but remember when I show - in the next posts - some practical use with device node (/dev).
<pre><span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/kernel.h&gt;</span></strong></span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/module.h&gt;</span></strong></span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/init.h&gt;</span></strong></span>

<span style="color: #444444;">/* for sysfs class creation */</span>
<span style="color: #0000ff;"><strong>#include <span style="color: #008000;">&lt;linux/platform_device.h&gt;</span></strong></span>

<strong>static</strong> <strong>struct</strong> <span style="color: #2040a0;">class</span> <span style="color: #4444ff;">*</span><span style="color: #2040a0;">sysfs_class</span><span style="color: #4444ff;">;</span>

<strong>int</strong> <span style="color: #2040a0;">__init</span> <span style="color: #2040a0;">sysfs_init</span><span style="color: #4444ff;">(</span><strong>void</strong><span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>

	<span style="color: #2040a0;">sysfs_class</span> <span style="color: #4444ff;">=</span> <span style="color: #2040a0;">class_create</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">THIS_MODULE</span>, <span style="color: #008000;">"sysfs"</span> <span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>
	<strong>return</strong> <span style="color: #ff0000;">0</span> <span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<strong>void</strong> <span style="color: #2040a0;">__exit</span> <span style="color: #2040a0;">sysfs_cleanup</span><span style="color: #4444ff;">(</span><strong>void</strong><span style="color: #4444ff;">)</span> <span style="color: #4444ff;"><strong>{</strong></span>

	<span style="color: #444444;">/* We delete our entry */</span>
	<span style="color: #2040a0;">class_destroy</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">sysfs_class</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>
<span style="color: #4444ff;"><strong>}</strong></span>

<span style="color: #2040a0;">module_init</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">sysfs_init</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>
<span style="color: #2040a0;">module_exit</span><span style="color: #4444ff;">(</span><span style="color: #2040a0;">sysfs_cleanup</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span>

<span style="color: #2040a0;">MODULE_LICENSE</span><span style="color: #4444ff;">(</span><span style="color: #008000;">"GPL"</span><span style="color: #4444ff;">)</span><span style="color: #4444ff;">;</span></pre>