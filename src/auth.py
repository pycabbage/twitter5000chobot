#!/usr/bin/env python3
# coding: utf-8

import tweepy
import webbrowser


def oauth_pin(consumer_key, consumer_secret, access_token="", access_token_secret=""):
    # ここで oob と入力することで、アクセス許可後にPINが表示される様になる
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, 'oob')

    if not (len(access_token) and len(access_token_secret)):
        # 認証用URLを取得後ブラウザで開く
        print("Open :")
        authorization_url = auth.get_authorization_url()
        print(authorization_url)
        webbrowser.open(authorization_url)

        # アクセスを許可後出てきたPINを入力
        pin_code = input("PIN CODE >> ").strip()

        # PINコードを元にトークンなどを取得
        auth.get_access_token(pin_code)
        # print(f"ACCESS_TOKEN = {auth.access_token}")
        # print(f"ACCESS_SECRET = {auth.access_token_secret}")
        access_token = auth.access_token
        access_token_secret = auth.access_token_secret

    # 取得した情報を認証情報に追加
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # username = api.me().name
    # print(f"ユーザー名: {username}")
    return (api, auth.access_token, auth.access_token_secret)


def oauth2(consumer_key, consumer_secret):
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
    print(dir(auth))
    # return (api, auth.access_token, auth.access_token_secret)
    return api
