---
layout: post
title: TV Digital: uma introduo
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: right;"><em>Esse post n�o ir� falar do Ginga.</em></p>
<p style="text-align: justify;">Atualmente estou dedicando um tempo no estudo da norma brasileira de TV Digital, vou tentar documentar estas "descobertas". Meu foco inicial � nos mecanismos de transmiss�o, particularmente no�<em>Transport Stream</em>. N�o sou um especialista muito menos vinculado a alguma institui��o que faz pesquisa na �rea, mas quero mostrar alguns conceitos e aplica��es pr�ticas, por isso, � importante o leitor buscar outras fontes que explicam melhor a teoria e se necess�rio, por favor, me corrija.</p>
Um breve hist�rio: O padr�o brasileiro de televis�o digitial foi criado em conjunto com o F�rum de TV Digital e a ABNT. As normas s�o referentes a:
<ul>
	<li>Transmiss�o (ABNT NBR 15601)</li>
	<li>Conpres�o de Audio e Video (ABNT NBR 15602)</li>
	<li>Multiplexa��o e Servi�os de Informa��o (SI) (ABNT NBR 15603)</li>
	<li>Receptores (ABNT NBR 15604)</li>
	<li>Seguran�a (ABNT NBR 15605)</li>
	<li>Codifica��o de Dados (ABNT NBR 15606)</li>
	<li>Canal de Interatividade (ABNT NBR 15607)</li>
	<li>Diretivas de Opera��o (ABNT NBR 15608)</li>
	<li>Suites de Testes para o Middleware (ABNT NBR 15609)</li>
	<li>Certifica��o dos receptores (ABNT NBR 15610)</li>
</ul>
<p style="text-align: justify;">Como mencionado,�<em>a priori </em>vamos focar no�<em>Transport Stream (TS)</em> que um protocolo de comunica��o para audio, video e dados. � um tipo de "recipiente" que pode conter v�rios formatos que s�o separados no mesmo arquivo.</p>
<p style="text-align: justify;">Dois tipos de pacotes foram padronizados para os sinais gerados pelo <strong>MPEG</strong>: um chamado�<em><strong>Program Stream</strong></em><em> </em>que � otimizado para um armazenamento eficiente e assume que o decodificador tem acesso ao�<em>stream </em>completo para fins de sincroniza��o; j� o outro outro, o�<em><strong>Transport Stream</strong></em> foi projetado para transmitir os dados em tempo real mesmo em um meio n�o-confi�vel (o ar) sendo que o receptor pode come�ar a "ler" os dados da fonte a partir de qualquer momento (e n�o necessariamente no come�o da transmiss�o), por isso � usado na transmiss�o ISDB-Tb (incluindo tamb�m DVB e ATSC). Em linhas gerais, o�<em>Program Stream </em>� usado, por exemplo, num CD ou DVD e o�<em>Transport Stream</em> para uma transmiss�o de televis�o. Para que este mecanismo funcione, � adicionado regularmente ao�<em>stream</em> uma informa��o de tempo (<em>timestamps</em>) fazendo com que a sincroniza��o dos pacotes seja agrupada relativo ao�<em>timestamp</em> mais recente ao inv�s de um ponto inicial apenas no come�o da transmiss�o. O TS est� especificado na norma <a href="http://neuron2.net/library/mpeg2/iso13818-1.pdf">ISO/IEC 13818-1</a>.</p>
<p style="text-align: justify;">O TS utiliza o conceito de programas. Cada programa � descrito numa tabela chamada PMT (<em>Program Map Table</em>) na qual possui um �nico PID (Program ID) e os�<em>elementary streams</em> associados a este PID. Por exemplo: um<em> transport stream</em> utilizado na televis�o digital pode conter tr�s programas, para representar tr�s canais de televis�o. Suponha que cada canal consista de um video diferente, um ou dois�<em>streams</em> de audio (ex.: o audio dublado e original) e qualquer meta-informa��o necess�ria (ex.: sinopse do filme). O teleespectador querendo assistir a um canal particular apenas tem que decodificar os�<em>payloads</em> de cada PID associado ao programa escolhido. Ele pode ignorar o conte�do do resto. Um transport stream com mais de um programa � chamado MPTS (<em>Multi Program Transport Stream</em>) e um�<em>transport stream</em> com um �nico programa � chamado SPTS (<em>Single Program Transport Stream</em>)</p>
<p style="text-align: justify;">Nesta s�rie de <em>posts</em> vou me concentrar nas "meta-informa��es" - qualquer informa��o que n�o o�<em>payload</em> - do�<em>transport stream</em>, ou seja, aquilo que caracteriza o protocolo e n�o propriamente no conte�do.�Na pr�tica, se abrirmos um arquivo TS atrav�s de um editor hexadecimal (ex: hexdump) notaremos nos primeiros�<em>bytes</em> alguma coisa do tipo:</p>

<pre>00000000 <strong>47</strong> 40 00 10 00 00 b0 11 00 01 c1 00 00 00 00 e0
00000010 1f 00 01 e1 00 24 ac 48 84 ff ff ff ff ff ff ff</pre>
<p style="text-align: justify;">Contudo � imposs�vel analisar um <em>Transport Stream</em> pelo <em>dump</em> do TS pois a constru��o dele � din�mica. O primeiro erro que cometi foi pensar que era facil extrair o video de dentro do TS apenas "removendo" as informa��es que n�o eram pertinentes.� (Isso � at� poss�vel, mas meus testes foram restritos, espero fazer um <em>post</em> a parte sobre o tema) Deste come�o, a �nica informa��o confiavel (que n�o muda) � o primeiro byte 0x47 referente ao sincronismo. Estruturalmente podemos pensar o cabe�alho como algo:</p>

<pre lang="cpp">struct�ts_header�{
uint8_t sync_byte;
uint16_t transport_error_indicator:1;
uint16_t payload_unit_start_indicator:1;
uint16_t transport_priority:1;
uint16_t pid:13;
uint8_t transport_scrambling_control:2;
uint8_t adaptation_field:2;
uint8_t continuity_counter:4;
}�__attribute__((__packed__));

struct�adaptation_field�{
uint8_t length;
uint8_t discontinuity_indicator:1;
}�__attribute__((__packed__));</pre>
<p style="text-align: justify;">Existem diversas bibliotecas para a manipula��o do TS. Uma delas � a�<strong>libdvbpsi</strong> que foi desenvolvida para decodificar e gerar tabelas do MPEG TS e DVB PSI. No site diz que roda nas plataformas GNU/Linux, Windows e Mac OS X.</p>
<p style="text-align: justify;">Bom, isso foi apenas uma introdu��o, pretendo ir publicando meus avan�os por aqui... Lembre-se n�o � um t�pico f�cil, estou conversando com bastante gente e tirando d�vidas b�sicas, muitas delas referente a especifica��o na norma.</p>
--tm