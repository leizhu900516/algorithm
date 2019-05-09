# -*- coding: utf-8 -*-
# @author: chenhuachao
# @time: 2019/5/9
# KMP.py 查找字符串出现的首次位置



t = 'whatyouname'
p = 'name'


next = []
def get_next(p):
    next.insert(0,-1)
    i,j = 0,-1
    while i< len(p):
        if j == -1 or p[i] == p[j]:
            i+=1
            j+=1
            next.insert(i,j)
        else:
            j = next[j]


def kmp(t,p):
    i,j = 0,0
    while j<len(t) and j < len(p):
        if j == -1 or t[i] == p[j]:
            i+=1
            j+=1
        else:
            j = next[j]
    if j == len(p):
        return  i-j
    else:
        return -1


if __name__ == '__main__':
    get_next(p)
    print(next)
    result = kmp(t,p)
    print(result)
