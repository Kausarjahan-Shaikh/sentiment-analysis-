<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

/* Create two equal columns that floats next to each other */
.column {
  float: left;
  width: 50%;
  padding: 10px;
  height: 300px; /* Should be removed. Only for demonstration */
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

/* Responsive layout - makes the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
  }
}
</style>
</head>
<body>

<h2>Sentiment Analysis of Lockdown in USA during Covid-19</h2>
<p>A case study on Twitter using Machine Learning</p>

<div class="row">
  <div class="column" style="background-color:#aaa;">
    <h2>Tweet</h2>
    <p>Some text..</p>
  </div>
  <div class="column" style="background-color:#bbb;">
    <h2>Sentiment</h2>
    <p>Some text..</p>
  </div>

</div>
<script>
import tweepy
from textblob import TextBlob

consumer_key = 'kNUlFVnkKaDHL2LmbFCcL3vB9'
consumer_secret = 'IRoCoL6qDxio3iirC63sPwswkh20cJXpzBCzsAJ3anzvUbkAHL'
access_token = '1492044764799115266-IYcwOMQ6Yd6TCuKSqwh0nfJyfTUtoS'
access_token_secret = '4scpXoux5uPhZwS6jlEt3kCb2ORtUB1Was13htrSCy7vy'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                        # set access token and secret
auth.set_access_token(access_token, access_token_secret)
                        # create tweepy API object to fetch tweets
api = tweepy.API(auth)

public_tweets=https://t.co/EI8eeGHapE(q="covid usa",lang="en")

for tweet in public_tweets:
  print(tweet.text) # This should be printed in the tweet column
  analysis=TextBlob(tweet.text)
  print(analysis.sentiment) #This should be printed in the sentiment column
  if analysis.sentiment[0]>0:
    print('Positive')
  elif analysis.sentiment[0]<0:
    print('negative')
  else:
    print('neutral')
</script>

</body>
</html>
