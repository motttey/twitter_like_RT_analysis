# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/followers/list.json"
params = {}

req = twitter.get(url, params=params)

if req.status_code == 200:
    followers = json.loads(req.text)
    for follower in followers["users"]:
        screen_name = follower["screen_name"]
        name = follower["name"]
        result_text = "screen_name: " + screen_name + ", name: " + name
        print(result_text.encode('utf-8'))
else:
    print(req.status_code)
