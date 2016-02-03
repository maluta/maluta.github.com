---
layout: post
title: YoutubeEDU BR
---

Comece agora a aprender com videos no [Youtube EDU](http://youtube.com.br/edu)

{% highlight ruby %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}
