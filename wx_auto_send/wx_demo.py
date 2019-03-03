# !/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from wxpy import *
import requests
import time

def get_news():
    """获取金山词霸每日一句，英文和翻译"""
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    content = r.json()['content']
    note = r.json()['note']
    return content, note

def send_news():
    try:

        content,note = get_news()
        connect_person_list =[u'莲']

        bot = Bot()
        for person in connect_person_list:
            my_friend = bot.friends().search(person)[0]
            my_friend.send(content)
            my_friend.send(note)

            time.sleep(8)
    except:

        print "failed."

if __name__ == "__main__":
    send_news()