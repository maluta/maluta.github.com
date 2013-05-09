---
layout: post
title: Android CTS 
---

Run CTS on Android isn't straightforward. Probably you I'll have some test cases failing so I'll try to register my experience running it against Android 2.3.x.

### GOLDEN RULE FOR FAILED TESTS ###
run the test individually like "cts start --plan CTS -p aaaa.bbbb.cccc.dddd#eeee" then use "adb logcat" to find the exception or errors.

