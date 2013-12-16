---	
layout: post
title: Things to do with Twitter Archive
---

Twitter, Inc provides a [backup](https://blog.twitter.com/2012/your-twitter-archive) of all your Twitter archive. In 5-years I have tweeted #1,811 times (my _firt_ date from 2008 and I didn't tweet a lot).

After download the content, checking the raw content (.csv) I decided do play with data. Ideas come into my mind:

* generate a tag (word) cloud 
* which my average tweets per year?
* which hour of the day I tweet more? _(this particularly info is only available from late-2010)_
* all urls listed in tweets (and open it in browser)

Also if you are a social media manager that like programming you can study how to improve your campaign. Said that it's time to write some code (all examples uses Python 2.x). All code are avaliable on gist, link at end of post.

First thing to do is read content from CSV file, this is straightforward with python's [csv](http://docs.python.org/2/library/csv.html) module.

        csv.reader(open("tweets.csv"), delimiter=',', quotechar='"')

It returns an iterable _csv.reader object. Besides the content itself, each tweet contains the following metadata. 

        ['tweet_id', 'in_reply_to_status_id', 'in_reply_to_user_id', 'timestamp', 
        'source', 'text', 'retweeted_status_id', 'retweeted_status_user_id', 
        'retweeted_status_timestamp', 'expanded_urls']

With this information you can use your creativity to better "interpret" your tweets. Starting with [data visualization](http://en.wikipedia.org/wiki/Data_visualization) I choose an example using tag cloud (tags are usually single words, and the importance of each tag is shown with font size or color). Using [PyTagCloud](https://github.com/atizo/PyTagCloud) it's easy generate the word cloud. In order to consider the relevant data I excluded _articles_, _pronouns_,  _interjections_ and other common words like _"www"_, _"bi.ly"_, etc; an example on how to do this. 


        re.sub("(www|the|a|we|ours|this|some|who|bit.ly)", " ", buffer)

The image below represent the 25 most important words from my tweets.

![](http://farm3.staticflickr.com/2836/11376478926_95c0033f63_o.png)

With this visualization it's easy to conclude that most of my tweets are tech related, especially linux and android :)

**Which my average tweets per year?**

To get stats from date we can data from **['timestamp']** value. An example of data: 2013-12-13 06:33:25 +0000 but it's type is str and not [datetime](http://docs.python.org/2/library/datetime.html), the first thing to do is convert and then filter relevant information. 


        tweets_per_year = { 2008:0, 2009:0, 2010:0, 2011:0, 2012:0, 2013:0 }

        format = '%Y-%m-%d %H:%M:%S' #example 2013-12-13 06:33:25

        for tweet in tweets:
            date = tweet[3]
            if date != "timestamp": 
                date_object = datetime.strptime(date[:-6],format) # -6 to remove " +0000"
                year = date_object.year
                for y in tweets_per_year:
                    if y == year:
                        tweets_per_year[year] += 1


        print tweets_per_year

Here my stats:

        2008 — #223
        2009 — #380
        2010 — #675
        2011 — #368
        2012 — #77
        2013 — #87

I need more years like 2010.

**Which hour of the day I tweet more?**

Remember that feature was incorporated late (to me appeared on tweets from late-2010). Using the same snippet above we can add it:


        tweets_per_hour  = { 0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 
                             7:0, 8:0, 9:0, 10:0, 11:0, 12:0,
                             13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 
                             19:0, 20:0, 21:0, 22:0, 23:0 }
        	
        # (...)

        hour = date_object.hour
        minute = date_object.minute
        second = date_object.second

        if hour == 0 and minute == 0 and second == 0:
            pass # feature not implemeted
        else:
             print date_object
             for t in tweets_per_hour:
                 if t == hour:
                     tweets_per_hour[t] += 1


It produces: {0: 25, 1: 43, 2: 30, 3: 15, 4: 8, 5: 4, 6: 4, 7: 1, 8: 0, 9: 2, 10: 3, 11: 24, 12: 50, 13: 36, 14: 42, 15: 34, 16: 42, 17: 49, 18: 36, 19: 36, 20:56, 21: 39, 22: 23, 23: 28}

        from 12:00 a.m to 2 a.m — 98
        from 12:00 p.m to 2 p.m — #128
        from 20:00 p.m to 22 p.m — #118

This data can be particularly interesting if you associate with [Twitter API](https://dev.twitter.com/docs/api/1.1/get/statuses/mentions_timeline) to evaluate the "rate" of interactions (retweets, mentions). 

Finally, let's get the **URLs** in this case the can use two approaches: filter the **['text']** content or directly from **['expanded_urls']** (this was introduced propably after [t.co](https://blog.twitter.com/2010/links-and-twitter-length-shouldn%E2%80%99t-matter) feature). Since I have links from 2008 when this feature wasn't enable I'll use the first one. 

        exp = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        for tweet in tweets:
            urls = re.findall(exp, tweet)
            for url in urls:
                if url != "":
                print url # do something


You can use Python's [webbrowser](http://docs.python.org/2/library/webbrowser.html) module to open URLs.

        import webbrowser
        webbrowser.open_new_tab("www.google.com")

**CODE ready to go**

some gists read to go

* **[tagcloud](https://gist.github.com/maluta/7994212)** ([raw](https://gist.github.com/maluta/7994212/raw/615097ef39a27b384d264f2fef54ed7616e04bd1/tagcloud.py))
* **[stats](https://gist.github.com/maluta/7994360)** like average tweets per year and hour ([raw](https://gist.github.com/maluta/7994360/raw/3a527b5fe1e46173319ecea2f2c79a0d590ff3a1/tweets_per_year-hour.py)) 
* **[listed urls](https://gist.github.com/maluta/7994272)** ([raw](https://gist.github.com/maluta/7994272/raw/addb83522ea546ad3fcee576558393c7740f6f53/tweets_url.py))





If you like this post you can [follow me](http://www.twitter.com/maluta)










