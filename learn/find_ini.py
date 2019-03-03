# !/usr/bin/env python
# -*- coding:utf-8 -*-


import os

temp=[]
root=r"D:\02E_DISK\02_Python\Python_Code"

for root,subdirs,files in os.walk(root):
    for file in files:
        if file.endswith(".ini"):
            print file
            temp.append(os.path.join(root,file))
print temp




