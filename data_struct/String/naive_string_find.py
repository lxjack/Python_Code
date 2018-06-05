#_*_ coding: utf-8 _*_

def naive_string_find(p,t):
    '''使用传统方式进行字符串查找，会产生回溯'''
    m, n = len(p), len(t)
    i, j=0, 0

    while i<m and j<n:
        if p[i]==t[j]:
            i, j=i+1, j+1
        else:
            i, j=0, j-i+1

    if i==m:
        return j-i
    else:
        return  -1

pa='aa'
tr='abbbaacc'
index=naive_string_find(pa,tr)
print index