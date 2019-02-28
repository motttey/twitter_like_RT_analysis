# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# url = "https://api.twitter.com/1.1/users/show.json"
# params = {"id": 23048655}
url = "https://api.twitter.com/1.1/search/tweets.json"
params = {
    "q": "from:@motttey filter:images exclude:retweets",
    # "result_type": "popular",
    "count": 100,
}
req = twitter.get(url, params=params)

if req.status_code == 200:
    statuses = json.loads(req.text)
    for status in statuses["statuses"]:
        print(status["text"].encode('utf-8'))
        print(status["retweet_count"])
        print(status["favorite_count"])
        print("---")
else:
    print(req.status_code)
