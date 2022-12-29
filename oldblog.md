---
layout: default
permalink: /blog/
---

<!-- new new new -->
<div id="main" role="main" class="container">
        <center><p class="" style="font-family: 'Inconsolata', monospace; font-size: 14px; background-color: #d42; color:white;">
        ★ <br>Below you'll find my old posts ranging from 2009 and 2019<br> Here just for historical purposes <br>★<br>
        </p></center></div>

<div id="main" role="main" class="container" style="font-family: 'Inconsolata', monospace;">

        {{ content }} 

<div class="posts clearfix">
      {% for post in site.posts %}
      {% if post.draft == true %}
      {% else %}
      {% capture date %}{{post.date | date: '%Y' | plus: 0 }}{% endcapture %}
    
      {% if date contains "2019" or date contains "2018" or date contains "2017" or date contains "2016" or date contains "2015" or date contains "2014" or date contains "2013" or date contains "2012" or date contains "2011" or date contains "2010" or date contains "2009" %}
    
      <article class="post">
          <div class="eyebrow">{{ post.date | date: "%d %b %Y" }}</div>
          <h1><a href="{{ site.baseurl }}{{ post.url }}" style="font-family: 'EB Garamond', serif; color: #7a7a7a;">{{ post.title }}</a></h1>
          <a href="{{ site.baseurl }}{{ post.url }}"><img src="../images/{{ post.url | remove: "/" }}.png" style="width: 75%; height: auto;" alt="post img" /></a>
          <div class="entry">
          </div>
        </article>
      {% endif %}
      {% endif %}
      {% endfor %}
</div>


    {% include footer.html %}
    {% include analytics.html %}
    <script>
      var coll = document.getElementsByClassName("collapsible");
      var i;
  
      for (i = 0; i < coll.length; i++) {
          coll[i].addEventListener("click", function() {
          this.classList.toggle("active");
          var content = this.nextElementSibling;
        if (content.style.display === "block") {
          content.style.display = "none";
        } else {
          content.style.display = "block";
      }
      });
      }
      </script>
  