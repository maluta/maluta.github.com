---
layout: draft
title: Drafts
permalink: /drafts/
---

<div class="posts clearfix">
  {% for post in site.posts %}
  {% if post.draft == true %}
  <article class="post">
      <div class="eyebrow">{{ post.date | date: "%d %b %Y" }}</div>
      <h1><a href="{{ site.baseurl }}{{ post.url }}" style="font-family: 'EB Garamond', serif;">{{ post.title }}</a></h1>
      <!--<a href="{{ site.baseurl }}{{ post.url }}"><img src="images/{{ post.url | remove: "/" }}.png" alt="post img" /></a> -->
      <div class="entry">
      <!--<p>{{ post.desc }}</p>
         {{ post.content | truncatewords:40}}
 -->  </div>

<!--  <a href="{{ post.proj-url }}" class="small-link primary-link" target="_blank">View Project Site <i class="fa fa-external-link"></i></a> -->
      <!-- <a href="{{ site.baseurl }}{{ post.url }}" class="small-link">Read details</a> -->
    </article>
    {% else %}
    {% endif %}
  {% endfor %}
</div>


