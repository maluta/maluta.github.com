---
layout: post
title: TV Digital uma introduo
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: right;"><em>Esse post no ir falar do Ginga.</em></p>
<p style="text-align: justify;">Atualmente estou dedicando um tempo no estudo da norma brasileira de TV Digital, vou tentar documentar estas "descobertas". Meu foco inicial  nos mecanismos de transmisso, particularmente no<em>Transport Stream</em>. No sou um especialista muito menos vinculado a alguma instituio que faz pesquisa na rea, mas quero mostrar alguns conceitos e aplicaes prticas, por isso,  importante o leitor buscar outras fontes que explicam melhor a teoria e se necessrio, por favor, me corrija.</p>
Um breve histrio: O padro brasileiro de televiso digitial foi criado em conjunto com o Frum de TV Digital e a ABNT. As normas so referentes a:
<ul>
	<li>Transmisso (ABNT NBR 15601)</li>
	<li>Conpreso de Audio e Video (ABNT NBR 15602)</li>
	<li>Multiplexao e Servios de Informao (SI) (ABNT NBR 15603)</li>
	<li>Receptores (ABNT NBR 15604)</li>
	<li>Segurana (ABNT NBR 15605)</li>
	<li>Codificao de Dados (ABNT NBR 15606)</li>
	<li>Canal de Interatividade (ABNT NBR 15607)</li>
	<li>Diretivas de Operao (ABNT NBR 15608)</li>
	<li>Suites de Testes para o Middleware (ABNT NBR 15609)</li>
	<li>Certificao dos receptores (ABNT NBR 15610)</li>
</ul>
<p style="text-align: justify;">Como mencionado,<em>a priori </em>vamos focar no<em>Transport Stream (TS)</em> que um protocolo de comunicao para audio, video e dados.  um tipo de "recipiente" que pode conter vrios formatos que so separados no mesmo arquivo.</p>
<p style="text-align: justify;">Dois tipos de pacotes foram padronizados para os sinais gerados pelo <strong>MPEG</strong>: um chamado<em><strong>Program Stream</strong></em><em> </em>que  otimizado para um armazenamento eficiente e assume que o decodificador tem acesso ao<em>stream </em>completo para fins de sincronizao; j o outro outro, o<em><strong>Transport Stream</strong></em> foi projetado para transmitir os dados em tempo real mesmo em um meio no-confivel (o ar) sendo que o receptor pode comear a "ler" os dados da fonte a partir de qualquer momento (e no necessariamente no comeo da transmisso), por isso  usado na transmisso ISDB-Tb (incluindo tambm DVB e ATSC). Em linhas gerais, o<em>Program Stream </em> usado, por exemplo, num CD ou DVD e o<em>Transport Stream</em> para uma transmisso de televiso. Para que este mecanismo funcione,  adicionado regularmente ao<em>stream</em> uma informao de tempo (<em>timestamps</em>) fazendo com que a sincronizao dos pacotes seja agrupada relativo ao<em>timestamp</em> mais recente ao invs de um ponto inicial apenas no comeo da transmisso. O TS est especificado na norma <a href="http://neuron2.net/library/mpeg2/iso13818-1.pdf">ISO/IEC 13818-1</a>.</p>
<p style="text-align: justify;">O TS utiliza o conceito de programas. Cada programa  descrito numa tabela chamada PMT (<em>Program Map Table</em>) na qual possui um nico PID (Program ID) e os<em>elementary streams</em> associados a este PID. Por exemplo: um<em> transport stream</em> utilizado na televiso digital pode conter trs programas, para representar trs canais de televiso. Suponha que cada canal consista de um video diferente, um ou dois<em>streams</em> de audio (ex.: o audio dublado e original) e qualquer meta-informao necessria (ex.: sinopse do filme). O teleespectador querendo assistir a um canal particular apenas tem que decodificar os<em>payloads</em> de cada PID associado ao programa escolhido. Ele pode ignorar o contedo do resto. Um transport stream com mais de um programa  chamado MPTS (<em>Multi Program Transport Stream</em>) e um<em>transport stream</em> com um nico programa  chamado SPTS (<em>Single Program Transport Stream</em>)</p>
<p style="text-align: justify;">Nesta srie de <em>posts</em> vou me concentrar nas "meta-informaes" - qualquer informao que no o<em>payload</em> - do<em>transport stream</em>, ou seja, aquilo que caracteriza o protocolo e no propriamente no contedo.Na prtica, se abrirmos um arquivo TS atravs de um editor hexadecimal (ex: hexdump) notaremos nos primeiros<em>bytes</em> alguma coisa do tipo:</p>

<pre>00000000 <strong>47</strong> 40 00 10 00 00 b0 11 00 01 c1 00 00 00 00 e0
00000010 1f 00 01 e1 00 24 ac 48 84 ff ff ff ff ff ff ff</pre>
<p style="text-align: justify;">Contudo  impossvel analisar um <em>Transport Stream</em> pelo <em>dump</em> do TS pois a construo dele  dinmica. O primeiro erro que cometi foi pensar que era facil extrair o video de dentro do TS apenas "removendo" as informaes que no eram pertinentes. (Isso  at possvel, mas meus testes foram restritos, espero fazer um <em>post</em> a parte sobre o tema) Deste comeo, a nica informao confiavel (que no muda)  o primeiro byte 0x47 referente ao sincronismo. Estruturalmente podemos pensar o cabealho como algo:</p>

<pre lang="cpp">structts_header{
uint8_t sync_byte;
uint16_t transport_error_indicator:1;
uint16_t payload_unit_start_indicator:1;
uint16_t transport_priority:1;
uint16_t pid:13;
uint8_t transport_scrambling_control:2;
uint8_t adaptation_field:2;
uint8_t continuity_counter:4;
}__attribute__((__packed__));

structadaptation_field{
uint8_t length;
uint8_t discontinuity_indicator:1;
}__attribute__((__packed__));</pre>
<p style="text-align: justify;">Existem diversas bibliotecas para a manipulao do TS. Uma delas  a<strong>libdvbpsi</strong> que foi desenvolvida para decodificar e gerar tabelas do MPEG TS e DVB PSI. No site diz que roda nas plataformas GNU/Linux, Windows e Mac OS X.</p>
<p style="text-align: justify;">Bom, isso foi apenas uma introduo, pretendo ir publicando meus avanos por aqui... Lembre-se no  um tpico fcil, estou conversando com bastante gente e tirando dvidas bsicas, muitas delas referente a especificao na norma.</p>
--tm