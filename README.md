Bruh Bot for Twitter
=======================

It currently replies with insults using evil insults api to home timeline and mentions timeline.
Working to add Sentiment analysis to reply with compliments, motivation and random facts.

Requirements
============

* Python3
* Twitter API Keys

Configuration
============

* Step-1: Make a .env file with your API Keys
* Step-2: Make a last_ids.json file like this:
```
{"last_mention_id": 0, "last_home_id": 0}
```

Usage
=====

First of all make sure you have all the libraries which are used to make this bot.
- [Tweepy](https://www.tweepy.org/)
- [Json](https://www.json.org/)
- [Time](https://docs.python.org/3/library/time.html)
- [os](https://docs.python.org/3/library/os.html)
- [Requests](https://pypi.org/project/requests/)
- [dotenv](https://pypi.org/project/python-dotenv/)

If you have all the libraries then **run main.py** file
