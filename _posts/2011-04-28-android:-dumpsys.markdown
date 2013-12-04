---
layout: post
title: android dumpsys
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interest I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



<p style="text-align: justify;"><!-- p { margin-bottom: 0.08in; }td p { margin-bottom: 0in; } -->Android has an interesting command called <em>dumpsys</em> to dump some system information. Even described on <a href="http://developer.android.com/guide/developing/tools/adb.html" target="_blank">adb manual</a> I think that some points should be reinforced. In order to get the complete status just run (will produce a large output):</p>

<h4 style="padding-left: 30px;">adb shell dumpsys</h4>
Also you can apply filters to running services:
<table border="0" cellspacing="0" cellpadding="4" width="100%">
<tbody>
<tr valign="TOP">
<td width="33%">1	SurfaceFlinger

2	accessibility

3	account

4	activity

5	alarm

6	appwidget

7	audio

8	backup

9	battery

10	batteryinfo

11	bluetooth

12	bluetooth_a2dp

13	clipboard

14	connectivity

15	content

16	<strong>cpuinfo</strong>

17	device_policy</td>
<td width="33%">18	devicestoragemonitor

19	diskstats

20	dropbox

21	entropy

22	ethernet

23	hardware

24	input_method

25	iphonesubinfo

26	isms

27	keybar

28	location

29	media.audio_flinger

30	media.audio_policy

31	media.camera

32	media.player

33	meminfo

34	mount

35	netstat</td>
<td width="33%">36	network_management

37	notification

38	package

39	permission

40	phone

41	power

42	search

43	sensor

44	simphonebook

45	statusbar

46	telephony.registry

47	throttle

48	uimode

49	usagestats

50	vibrator

51	wallpaper

52	<strong>wifi</strong>

53	window</td>
</tr>
</tbody>
</table>
Some examples:
<h4 style="padding-left: 30px;">adb shell dumpsys wifi</h4>
<h4 style="padding-left: 30px;">adb shell dumpsys cpuinfo</h4>
<p style="text-align: justify;">I suggest you try other items on the list above and be creative using all the power of Unix pipes. Example, to get all memory allocated by each process you can do something like:</p>

<pre style="padding-left: 30px;">adb shell dumpsys meminfo | grep "allocated:" | awk '{total = total + $5}END{print total}'</pre>