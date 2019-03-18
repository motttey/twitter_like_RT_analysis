# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# url = "https://api.twitter.com/1.1/users/show.json"
page_max = 16
user_timeline_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
fav_RT_ratio_array = []

for page_index in range(1,page_max):
    params = {
        "screen_name": "mt_tg",
        "count": 200,
        "page": page_index,
    }
    req = twitter.get(user_timeline_url, params=params)

    if req.status_code == 200:
        statuses = json.loads(req.text)
        print(len(statuses))
        print("---")

        for status in statuses:
            if status["favorite_count"] > 10 and "retweeted_status" not in status.keys():
                if "media" in status["entities"].keys():
                    print(status["text"].encode('utf-8'))
                    print(status["retweet_count"])
                    print(status["favorite_count"])
                    print(status["retweet_count"] / status["favorite_count"])
                    print("---")

                    fav_RT_ratio = {}
                    fav_RT_ratio["retweet_count"] = status["retweet_count"]
                    fav_RT_ratio["favorite_count"] = status["favorite_count"]
                    fav_RT_ratio["ratio"] = status["retweet_count"] / status["favorite_count"]

                    fav_RT_ratio_array.append(fav_RT_ratio)
    else:
        print(req.status_code)

print(fav_RT_ratio_array)
f = open('./result/username.json', 'w')
json.dump(fav_RT_ratio_array, f)
