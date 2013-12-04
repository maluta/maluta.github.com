---
layout: post
title: Postfix com Virtual Hosts e SMTP Autenticado
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<h1>Instalando o Postfix com Virtual Host e SMTP Autenticado</h1>
<p>Neste post será descrita a instalação passo-a-passo de um Postfix utilizando virtual hosts e smtp autenticado, todas as informações serão armazenadas em uma base de dados MySQL.</p>
<p>Neste procedimento será descrito desde o momento no qual realizamos uma instalação básica do Postfix, depois colocamos suporte a imap e pop3 seguros por TLS, depois configuramos o sasl que fará a autenticação das conexões SMTP através do PAM e por fim instalaremos o postfixadmin que gerenciará as contas de e-mail e o squirrelmail que servirá para acessá-las.</p>
<p>Este documento foi escrito devido a certa dificuldade de realizar uma configuração como esta e a falta de material em português e também a dificuldade de se encontrar um documento tão completo que realize passo-a-passo esses procedimentos ao seu final todos componentes funcionam de forma adequada, espero que sirva para você e comentários/críticas são sempre bem vindos.</p>
<h2>Postfix</h2>
<p><strong>1. Instalando sistema base</strong></p>
<p>Para configurar o postfix necessitaremos dos seguintes pacotes:</p>
<p><em>$ sudo apt-get install postfix postfix-mysql</em><br />
Configuração Padrão: "No Configuration"</p>
<p><em>$ sudo /usr/share/postfix/main.cf.debian /etc/postfix/main.cf</em></p>
<p><strong>2. Pacotes de Autenticação POP3/IMAP</strong></p>
<p>Estes pacotes são para estabelecer conexão segura entre o cliente pop3/imap e o servidor de e-mails.<br />
<em>$ sudo apt-get install courier-authdaemon courier-authlib-mysql courier-pop courier-pop-ssl courier-imap courier-imap-ssl</em></p>
<p><strong>3. Pacotes de Autenticação SMTP</strong></p>
<p>Já estes pacotes serão utilizados para autenticar usuários para envio de e-mails não tornando nosso servidor um open relay<br />
<em>$ sudo apt-get install libsasl2 libsasl2-modules libsasl2-modules-sql openssl sasl2-bin libpam-mysql</em></p>
<p><strong>4. Cria o Banco de Dados para o Postfix</strong></p>
<p>4.1. Cria o arquivo postfixadmin-mysql.sql que contém as tabelas usadas pelo mapeamento do postfix.</p>
<pre>#
# Postfix / MySQL
#
CREATE DATABASE postfix;

GRANT SELECT ON postfix.* TO postfix@localhost IDENTIFIED BY 'postfixpassword';
GRANT SELECT, INSERT, DELETE, UPDATE, CREATE, ALTER ON postfix.* TO postfixadmin@localhost IDENTIFIED BY 'postfixadmin';

USE postfix;
#
# Table structure for table admin
#
CREATE TABLE admin (
username varchar(255) NOT NULL default '',
password varchar(255) NOT NULL default '',
created datetime NOT NULL default '0000-00-00 00:00:00',
modified datetime NOT NULL default '0000-00-00 00:00:00',
active tinyint(1) NOT NULL default '1',
PRIMARY KEY  (username),
KEY username (username)
) COMMENT='Postfix Admin - Virtual Admins';

#
# Table structure for table alias
#
CREATE TABLE alias (
address varchar(255) NOT NULL default '',
goto text NOT NULL,
domain varchar(255) NOT NULL default '',
created datetime NOT NULL default '0000-00-00 00:00:00',
modified datetime NOT NULL default '0000-00-00 00:00:00',
active tinyint(1) NOT NULL default '1',
PRIMARY KEY  (address),
KEY address (address)
) COMMENT='Postfix Admin - Virtual Aliases';

#
# Table structure for table domain
#
CREATE TABLE domain (
domain varchar(255) NOT NULL default '',
description varchar(255) NOT NULL default '',
aliases int(10) NOT NULL default '0',
mailboxes int(10) NOT NULL default '0',
maxquota int(10) NOT NULL default '0',
transport varchar(255) default NULL,
backupmx tinyint(1) NOT NULL default '0',
created datetime NOT NULL default '0000-00-00 00:00:00',
modified datetime NOT NULL default '0000-00-00 00:00:00',
active tinyint(1) NOT NULL default '1',
PRIMARY KEY  (domain),
KEY domain (domain)
) COMMENT='Postfix Admin - Virtual Domains';

#
# Table structure for table domain_admins
#
CREATE TABLE domain_admins (
username varchar(255) NOT NULL default '',
domain varchar(255) NOT NULL default '',
created datetime NOT NULL default '0000-00-00 00:00:00',
active tinyint(1) NOT NULL default '1',
KEY username (username)
) COMMENT='Postfix Admin - Domain Admins';

#
# Table structure for table log
#
CREATE TABLE log (
timestamp datetime NOT NULL default '0000-00-00 00:00:00',
username varchar(255) NOT NULL default '',
domain varchar(255) NOT NULL default '',
action varchar(255) NOT NULL default '',
data varchar(255) NOT NULL default '',
KEY timestamp (timestamp)
) COMMENT='Postfix Admin - Log';

#
# Table structure for table mailbox
#
CREATE TABLE mailbox (
username varchar(255) NOT NULL default '',
password varchar(255) NOT NULL default '',
name varchar(255) NOT NULL default '',
maildir varchar(255) NOT NULL default '',
quota int(10) NOT NULL default '0',
domain varchar(255) NOT NULL default '',
created datetime NOT NULL default '0000-00-00 00:00:00',
modified datetime NOT NULL default '0000-00-00 00:00:00',
active tinyint(1) NOT NULL default '1',
PRIMARY KEY  (username),
KEY username (username)
) COMMENT='Postfix Admin - Virtual Mailboxes';

#
# Table structure for table vacation
#
CREATE TABLE vacation (
email varchar(255) NOT NULL default '',
subject varchar(255) NOT NULL default '',
body text NOT NULL,
cache text NOT NULL,
domain varchar(255) NOT NULL default '',
created datetime NOT NULL default '0000-00-00 00:00:00',
active tinyint(1) NOT NULL default '1',
PRIMARY KEY  (email),
KEY email (email)
) COMMENT='Postfix Admin - Virtual Vacation';</pre>
<p>4.2. Editar a senha para os usuários postfix e postfixadmin no postfixadmin-mysql.sql</p>
<p>4.3. Executa o sql no banco de dados</p>
<p><em>$ mysql -uroot -psenhaderoot &lt; postfixadmin-mysql.sql</em></p>
<p>4.4 Remove o arquivo sql</p>
<p><em>$ rm postfixadmin-mysql.sql</em></p>
<p><strong>5. Configurando os mapas do Postfix</strong></p>
<p>Uma vez que as tabelas foram criadas, configura o postfix para realizar o mapeamento editando cada um dos arquivos, e não esquecendo de alterar as credenciais de acesso ao banco de dados.</p>
<p><em>$ sudo vi /etc/postfix/mysql_virtual_alias_maps.cf</em></p>
<pre>user = postfix
password = postfixpassword
hosts = 127.0.0.1
dbname = postfix
table = alias
select_field = goto
where_field = address</pre>
<p><em>$ sudo vi /etc/postfix/mysql_virtual_domains_maps.cf</em></p>
<pre>user = postfix
password = postfixpassword
hosts = 127.0.0.1
dbname = postfix
table = domain
select_field = domain
where_field = domain
#additional_conditions = and backupmx = '0' and active = '1'</pre>
<p><em>$ sudo vi /etc/postfix/mysql_virtual_mailbox_maps.cf</em></p>
<pre>user = postfix
password = postfixpassword
hosts = 127.0.0.1
dbname = postfix
table = mailbox
select_field = maildir
where_field = username
#additional_conditions = and active = '1'</pre>
<p><em>$ sudo vi /etc/postfix/mysql_virtual_mailbox_limit_maps.cf</em></p>
<pre>user = postfix
password = postfixpassword
hosts = 127.0.0.1
dbname = postfix
table = mailbox
select_field = quota
where_field = username
#additional_conditions = and active = '1'</pre>
<p><em>$ sudo vi /etc/postfix/mysql_relay_domains_maps.cf</em></p>
<pre>user = postfix
password = postfixpassword
hosts = 127.0.0.1
dbname = postfix
table = domain
select_field = domain
where_field = domain
additional_conditions = and backupmx = '1'</pre>
<p>Alterar permissão dos mapas para somente root alterar e o postfix poder ler, visto que temos credenciais de acesso ao banco nos arquivos.<br />
<em>$ sudo chgrp postfix /etc/postfix/mysql_*.cf<br />
$ sudo chmod 640 /etc/postfix/mysql_*.cf</em></p>
<p>Criar usuário vmail para armazenar os e-mails de todos os vhosts, não necessitando assim uma conta no sistema para cada usuário<br />
<em>$ sudo groupadd -g 5000 vmail<br />
$ sudo useradd -m -g vmail -u 5000 -d /home/vmail -s /bin/bash vmail</em></p>
<p><strong>6. Configura o Postfix para Utilizar os Mapas</strong></p>
<p>Uma vez que temos o banco de dados criados, os arquivos que fazem o mapeamento, temos que configurar no Postfix para o mesmo utilizar cada um dos mapeamentos para determinada tarefa, como segue:</p>
<p><em>$ sudo vi /etc/postfix/main.cf</em></p>
<pre># Virtual Mailbox Domain Settings

virtual_alias_maps = mysql:/etc/postfix/mysql_virtual_alias_maps.cf
virtual_mailbox_domains = mysql:/etc/postfix/mysql_virtual_domains_maps.cf
virtual_mailbox_maps = mysql:/etc/postfix/mysql_virtual_mailbox_maps.cf
virtual_mailbox_limit = 51200000
virtual_minimum_uid = 5000
virtual_uid_maps = static:5000
virtual_gid_maps = static:5000
virtual_mailbox_base = /home/vmail
virtual_transport = virtual

# Additional for quota support

virtual_create_maildirsize = yes
virtual_mailbox_extended = yes
virtual_mailbox_limit_maps = mysql:/etc/postfix/mysql_virtual_mailbox_limit_maps.cf
virtual_mailbox_limit_override = yes
virtual_maildir_limit_message = Sorry, the your maildir has overdrawn your diskspace quota, please free up some of spaces of your mailbox try again.
virtual_overquota_bounce = yes</pre>
<p><strong>7. Configuração do Postfix</strong></p>
<p>Termina de realizar a configuração do Postfix para usar nossos certificados para o TLS e configurações básicas do mesmo.</p>
<p><em>$ sudo vi /etc/postfix/main.cf</em></p>
<pre># TLS parameters
smtpd_tls_cert_file = /etc/postfix/smtpd.cert
smtpd_tls_key_file = /etc/postfix/smtpd.key
smtpd_use_tls=yes
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

#The host name where your MX for virtual domains will point to
myhostname = mail.domain.com
mydestination = #Remains blank since we are going to host virtual domains
relayhost = #Remains blank unless you are going to use your ISP's SMTP server mail sending out mails. In which case it would be set to the host name of the ISP's SMTP server</pre>
<p>Deixe esses parâmetros com seus valores padrão</p>
<pre>alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
myorigin = /etc/mailname
mynetworks = &lt;seuip&gt;/32 127.0.0.1/32
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all</pre>
<p><strong>8. Autenticação de IMAP</strong></p>
<p>Configuramos este arquivo para o IMAP realizar a conexão ao banco de dados para validar cada tentativa de conexão dos usuários.</p>
<p>Alteração para usar o módulo mysql no courier authdaemon</p>
<p><em>$ sudo vi /etc/courier/authdaemonrc </em></p>
<pre>authmodulelist="authmysql authpam"</pre>
<p><em>$ sudo vi /etc/courier/authmysqlrc </em></p>
<pre>MYSQL_SERVER        127.0.0.1
MYSQL_USERNAME        postfixadmin
MYSQL_PASSWORD        &lt;senha postfixadmin&gt;
MYSQL_PORT            0
MYSQL_OPT            0
MYSQL_DATABASE        postfix
MYSQL_USER_TABLE    mailbox
MYSQL_CRYPT_PWFIELD    password
MYSQL_UID_FIELD        '5000'
MYSQL_GID_FIELD        '5000'
MYSQL_LOGIN_FIELD    username
MYSQL_HOME_FIELD    '/home/vmail'
MYSQL_NAME_FIELD    name
MYSQL_MAILDIR_FIELD    maildir
MYSQL_QUOTA_FIELD    concat(quota,'S')</pre>
<p>Reinicie os serviços e cheque os logs:</p>
<p><em>$ sudo /etc/init.d/courier-authdaemon restart<br />
$ sudo /etc/init.d/courier-imap restart<br />
$ sudo /etc/init.d/courier-imap-ssl restart<br />
$ sudo /etc/init.d/courier-pop restart<br />
$ sudo /etc/init.d/courier-pop-ssl restart<br />
$ sudo tail -f /var/log/mail.info</em></p>
<p><strong>9. Autenticação de SMTP</strong></p>
<p>Antes de mais nada para habilitar o saslauthd fazemos:<br />
<em>$ sudo vi /etc/default/saslauthd</em></p>
<pre>START=yes</pre>
<p>e verifique neste arquivo se os mecanismos estão configurados como:</p>
<pre>MECHANISMS="pam"</pre>
<p>e altere a opção OPTIONS:</p>
<pre>OPTIONS="-c -m /var/spool/postfix/var/run/saslauthd -r"</pre>
<p>e então habilite o servico:<br />
<em>$ sudo /etc/init.d/saslauthd start</em></p>
<p>Configuramos o Postfix para o mesmo somente aceitar envio de e-mails de usuários autenticados via sasl</p>
<p><em>$ sudo vi /etc/postfix/main.cf</em></p>
<pre>smtpd_recipient_restrictions = permit_mynetworks, permit_sasl_authenticated, reject_unauth_destination, permit
# modify the existing smtpd_sender_restrictions
smtpd_sender_restrictions = permit_sasl_authenticated, permit_mynetworks, reject_unauth_pipelining, permit
# then add these
smtpd_sasl_auth_enable = yes
broken_sasl_auth_clients = yes
smtpd_sasl_path = smtpd
smtpd_sasl_security_options = noanonymous
smtpd_sasl_local_domain =</pre>
<p>Cria o arquivo que diz para o Postfix como será a checagem da senha, no caso, via saslauthd<br />
<em>$ sudo vi /etc/postfix/sasl/smtpd.conf</em></p>
<pre>pwcheck_method: saslauthd
mech_list: PLAIN LOGIN
log_level: 5</pre>
<p>Configura o módulo 'smtp' no pam para que o sasl use este método para autenticar através do mesmo.<br />
<em>$ sudo vi /etc/pam.d/smtp</em></p>
<pre>auth    required   pam_mysql.so user=&lt;user do banco&gt; passwd=&lt;passwd do mysql&gt; host=127.0.0.1 db=postfix table=mailbox usercolumn=username passwdcolumn=password crypt=1
account sufficient pam_mysql.so user=&lt;user do banco&gt; passwd=&lt;passwd do mysql&gt; host=127.0.0.1 db=postfix table=mailbox usercolumn=username passwdcolumn=password crypt=1</pre>
<p>Como estamos utilizando nosso smtp em uma jail, temos que realizar as seguintes alterações:<br />
Crie o grupo sasl e adicione o usuário postfix ao mesmo adicionando esta linha no arquivo /etc/group<br />
<em>$ sudo vi /etc/group</em></p>
<pre>sasl:x:45:postfix</pre>
<p>Crie os arquivos/diretórios que ficarão dentro da jail para o postfix autenticar no sasl</p>
<pre>$ sudo mkdir -p /var/spool/postfix/var/run/
$ sudo mv /var/run/saslauthd /var/spool/postfix/var/run/saslauthd
$ sudo ln -ns /var/spool/postfix/var/run/saslauthd /var/run/saslauthd
$ sudo cp /etc/sasldb2 /var/spool/postfix/etc/
$ sudo chgrp sasl /var/spool/postfix/etc/sasldb2
$ sudo chmod g+w /var/spool/postfix/etc/sasldb2</pre>
<p>Reinicie os serviço e cheque o log<br />
<em>$ sudo /etc/init.d/courier-authdaemon restart<br />
$ sudo /etc/init.d/saslauthd restart<br />
$ sudo /etc/init.d/postfix restart<br />
$ sudo tail -f /var/log/mail.info</em></p>
<p>Uma vez que tenha adicionado um usuário no postfix (via inserção manual no banco ou usando o postfixadmin) pode testar a autenticação por sasl utilizando o seguinte comando:<br />
Testando usuário através do sasl<br />
<em>$ sudo testsaslauthd -s smtp -f /var/spool/postfix/var/run/saslauthd/mux -u 'user@vhost.com' -p senha</em></p>
<h2>Postfixadmin</h2>
<p>Baixe o postfixadmin na sua última versão, tenho usado em ambientes de produção e não tive nenhum problema com a mesma.</p>
<p><em>$ wget http://sourceforge.net/projects/postfixadmin/files/postfixadmin/postfixadmin_2.3rc5.tar.gz<br />
Descompacte o arquivo e copie para dentro do seu webroot</em></p>
<p><em>$ tar xvzf postfixadmin_2.3rc5.tar.gz</em><br />
<em>$ sudo mv postfixadmin-2.3rc5/ /var/www/postfixadmin/</em></p>
<p>Altere o arquivo de configuração para configurar o sistema de deixá-lo pronto para o setup</p>
<p><em>$ sudo vi /var/www/postfixadmin/config.inc.php</em></p>
<pre lang="php">$CONF['configured'] = true;

$CONF['database_type'] = 'mysqli';
$CONF['database_host'] = 'localhost';
$CONF['database_user'] = 'postfixadmin';
$CONF['database_password'] = '&lt;senha do postfixadmin&gt;';
$CONF['database_name'] = 'postfix';

$CONF['postfix_admin_url'] = '';
$CONF['admin_email'] = 'postmaster@change-this-to-your.domain.tld';

$CONF['domain_path'] = 'YES';
$CONF['domain_in_mailbox'] = 'NO';

# Customizações
$CONF['user_footer_link'] = "http://seudominio.com.br/postfixadmin";
$CONF['footer_text'] = 'Return to postfixmyadmin home';
$CONF['footer_link'] = 'http://seudominio.com.br/postfixadmin';

$CONF['welcome_text'] = &lt;&lt;&lt;EOM
Hi,

Welcome to your new account.
EOM;

$CONF['theme_logo'] = 'images/logo-default.png';
$CONF['theme_css'] = 'css/default.css';</pre>
<p>Acesse o setup.php em http://seudominio.com.br/postfixadmin/setup.php<br />
Coloque a senha da instalação e ao gerar o hash, copie-o para:</p>
<pre lang="php">$CONF['setup_password'] = 'changeme'</pre>
<p>Novamente acesse o setup.php em http://seudominio.com.br/postfixadmin/setup.php e crie as credenciais do seu usuário administrador e agora seu postfixadmin já está pronto para ser acessado e já podem ser criadas as contas.</p>
<h2>SquirrelMail</h2>
<p>Instalação do squirrelmail via apt<br />
<em>$ sudo apt-get install squirrelmail</em></p>
<p>Configure o squirrelmail utilizando seu configurador (customizações devem ser feitas nesse passo) nenhum configuração adicional é necessária para o nosso sitema.<br />
<em>$ sudo squirrelmail-configure</em></p>
<p>Copie o arquivo de configuração para usar o squirrelmail no apache, se quiser mudar a localização de /squirrelmail para /webmail por exemplo, altere na linha que contem o Alias<br />
<em>$ sudo cp /etc/squirrelmail/apache.conf /etc/apache2/sites-available/squirrelmail</em></p>
<p>Habilite o vhost do squirrelmail<br />
<em>$ sudo a2ensite squirrelmail</em></p>
<p>Reinicie o Apache<br />
<em>$ sudo /etc/init.d/apache2 force-reload</em></p>
