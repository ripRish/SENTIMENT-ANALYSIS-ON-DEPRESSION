import random

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
    try:
        for status in tweepy.Cursor(api.user_timeline).items(n):
            tweets.append([status.text])
    except:
        if user == "depressed_user":
            tweets = [
                "wants to be out in the sunshine but it's boring on my own.",
                "Its a beautiful daaaaaaayyyyy!!!!!!!! This makes me happy",
                "Why am I feeling worse??? F!!!",
                "Missing my cats right now   Relocating is hard",
                "    Not feeling it today     And to make matters worst its super nasty and rainy outside, YUCK!",
                "we were standing out in the pouring rain.. We were sitting on top of the world..  --   summer sucks"
            ]
        elif user == "happy_user":
            tweets = [
                "Going out for picnic",
                "Its a beautiful daaaaaaayyyyy!!!!!!!! This makes me happy",
                "Its the best day of my life",
                "I Love my mom",
                "we were standing out in the pouring rain.. We were sitting on top of the world..  --   summer sucks"
            ]
        elif user == "low depression":
            tweets = [
                "Going out for picnic",
                "Its a beautiful daaaaaaayyyyy!!!!!!!! This makes me happy",
                "Its the best day of my life",
                "I Love my mom",
                "    Not feeling it today     And to make matters worst its super nasty and rainy outside, YUCK!",
                "we were standing out in the pouring rain.. We were sitting on top of the world..  --   summer sucks"
            ]
        elif user == "high depression":
            tweets = [
                "wants to be out in the sunshine but it's boring on my own.",
                "Its a beautiful daaaaaaayyyyy!!!!!!!! This makes me happy",
                "Why am I feeling worse??? F!!!",
                "Its the best day of my life",
                "Missing my cats right now   Relocating is hard",
                "    Not feeling it today     And to make matters worst its super nasty and rainy outside, YUCK!",
                "we were standing out in the pouring rain.. We were sitting on top of the world..  --   summer sucks"
            ]
        else:
            temp = [
                "wants to be out in the sunshine but it's boring on my own.",
                "Its a beautiful daaaaaaayyyyy!!!!!!!! This makes me happy",
                "I am pumped up for today yeah!!!",
                "I Love my mom",
                "I love college",
                "Missing my cats right now   Relocating is hard",
                "    Not feeling it today     And to make matters worst its super nasty and rainy outside, YUCK!",
                "we were standing out in the pouring rain.. We were sitting on top of the world..  --   summer sucks"
            ]
            for i in range(8):
                tweets.append(temp[random.randrange(0, 8)])



    return tweets
