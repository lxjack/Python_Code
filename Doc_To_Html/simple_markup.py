#_*_ coding: utf-8 _*_
import re,sys
from util import blocks

print '<html><head><title>...</title><body>'

title=True

# for block in blocks(sys.stdin):
f=open(r'D:\03F_DISK\test.log','r')
for block in blocks(f):
    if title:
        print '<h1>'
        print block
        print '</h1>`'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'

print '</body></html>'


