---
layout: post
title: Welcome back NGW100!
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;">A some time ago I've <a href="http://en.wikipedia.org/wiki/Bricked" target="_blank">bricked</a> my NGW100 board by overwritten the U-boot from flash. To fix it was necessary using a JTAG interface, so I check some alternatives.</p>

<ul>
	<li>AVR JTAGICE mkII (US$ 299) [official] <a href="http://atmel.com/dyn/products/tools_card.asp?tool_id=3353">http://atmel.com/dyn/products/tools_card.asp?tool_id=3353</a></li>
	<li>AVR JTAG ICE mkii CN (US$ 99)  <a href="http://enshop.avrvi.com/avrjtagicemkiicn.html">http://enshop.avrvi.com/avrjtagicemkiicn.html</a></li>
	<li>AT AVR JTAGICE mkII clone (US$ 159) <a href="http://enshop.avrvi.com/jtagicemkiiclone.html">http://enshop.avrvi.com/jtagicemkiiclone.html</a></li>
</ul>
<p style="text-align: justify;">Considering that NGW100 itself costs about US$ 89.00 could be more cheaper get another board than buying a JTAG device. Note that I looking for way to allow a programming Interface to flash and not other features available in a JTAG like source level debugging.</p>
<p style="text-align: center;"><img class="aligncenter size-medium wp-image-737" title="ngw100+byteblaster" src="http://www.coding.com.br/wp-content/uploads/2010/03/ngw100+byteblaster-300x225.jpg" alt="" width="300" height="225" /> The bootloader for the NGW is stored in the parallell flash</p>
<p style="text-align: justify;">Searching for a inexpensive solution I found this AVR Freaks <a href="http://www.avrfreaks.net/index.php?name=PNphpBB2&amp;file=viewtopic&amp;t=53865" target="_blank">thread</a> teaching how to use cable <a href="http://jtag-arm9.sourceforge.net/circuit.txt" target="_blank">wiggler</a> or byteblaster to flash NGW.  Everyone that used Altera FPGA at least one time know about Byteblaster cable, was easy found one at university and try (thanks Prof. Robson Moreno)</p>
<p style="text-align: left;"></p>
<p style="text-align: center;"><img class="aligncenter size-medium wp-image-746" title="Byteblaster cable" src="http://www.coding.com.br/wp-content/uploads/2010/03/bbla-300x163.png" alt="" width="300" height="163" />I'm using Byteblaser I</p>
<p style="text-align: left;">I've compiled a new u-boot binary from BSP code and used a too called <a href="http://194.204.26.104/~andrei/avrfreaks/avr32prog.zip" target="_blank">avr32prog</a> (it's windows-only) to record.</p>

<pre style="text-align: left;">avr32prog.exe -c byteblaster -p LPT1 -f u-boot.img prog
</pre>
<p style="text-align: center;"><span style="color: #ff0000;">The process is extremely slow, about 35 minutes to flash a 100kbyte binary (~ 50bps)</span></p>
<p style="text-align: justify;">I have not had success the first time due some kind of "writing error". I noted that if I use the computer (i.e.: browsing) when avr32prog is running the error happens faster, so I started the program a let flash the board "alone". After finished just turn off the board, unplug JTAG connector and turn on the board again. It's nice to see serial working again :-)</p>

<blockquote>
U-Boot 1.1.4-at0 (Mar  9 2010 - 01:55:04) 

U-Boot code: 00000000 -> 000149cf  data: 24000000 -> 24002d80
SDRAM: 32 MB at address 0x10000000
Testing SDRAM...OK
malloc: Using memory from 0x11fc0000 to 0x12000000
Flash:  8 MB at address 0x00000000
DRAM Configuration:
Bank #0: 10000000 32 MB

In:    serial
Out:   serial
Err:   serial

Net:   macb0, macb1
Press SPACE to abort autoboot in 1 seconds
Uboot> 
</blockquote>

