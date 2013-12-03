---
layout: post
title: Kernel stats: horrios dos commits
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p align="justify">
Durante sua apresentação na Linux.conf.au 2010, o fundador do site LWN.net e contribuidor do kernel Jonathan Corbet <a href="http://www.lca2010.org.nz/programme/schedule/view_talk/50141?day=wednesday">demonstrou</a> uma análise das contribuições no kernel Linux durante aproximadamente 1 ano (entre Dez 2008 e Jan 2010). Uma das conclusões é que 75% código é escrito por programadores pagos por empresas, lideram a lista: Red Hat (12%), Intel (8%), IBM e Novell (6% cada), Oracle (3%). 
<p>
<p align="justify">
Um dos pontos que a estatística não mostra é que - mesmo sendo empregado de grandes empresas - boa parte do trabalho é feita fora do horário "comercial", se alguém observar as datas de todos os <em>commits</em> e organizá-los pela frequência em horas, você tem o seguinte resultado para diferentes <em>releases</em>. 
</p> 

<pre>
<strong>v2.6.33-rc7	</strong>	<strong>v2.6.32</strong>			  <strong>v2.6.24</strong>	

Hora	Commits		Hora	Commits		Hora	Commits
<strong>0	8069		0	7808		0	4745
1	7052		1	6800		1	4155
2	4715		2	4556		2	2835
3	2717		3	2601		3	1395</strong>
4	2236		4	2096		4	898
5	1426		5	1193		5	559
6	1299		6	1134		6	381
7	1933		7	1723		7	580
8	4108		8	3798		8	1445
9	6429		9	6003		9	2261
10	8550		10	7969		10	3027
11	10284		11	9640		11	3946
12	9191		12	8403		12	3313
13	11728		13	11024		13	4522
<strong>14	13127		14	12340		14	5052
15	14281		15	13295		15	5813
16	13685		16	12721		16	5212
17	11486		17	10793		17	5050</strong>
18	7938		18	7334		18	3335
19	7354		19	6933		19	2850
20	7460		20	6953		20	3161
21	8561		21	8138		21	3436
22	8953		22	8498		22	3872
23	7741		23	7335		23	3843
</pre>
Comando utilizado para gerar esses dados:
<blockquote>
git log v2.6.33 | grep ^Date: | perl -pe 's/^(?:\S+\s+){4}(\d+).*/$1/' | sort -g | uniq -c
</blockquote>

A conclusão é que muitos desenvolvedores fazem o código durante a noite e acordam tarde. ;-)
