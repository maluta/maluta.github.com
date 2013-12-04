---
layout: post
title: Adicionando SSH Fingerprints automaticamente ao known_hosts
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Ol�,
Da mesma s�rie de posts sobre automatiza��o de configura��es da pasta do usu�rio (nossa, pra quem n�o postava, j� esta at� fazendo s�rie de posts heheh). Iremos abordar uma configura��o que muitas vezes nos tr�s muita dor de cabe�a, aceitar todos fingerprints de chaves de servidor ssh.

Eu costumo utilizar o $HOME/.ssh/config para deixar todos meus hosts ssh configurados, pra quem n�o conhece isso, basta criar este arquivo, e ele usa o seguinte formato:
<pre lang="php" escaped="true">Host &lt;nome servidor&gt;
HostName &lt;host/ip&gt;
User &lt;usu�rio&gt;</pre>
realizando a configura��o de um servidor fict�cio:
<pre lang="bash">Host servidor
HostName localhost
User root</pre>
Feito isto, basta digitar: ssh servidor, que seria o equivalente a ssh root@localhost, isto facilita quando n�o se tem acesso ao /etc/hosts para guardar nome amig�vel para determinados ips, e quando se acessa diferentes servidores com diferentes nomes de usu�rios. Voltando ao nosso problema, eu tenho meu config, mas meu known_hosts esta desatualizado ou pior, vazio!

A cada nova conex�o seria necess�rio aceitar cada chave do servidor, como a seguir:
<blockquote>The authenticity of host 'servidor (127.0.0.1)' can't be established.
RSA key fingerprint is bc:b1:8d:c3:61:6a:5b:9f:c1:b2:16:c5:e4:d2:b1:b2.
Are you sure you want to continue connecting (yes/no)?</blockquote>
O que torna cansativo, principalmente se tiver que executar um comando em cada servidor, ent�o temos o seguinte script:
<pre lang="bash">KNOWN_HOSTS=./ssh_known_hosts
SSH_ARGS="-o StrictHostKeyChecking=no -o UserKnownHostsFile=$KNOWN_HOSTS"

for host in `cat $HOME/.ssh/config |grep "^Host "|cut -d" " -f2`; do
    echo $host;
    ssh $host $SSH_ARGS echo '';
done

cnt=1
for host in `cat $HOME/.ssh/config |grep "^Host "|cut -d" " -f2`; do
    linha1=`sed "${cnt}q;d" $KNOWN_HOSTS`
    echo $linha1 $host &gt;&gt; ${KNOWN_HOSTS}.tmp
    echo "" &gt;&gt; ${KNOWN_HOSTS}.tmp
    let cnt++
done

mv ${KNOWN_HOSTS}.tmp ${KNOWN_HOSTS}</pre>
O que este script faz, nada mais � do que ler cada Host configurado no arquivo <em>$HOME/.ssh/config</em> e aceitar automaticamente a chave prim�ria do mesmo atrav�s da <em>op��o -o StrictHostKeyChecking=no</em> e salva no arquivo <em>-o UserKnownHostsFile=$KNOWN_HOSTS</em> (no nosso caso KNOWN_HOSTS=./ssh_known_hosts), fiz isso para n�o sobrescrever o seu arquivo <em>known_hosts</em> e ainda para facilitar a leitura do arquivo, ou pegar somente os hosts que lhe interessam, o segundo for do script coloca o valor do 'Host' como coment�rio em cada fingerprint.

Vale a pena lembrar que cada chave ser� automaticamente aceita, ent�o cabe a voc� garantir que realmente cada chave pertence ao servidor em quest�o, e n�o esta ocorrendo nenhum tipo de ataque man-in-the-middle. E ap�s executado o script, � s� colocar os fingerprints no known_hosts e estamos prontos para conectar no servidor sem confirma��o dos mesmos.

At� breve.