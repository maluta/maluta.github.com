---
layout: post
title: TV Digital: uma introduo
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: right;"><em>Esse post não irá falar do Ginga.</em></p>
<p style="text-align: justify;">Atualmente estou dedicando um tempo no estudo da norma brasileira de TV Digital, vou tentar documentar estas "descobertas". Meu foco inicial é nos mecanismos de transmissão, particularmente no <em>Transport Stream</em>. Não sou um especialista muito menos vinculado a alguma instituição que faz pesquisa na área, mas quero mostrar alguns conceitos e aplicações práticas, por isso, é importante o leitor buscar outras fontes que explicam melhor a teoria e se necessário, por favor, me corrija.</p>
Um breve histório: O padrão brasileiro de televisão digitial foi criado em conjunto com o Fórum de TV Digital e a ABNT. As normas são referentes a:
<ul>
	<li>Transmissão (ABNT NBR 15601)</li>
	<li>Conpresão de Audio e Video (ABNT NBR 15602)</li>
	<li>Multiplexação e Serviços de Informação (SI) (ABNT NBR 15603)</li>
	<li>Receptores (ABNT NBR 15604)</li>
	<li>Segurança (ABNT NBR 15605)</li>
	<li>Codificação de Dados (ABNT NBR 15606)</li>
	<li>Canal de Interatividade (ABNT NBR 15607)</li>
	<li>Diretivas de Operação (ABNT NBR 15608)</li>
	<li>Suites de Testes para o Middleware (ABNT NBR 15609)</li>
	<li>Certificação dos receptores (ABNT NBR 15610)</li>
</ul>
<p style="text-align: justify;">Como mencionado, <em>a priori </em>vamos focar no <em>Transport Stream (TS)</em> que um protocolo de comunicação para audio, video e dados. É um tipo de "recipiente" que pode conter vários formatos que são separados no mesmo arquivo.</p>
<p style="text-align: justify;">Dois tipos de pacotes foram padronizados para os sinais gerados pelo <strong>MPEG</strong>: um chamado <em><strong>Program Stream</strong></em><em> </em>que é otimizado para um armazenamento eficiente e assume que o decodificador tem acesso ao <em>stream </em>completo para fins de sincronização; já o outro outro, o <em><strong>Transport Stream</strong></em> foi projetado para transmitir os dados em tempo real mesmo em um meio não-confiável (o ar) sendo que o receptor pode começar a "ler" os dados da fonte a partir de qualquer momento (e não necessariamente no começo da transmissão), por isso é usado na transmissão ISDB-Tb (incluindo também DVB e ATSC). Em linhas gerais, o <em>Program Stream </em>é usado, por exemplo, num CD ou DVD e o <em>Transport Stream</em> para uma transmissão de televisão. Para que este mecanismo funcione, é adicionado regularmente ao <em>stream</em> uma informação de tempo (<em>timestamps</em>) fazendo com que a sincronização dos pacotes seja agrupada relativo ao <em>timestamp</em> mais recente ao invés de um ponto inicial apenas no começo da transmissão. O TS está especificado na norma <a href="http://neuron2.net/library/mpeg2/iso13818-1.pdf">ISO/IEC 13818-1</a>.</p>
<p style="text-align: justify;">O TS utiliza o conceito de programas. Cada programa é descrito numa tabela chamada PMT (<em>Program Map Table</em>) na qual possui um único PID (Program ID) e os <em>elementary streams</em> associados a este PID. Por exemplo: um<em> transport stream</em> utilizado na televisão digital pode conter três programas, para representar três canais de televisão. Suponha que cada canal consista de um video diferente, um ou dois <em>streams</em> de audio (ex.: o audio dublado e original) e qualquer meta-informação necessária (ex.: sinopse do filme). O teleespectador querendo assistir a um canal particular apenas tem que decodificar os <em>payloads</em> de cada PID associado ao programa escolhido. Ele pode ignorar o conteúdo do resto. Um transport stream com mais de um programa é chamado MPTS (<em>Multi Program Transport Stream</em>) e um <em>transport stream</em> com um único programa é chamado SPTS (<em>Single Program Transport Stream</em>)</p>
<p style="text-align: justify;">Nesta série de <em>posts</em> vou me concentrar nas "meta-informações" - qualquer informação que não o <em>payload</em> - do <em>transport stream</em>, ou seja, aquilo que caracteriza o protocolo e não propriamente no conteúdo. Na prática, se abrirmos um arquivo TS através de um editor hexadecimal (ex: hexdump) notaremos nos primeiros <em>bytes</em> alguma coisa do tipo:</p>

<pre>00000000 <strong>47</strong> 40 00 10 00 00 b0 11 00 01 c1 00 00 00 00 e0
00000010 1f 00 01 e1 00 24 ac 48 84 ff ff ff ff ff ff ff</pre>
<p style="text-align: justify;">Contudo é impossível analisar um <em>Transport Stream</em> pelo <em>dump</em> do TS pois a construção dele é dinâmica. O primeiro erro que cometi foi pensar que era facil extrair o video de dentro do TS apenas "removendo" as informações que não eram pertinentes.  (Isso é até possível, mas meus testes foram restritos, espero fazer um <em>post</em> a parte sobre o tema) Deste começo, a única informação confiavel (que não muda) é o primeiro byte 0x47 referente ao sincronismo. Estruturalmente podemos pensar o cabeçalho como algo:</p>

<pre lang="cpp">struct ts_header {
uint8_t sync_byte;
uint16_t transport_error_indicator:1;
uint16_t payload_unit_start_indicator:1;
uint16_t transport_priority:1;
uint16_t pid:13;
uint8_t transport_scrambling_control:2;
uint8_t adaptation_field:2;
uint8_t continuity_counter:4;
} __attribute__((__packed__));

struct adaptation_field {
uint8_t length;
uint8_t discontinuity_indicator:1;
} __attribute__((__packed__));</pre>
<p style="text-align: justify;">Existem diversas bibliotecas para a manipulação do TS. Uma delas é a <strong>libdvbpsi</strong> que foi desenvolvida para decodificar e gerar tabelas do MPEG TS e DVB PSI. No site diz que roda nas plataformas GNU/Linux, Windows e Mac OS X.</p>
<p style="text-align: justify;">Bom, isso foi apenas uma introdução, pretendo ir publicando meus avanços por aqui... Lembre-se não é um tópico fácil, estou conversando com bastante gente e tirando dúvidas básicas, muitas delas referente a especificação na norma.</p>
--tm