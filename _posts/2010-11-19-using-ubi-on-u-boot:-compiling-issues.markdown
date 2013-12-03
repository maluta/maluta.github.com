---
layout: post
title: using ubi on u-boot: compiling issues
tags: [oldblog]
---

<small>[Warning: This post is a backup recovery from my previous Wordpress blog. All content was automatically converted accessing a MySQL database using a Python script (<a href="http://maluta.github.io/blog/convert-wordpress-to-jekyll/">details</a>). Mostly are in Portuguese but if you are interesent I can translate to English. If you found any problem dont't hesitate to contact me in comments.]</small>



if you are adding support to ubifs on u-boot, you must add some ?<em>include/configs/&lt;CONFIG&gt;.h</em>
<p style="padding-left: 30px;">?#define CONFIG_CMD_UBI
#define CONFIG_CMD_UBIFS
<strong> #define CONFIG_RBTREE</strong>
#define CONFIG_LZO</p>

<div id="_mcePaste">to avoid errors like:</div>
<p style="padding-left: 30px;">/uboot-imx/fs/ubifs/tnc.c:105: undefined reference to `rb_insert_color'
fs/ubifs/libubifs.a(orphan.o): In function `insert_dead_orphan':
/uboot-imx/fs/ubifs/orphan.c:129: undefined reference to `rb_insert_color'
fs/ubifs/libubifs.a(recovery.o): In function `add_ino':
/uboot-imx/fs/ubifs/recovery.c:1050: undefined reference to `rb_insert_color'
fs/ubifs/libubifs.a(recovery.o): In function `remove_ino':
/uboot-imx/fs/ubifs/recovery.c:1088: undefined reference to `rb_erase'
fs/ubifs/libubifs.a(recovery.o): In function `ubifs_recover_size':
/uboot-imx/fs/ubifs/recovery.c:1171: undefined reference to `rb_first'
/uboot-imx/fs/ubifs/recovery.c:1214: undefined reference to `rb_next'
/uboot-imx/fs/ubifs/recovery.c:1220: undefined reference to `rb_next'
/uboot-imx/fs/ubifs/recovery.c:1221: undefined reference to `rb_erase'
fs/ubifs/libubifs.a(replay.o): In function `insert_node':
/uboot-imx/fs/ubifs/replay.c:373: undefined reference to `rb_insert_color'
fs/ubifs/libubifs.a(replay.o): In function `insert_dent':
/uboot-imx/fs/ubifs/replay.c:448: undefined reference to `rb_insert_color'
fs/ubifs/libubifs.a(replay.o): In function `insert_ref_node':
/uboot-imx/fs/ubifs/replay.c:689: undefined reference to `rb_insert_color'
fs/ubifs/libubifs.a(replay.o): In function `apply_replay_tree':
/uboot-imx/fs/ubifs/replay.c:306: undefined reference to `rb_next'
/uboot-imx/fs/ubifs/replay.c:294: undefined reference to `rb_first'</p>
obs.: probably you will need add MTD part support too :)