# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

url = "https://api.twitter.com/1.1/friends/list.json"

params = {
    "screen_name": "mt_tg",
}

req = twitter.get(url, params=params)
screen_name_list = []

if req.status_code == 200:
    user_object = json.loads(req.text.encode('utf-8'))
    print(user_object["next_cursor"])
    cursor = user_object["next_cursor"]

    for user in user_object["users"]:
        screen_name_list.append(user["screen_name"])
        print(user["screen_name"])

    while "next_cursor" in user_object:
        url = "https://api.twitter.com/1.1/friends/list.json"
        params = {
            "screen_name": "mt_tg",
            "cursor": cursor,
        }
        req = twitter.get(url, params=params)
        user_object = json.loads(req.text.encode('utf-8'))

        if req.status_code == 200:
            for user in user_object["users"]:
                screen_name_list.append(user["screen_name"])
                print(user["screen_name"])
        else:
            print(req.status_code)

else:
    print(req.status_code)

'''
if req.status_code == 200:
    followers = json.loads(req.text)
    for follower in followers["users"]:
        screen_name = follower["screen_name"]
        name = follower["name"]
        result_text = "screen_name: " + screen_name + ", name: " + name
        print(result_text.encode('utf-8'))
else:
    print(req.status_code)
'''
