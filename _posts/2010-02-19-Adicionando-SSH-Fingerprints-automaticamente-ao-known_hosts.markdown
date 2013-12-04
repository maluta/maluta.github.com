---
layout: post
title: Adicionando SSH Fingerprints automaticamente ao known_hosts
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



Olá,
Da mesma série de posts sobre automatização de configurações da pasta do usuário (nossa, pra quem não postava, já esta até fazendo série de posts heheh). Iremos abordar uma configuração que muitas vezes nos trás muita dor de cabeça, aceitar todos fingerprints de chaves de servidor ssh.

Eu costumo utilizar o $HOME/.ssh/config para deixar todos meus hosts ssh configurados, pra quem não conhece isso, basta criar este arquivo, e ele usa o seguinte formato:
<pre lang="php" escaped="true">Host &lt;nome servidor&gt;
HostName &lt;host/ip&gt;
User &lt;usuário&gt;</pre>
realizando a configuração de um servidor fictício:
<pre lang="bash">Host servidor
HostName localhost
User root</pre>
Feito isto, basta digitar: ssh servidor, que seria o equivalente a ssh root@localhost, isto facilita quando não se tem acesso ao /etc/hosts para guardar nome amigável para determinados ips, e quando se acessa diferentes servidores com diferentes nomes de usuários. Voltando ao nosso problema, eu tenho meu config, mas meu known_hosts esta desatualizado ou pior, vazio!

A cada nova conexão seria necessário aceitar cada chave do servidor, como a seguir:
<blockquote>The authenticity of host 'servidor (127.0.0.1)' can't be established.
RSA key fingerprint is bc:b1:8d:c3:61:6a:5b:9f:c1:b2:16:c5:e4:d2:b1:b2.
Are you sure you want to continue connecting (yes/no)?</blockquote>
O que torna cansativo, principalmente se tiver que executar um comando em cada servidor, então temos o seguinte script:
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
O que este script faz, nada mais é do que ler cada Host configurado no arquivo <em>$HOME/.ssh/config</em> e aceitar automaticamente a chave primária do mesmo através da <em>opção -o StrictHostKeyChecking=no</em> e salva no arquivo <em>-o UserKnownHostsFile=$KNOWN_HOSTS</em> (no nosso caso KNOWN_HOSTS=./ssh_known_hosts), fiz isso para não sobrescrever o seu arquivo <em>known_hosts</em> e ainda para facilitar a leitura do arquivo, ou pegar somente os hosts que lhe interessam, o segundo for do script coloca o valor do 'Host' como comentário em cada fingerprint.

Vale a pena lembrar que cada chave será automaticamente aceita, então cabe a você garantir que realmente cada chave pertence ao servidor em questão, e não esta ocorrendo nenhum tipo de ataque man-in-the-middle. E após executado o script, é só colocar os fingerprints no known_hosts e estamos prontos para conectar no servidor sem confirmação dos mesmos.

Até breve.