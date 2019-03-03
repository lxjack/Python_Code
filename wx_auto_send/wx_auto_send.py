# !/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import ConfigParser
from wxpy import *
import time
import os


# 从配置文件读取朋友信息
def get_persons():
    CODEC = 'utf-8'
    cf = ConfigParser.ConfigParser()
    cf.read("person_group.ini")
    connect_person_dict = cf.items("persons")
    connect_person_list = []
    for key in connect_person_dict:
        str = key[1]
        str_decode = str.decode(CODEC)  # 转码为unicode字符串
        connect_person_list.append(str_decode)
    return connect_person_list


# 从配置文件读取组信息
def get_groups():
    CODEC = 'utf-8'
    cf = ConfigParser.ConfigParser()
    cf.read("person_group.ini")
    connect_group_dict = cf.items("groups")
    connect_group_list = []
    for key in connect_group_dict:
        str = key[1]
        str_decode = str.decode(CODEC)  # 转码为unicode字符串
        connect_group_list.append(str_decode)
    return connect_group_list


# 获取message文件配置的信息
def get_message(message_file):
    CODEC = 'utf-8'
    info = ""
    if os.path.isfile(message_file):
        f = open(message_file, 'r')
        info = f.read()
    info = info.decode(CODEC)
    return info


# 获取图片列表
def get_picture(picture_dir):
    picture_list = []
    if os.path.isdir(picture_dir):
        temp_list = os.listdir(picture_dir)
        for picture_file in temp_list:
            if picture_file.endswith("jpg") or picture_file.endswith("png"):
                picture_file = os.path.join(picture_dir, picture_file)
                picture_list.append(picture_file)
    return picture_list


def send_news():
    current_work_dir = os.getcwd()
    picture_dir = os.path.join(current_work_dir, "picture")
    message_dir = os.path.join(current_work_dir, "message")
    message_file = os.path.join(message_dir, "message.txt")

    message_info = get_message(message_file)
    picture_list = get_picture(picture_dir)
    bot = Bot()

    # 给朋友发送消息
    connect_person_list = get_persons()
    for person in connect_person_list:
        try:
            my_friend = bot.friends().search(person)[0]
            if message_info != "":
                my_friend.send(message_info)
                time.sleep(1)

            for picture in picture_list:
                my_friend.send_image(picture)
                time.sleep(1)

            time.sleep(10)
        except:
            pass

    # 给群发送消息
    connect_group_list = get_groups()
    for group in connect_group_list:
        try:
            my_group = bot.groups().search(group)[0]
            if message_info != "":
                my_group.send(message_info)
                time.sleep(1)

            for picture in picture_list:
                my_group.send_image(picture)
                time.sleep(1)

            time.sleep(10)
        except:
            pass
            # my_friend = bot.friends().search('沙海拾贝')[0]
            # my_friend.send(u"消息发送失败，to:" + group)

if __name__ == "__main__":
    send_news()