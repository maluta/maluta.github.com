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

    #!/usr/bin/python 
    import serial
    import re
    import time

    device="/dev/ttyACM0" # modem interface

    class Modem:

        def __init__(self):
            try:
                file = open(device, "r")
            except IOError:
                print "could not opem modem interface: ", device
                exit()
            self.ser=serial.Serial(device,19200,timeout=3)
            self.ser.write("ATZ\r")
            line=self.ser.read(10)

        def readuntil(self,word):
            ol=[]
            while 1:
                c=self.ser.read()
                if not c:
                    break
                ol.append(c)
                ostring="".join(ol)
                if len(ol)>len(word)+1 and ostring[-4:]=="%s\r\n" % word:
                    break
            return ostring

        def cmd(self,cmd):
            self.ser.write(cmd+"\r")
            r=self.readuntil("OK")
            r=r.split("\n")
            for i in range(len(r)):
                r[i]=r[i][:-1]
            return r

        def close(self):
            self.ser.close()


    if __name__ == "__main__":

        m = Modem()

        AT_LIST = ["AT+CFUN?","AT+CPIN?","AT+CIMI","AT+CGSN","AT+CREG?","AT+COPS?","ATD+97314686;"]

        for cmd in AT_LIST:
            print m.cmd(cmd)[1]
            time.sleep(1)

        time.sleep(15) # wait and then end call
        m.cmd("ATZ")[1]

        m.close()



Reference:
    [List of AT Commands](http://www.shapeshifter.se/2008/04/30/list-of-at-commands/)

