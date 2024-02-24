---
layout: default
permalink: /blog/
---

<div class="posts clearfix">
      {% for post in site.posts %}
      {% if post.draft == true %}
      {% else %}
      {% capture date %}{{post.date | date: '%Y' | plus: 0 }}{% endcapture %}
    
      {% if date contains "2023" or contains "2022" or date contains "2021" or date contains "2020" %}
    
      <article class="post">
          <div class="eyebrow">{{ post.date | date: "%d %b %Y" }}</div>
          <div class="row">
            <div class="column left">
                <a href="{{ site.baseurl }}{{ post.url }}"><img src="../images/{{ post.url | remove: "/" }}.png" style="border-radius: 5px;vertical-align: middle; width: 75%; height: auto;" alt="post img" /></a><br><br>
            </div>
            <div class="column right">
                <a href="{{ site.baseurl }}{{ post.url }}" style="font-family: 'Spectral', serif; font-size: 26px; color: #484848;">{{ post.title }}</a>
            </div>
          </div>
          <div class="entry">
          </div>
        </article>
      {% endif %}
      {% endif %}
      {% endfor %}
</div>



<!-- new new new -->
<div id="main" role="main" class="container">
        <center>
          <p class="" style="font-family: 'Spectral', monospace; font-size: 14px; background-color: #62453f; color:white;">
              ★ Historical Archive: My Posts from 2009 to 2019 ★
          </p>
        </center>
</div>

<div id="main" role="main" class="container" style="font-family: 'Spectral'; background-color:#fafafa; color:#484848;">

<div class="posts clearfix">
      {% for post in site.posts %}
      {% if post.draft == true %}
      {% else %}
      {% capture date %}{{post.date | date: '%Y' | plus: 0 }}{% endcapture %}
    
      {% if date contains "2019" or date contains "2018" or date contains "2017" or date contains "2016" or date contains "2015" or date contains "2014" or date contains "2013" or date contains "2012" or date contains "2011" or date contains "2010" or date contains "2009" %}
    
      <article class="post">
          <div class="eyebrow"><span style="font-family: 'Spectral'; background-color: #62453f; color: white;">&nbsp;&nbsp; {{ post.date | date: "%d %b %Y" }} &nbsp;&nbsp;</span></div>
          <div class="row">
            <div class="column left">
                <a href="{{ site.baseurl }}{{ post.url }}"><img src="../images/{{ post.url | remove: "/" }}.png" style="border-radius: 5px; vertical-align: middle; width: 75%; height: auto;" alt="post img" /></a><br><br>
            </div>
            <div class="column right">
                <a href="{{ site.baseurl }}{{ post.url }}" style="font-family: 'Spectral', serif; font-size: 18px;">{{ post.title }}</a>
            </div>
          </div>
          <div class="entry">
          </div>
        </article>
      {% endif %}
      {% endif %}
      {% endfor %}
</div>



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
  