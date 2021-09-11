#!/usr/bin/env python3
# coding: utf-8

from base64 import b64decode, b64encode


def encode(x): return b64encode(x[::-1].encode())
def decode(x): return b64decode(x).decode()[::-1]

CONSUMER_KEY = decode(b'TzFkclpicE9tSGx4akhjZW1IRmlDS1Z6Ng==')
CONSUMER_SECRET = decode(
    b'TTRGaUo4aVZSM1RxOGdkdkVuUEhJYTdWMVB5Q0ZYaVd2MW5rQzNPNlRyNXdhclJoaUk=')

ACCESS_TOKEN = decode(
    b'dTdRbzFXWWVhVFppaE03MEFBVjJmdUYzWjI3dHJaLTA4Nzk5ODU0NjM3ODU3MzUzNDE=')
ACCESS_TOKEN_SECRET = decode(
    b'QnJ4emNOdkRMNDJsSE42ZVh5QUI1ajBmNzgyOVZOUDJHbWl3Z29USzc0SHdo')
