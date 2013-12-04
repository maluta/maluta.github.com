---
layout: post
title: Adicionando SSH Fingerprints automaticamente ao known_hosts
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Ol,
Da mesma srie de posts sobre automatizao de configuraes da pasta do usurio (nossa, pra quem no postava, j esta at fazendo srie de posts heheh). Iremos abordar uma configurao que muitas vezes nos trs muita dor de cabea, aceitar todos fingerprints de chaves de servidor ssh.

Eu costumo utilizar o $HOME/.ssh/config para deixar todos meus hosts ssh configurados, pra quem no conhece isso, basta criar este arquivo, e ele usa o seguinte formato:
<pre lang="php" escaped="true">Host &lt;nome servidor&gt;
HostName &lt;host/ip&gt;
User &lt;usurio&gt;</pre>
realizando a configurao de um servidor fictcio:
<pre lang="bash">Host servidor
HostName localhost
User root</pre>
Feito isto, basta digitar: ssh servidor, que seria o equivalente a ssh root@localhost, isto facilita quando no se tem acesso ao /etc/hosts para guardar nome amigvel para determinados ips, e quando se acessa diferentes servidores com diferentes nomes de usurios. Voltando ao nosso problema, eu tenho meu config, mas meu known_hosts esta desatualizado ou pior, vazio!

A cada nova conexo seria necessrio aceitar cada chave do servidor, como a seguir:
<blockquote>The authenticity of host 'servidor (127.0.0.1)' can't be established.
RSA key fingerprint is bc:b1:8d:c3:61:6a:5b:9f:c1:b2:16:c5:e4:d2:b1:b2.
Are you sure you want to continue connecting (yes/no)?</blockquote>
O que torna cansativo, principalmente se tiver que executar um comando em cada servidor, ento temos o seguinte script:
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
O que este script faz, nada mais  do que ler cada Host configurado no arquivo <em>$HOME/.ssh/config</em> e aceitar automaticamente a chave primria do mesmo atravs da <em>opo -o StrictHostKeyChecking=no</em> e salva no arquivo <em>-o UserKnownHostsFile=$KNOWN_HOSTS</em> (no nosso caso KNOWN_HOSTS=./ssh_known_hosts), fiz isso para no sobrescrever o seu arquivo <em>known_hosts</em> e ainda para facilitar a leitura do arquivo, ou pegar somente os hosts que lhe interessam, o segundo for do script coloca o valor do 'Host' como comentrio em cada fingerprint.

Vale a pena lembrar que cada chave ser automaticamente aceita, ento cabe a voc garantir que realmente cada chave pertence ao servidor em questo, e no esta ocorrendo nenhum tipo de ataque man-in-the-middle. E aps executado o script,  s colocar os fingerprints no known_hosts e estamos prontos para conectar no servidor sem confirmao dos mesmos.

At breve.