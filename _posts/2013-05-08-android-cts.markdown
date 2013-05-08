---
layout: post
title: Android CTS 
---

Run CTS on Android isn't straightforward. Probably you I'll have some test cases failing so I'll try to register my experience running it against Android 2.3.x.

### GOLDEN RULE ###
run the test individually like "cts start --plan CTS -p xxxx.xxxx.xxxx" then use "adb logcat" to find the exception or errors.

