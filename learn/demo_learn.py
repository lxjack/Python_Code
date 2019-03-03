# !/usr/bin/env python
# -*- coding:utf-8 -*-
import re

SECTCRE = re.compile(
        r'\[+'                                 
        r'(?P<header>[^]]+)'                  
        r'\]'
        )
line="[name]"
mo = SECTCRE.match(line)
sectname = mo.group('header')
print sectname

OPTCRE = re.compile(
        r'(?P<option>[^:=\s][^:=]*)'               
        r'\s*(?P<vi>[:=])\s*'
        r'(?P<value>.*)$'
        )
line="A=1111"
mo = OPTCRE.match(line)
optname, vi, optval = mo.group('option', 'vi', 'value')
print optname, vi, optval