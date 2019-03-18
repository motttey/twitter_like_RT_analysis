# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

page_max = 16
user_timeline_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
get_follower_url = "https://api.twitter.com/1.1/friends/list.json"

def get_each_user_tweets(screen_name):
    fav_RT_ratio_array = []

    for page_index in range(1,page_max):
        params = {
            "screen_name": screen_name,
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
    f = open('./result/' + screen_name + '.json', 'w')
    json.dump(fav_RT_ratio_array, f)
    return

def get_follower_list(screen_name):
    params = {
        "screen_name": screen_name,
    }

    req = twitter.get(get_follower_url, params=params)
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
                "screen_name": screen_name,
                "cursor": cursor,
            }
            req = twitter.get(get_follower_url, params=params)
            user_object = json.loads(req.text.encode('utf-8'))

            if req.status_code == 200:
                for user in user_object["users"]:
                    screen_name_list.append(user["screen_name"])
                    print(user["screen_name"])
            else:
                print(req.status_code)

    else:
        print(req.status_code)
    return screen_name_list

def main():
    follower_list = get_follower_list("mt_tg")
    for follower in follower_list:
        get_each_user_tweets(follower)
    return

if __name__ == '__main__':
    main()
