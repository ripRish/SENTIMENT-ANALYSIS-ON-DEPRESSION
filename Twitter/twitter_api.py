import tweepy
# import configparser
# import pandas as pd
#
# # read configs
# config = configparser.ConfigParser()
# config.read('config.ini')
#
# api_key = config['twitter']['api_key']
# api_key_secret = config['twitter']['api_key_secret']
#
# access_token = config['twitter']['access_token']
# access_token_secret = config['twitter']['access_token_secret']
# vahalof818@tourcc.com
# Rishab@123
api_key = "XxZLOFSNL6nJwVhwBTiF8qR5z"
api_key_secret = "eAEde3UkxsVlI4mptJZjEG342xrgqHdoBJZbWD3tyyuCt6EYde"

access_token = "1505498035316408321-ZeqGyQtzTmePKSti37yVYjgyK2TQaj"
access_token_secret = "Qesj4T5jh2EZNdoNOuPV2WL8Fwkzksa3o8AejUMPLQo4b"
# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)


def get_tweets(user, n):
    tweets = []
    api = tweepy.API(auth)
    for status in tweepy.Cursor(api.user_timeline).items(n):
        tweets.append([status.text])
    # tweets = [
    #         "wants to be out in the sunshine but it's boring on my own.",
    #           "Its a beautiful daaaaaaayyyyy!!!!!!!! This makes me happy",
    #           "Why am I feeling worse??? F!!!",
    #           "Missing my cats right now   Relocating is hard",
    #           "    Not feeling it today     And to make matters worst its super nasty and rainy outside, YUCK!",
    #             "we were standing out in the pouring rain.. We were sitting on top of the world..  --   summer sucks"
    #           ]
    return tweets
