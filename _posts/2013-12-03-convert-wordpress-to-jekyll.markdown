---
layout: post
title: Converting a Wordpress blog to Jekyll (GitHub Pages)
---

I had a plenty of _old posts_ from a previous Wordpress blog. Since I'm [using](http://maluta.github.io/blog/hello-world/) GitHub pages (powered by [Jekyll](http://jekyllrb.com/) engine) I'll describe my steps if you need to do the same.

To import the backup file into a fresh new instance of MySQL, you can simply use the **mysql** command to import the data:

		mysql -u root -p < myoldblog.sql

Now with db access I need to extract the relevant information from each post, basically: _date_, _title_ and _content_. You don't need to be a database expert to get this information, a simple SQL query should work.

		SELECT post_date, post_title, post_content FROM wp_posts 
        	WHERE post_status="publish" and post_type="post";

I restricted my query to published posts. In other words, I'm not interested in _static pages_ and _drafts_ from Wordpress.

I counted 86 published posts... and perform this task by hand isn't a wise option. In order to automate this process I've created a Python script that generates the correct Jekyll page for me. Nowadays I use [markdown](http://daringfireball.net/projects/markdown/) syntax to write but Jekyll also supports plain HTML so I didn't bother to convert it. 

Each post has a template for filename (**YYYY-MM-DD-title.markdown**) and page content:

		---
		layout: post
		title: post title
		---

		{html content}

Some notes:

* Don't forget to fill your credentials to access MySQL db.
* I had *a lot* of problems with UTF-8 chars and not figure out yet a good way to fix it. If you content has non-ascii chars they will disappear. 
* To avoid some naming problems I replaced some chars, maybe you need more. 
* This script don't get any other data than text (images and post comments are missing) 

<br>
<script src="https://gist.github.com/maluta/7791137.js"></script>

I strongly recommend use a local instance of Jekyll before publish on GitHub. If something goes wrong GitHub will only email you with a _"Page build failure"_ and no more details. When you push 86 files find the problem can be a mess. If you don't know how to install check this [instructions](https://help.github.com/articles/using-jekyll-with-pages).

The final result wasn't perfect (especially the missing chars in posts written in Portuguese) but fit my needs and now I'm able to polish each post individually. 





