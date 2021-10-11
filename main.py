import time
import tweepy
import os
import json
import requests

import get_reply

from file_operations import *

from dotenv import load_dotenv

load_dotenv()
auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_KEY_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_SECRET'))

API = tweepy.API(auth)


def reply_mentions():
    last_id = retrive_last_id("last_mention_id", "last_ids.json")
    if (last_id == 0):
        mentions = API.mentions_timeline()
        mentions.reverse()
    else:
        mentions = API.mentions_timeline(
            since_id=last_id, exclude_replies=True)
        mentions.reverse()
    for mention in mentions:
        save_last_id("last_mention_id", mention.id, "last_ids.json")
        if "bruh" in mention.text.lower():
            API.update_status(get_reply.get_random_insult(),
                              in_reply_to_status_id=mention.id,
                              auto_populate_reply_metadata=True)
            print("Replied to " + mention.user.screen_name)


def reply_home():
    last_id = retrive_last_id("last_home_id", "last_ids.json")
    if (last_id == 0):
        homestatuses = API.home_timeline()
        homestatuses.reverse()
    else:
        homestatuses = API.home_timeline(
            since_id=last_id, exclude_replies=True)
        homestatuses.reverse()
    for homestatus in homestatuses:
        if homestatus.user.screen_name != "bruh_bot_69":
            save_last_id("last_home_id", homestatus.id, "last_ids.json")
            API.update_status(get_reply.get_random_insult(),
                              in_reply_to_status_id=homestatus.id,
                              auto_populate_reply_metadata=True)
            print("Replied to " + homestatus.user.screen_name)


while True:
    reply_home()
    reply_mentions()
    time.sleep(69)
