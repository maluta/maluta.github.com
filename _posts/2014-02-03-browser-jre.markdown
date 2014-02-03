---	
layout: post
title: Browser and Java (a.k.a JRE)
---

Personal note do install JRE, if needed ([check it](http://java.com/en/download/installed.jsp?detect=jre))

**Steps**

1. [Download](http://www.java.com/en/download/manual.jsp) the latest version (at time it's Version 7 Update 51) and save in some directory, in my case I usually copy to  `/opt`.

2. Within the chosen directory, runn the following command on your `shell`: 

```bash
		tar zxvf jre-7u51-linux-x64.tar.gz
		ln -sf jre1.7.0\_51 jre
		ln -sf `pwd`/jre/lib/amd64/libnpjp2.so /usr/lib/mozilla/plugins/
```

3. Restart it, eg.: `killall firefox` :)

4. [Re-check](http://java.com/en/download/installed.jsp?detect=jre)

