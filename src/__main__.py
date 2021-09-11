#!/usr/bin/env python3
# coding: utf-8

from dis5000.genimg import genBaseImage, genImage
from time import time
from decimal import Decimal, ROUND_HALF_UP
from . import config, auth
_round = lambda f, r=ROUND_HALF_UP: int(Decimal(str(f)).quantize(Decimal("0"), rounding=r))

from tweepy import Stream, StreamListener


def _auth(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN="", ACCESS_TOKEN_SECRET=""):
    api, access_token, access_token_secret = auth.oauth_pin(CONSUMER_KEY, CONSUMER_SECRET,
                   ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    print(access_token, access_token_secret)
    return api, access_token, access_token_secret

def gen():
    t = time()
    width = 1500
    height = 500
    base = genBaseImage(width=width, height=_round(height/2))
    print("genBaseImage Time :", time()-t)
    i = genImage("5000兆円", default_width=width, height=height,
                 bg=(0, 0, 0, 0), default_base=base)


class MyStreamListener(StreamListener):
    def on_status(self, status):
        print(status.text)
        


def main():
    api = _auth(config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)[0]
    myStreamListener = MyStreamListener()
    myStream = Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['5000chobot'])


if __name__ == '__main__':
    main()
