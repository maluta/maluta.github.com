---
layout: post
title: AT commands 
---

Suppose you must validate some modem through AT commands. You could follow some steps: checking if antenna is functional, gather IMSI and IMEI number, get network registration status and controls, get operator name and dial a valid number and so on...

    AT+CFUN?
    AT+CPIN?
    AT+CIMI
    AT+CGSN
    AT+CREG?
    AT+COPS?
    ATD+<NUMBER>;

You can enter any program that access serial interface (minicom, [picocom](http://code.google.com/p/picocom/), etc) to type this commands, but if you like to automate your steps:

<script src="https://gist.github.com/maluta/7775063.js"></script>

Reference:
    [List of AT Commands](http://www.shapeshifter.se/2008/04/30/list-of-at-commands/)

