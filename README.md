# Bruh Bot for Twitter

It currently replies with insults using evil insults api to home timeline and mentions timeline.
Planning to add Sentiment analysis to reply with compliments, motivation and random facts.
<br/> </br>
[Bruh Bot 69 on Twitter](https://www.twitter.com/bruh_bot_69)

## Requirements

* Python3
* Twitter API Keys

## Configuration


* Step-1: Make a .env file with your API Keys
```
API_KEY = "Your API key here"
API_KEY_SECRET = "Your API key secret here"
ACCESS_TOKEN = "Your Access token"
ACCESS_SECRET = "Your Access token secret"
BEARER_TOKEN = "Your Bearer token"
```
* Step-2: Make a last_ids.json file to store tweet ids
```
{
  "last_mention_id": 0,
  "last_home_id": 0
}
```

## How to run

After configuration make sure you have all the libraries which are used to run this bot properly.
- [Tweepy](https://www.tweepy.org/)
- [Json](https://www.json.org/)
- [Time](https://docs.python.org/3/library/time.html)
- [os](https://docs.python.org/3/library/os.html)
- [Requests](https://pypi.org/project/requests/)
- [dotenv](https://pypi.org/project/python-dotenv/)

If you have all the libraries then run **main.py** file

## Cat Image

Here's a pic of a random cat
<br/>
![I love cats](https://st2.depositphotos.com/4684319/7048/i/600/depositphotos_70486253-stock-photo-smiling-cat-cats.jpg)
