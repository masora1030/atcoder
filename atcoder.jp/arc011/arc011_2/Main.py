# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque

inf = 10 ** 15
mod = 10 ** 9 + 7

n = int(input())
s = input().split()

dic = {'b':'1', 'c':'1', 't':'3', 'j':'3', 'd':'2', 'w':'2',
       'f':'4', 'q':'4', 'l':'5', 'v':'5', 's':'6', 'x':'6',
       'p':'7', 'm':'7', 'h':'8', 'k':'8', 'n':'9', 'g':'9',
       'z':'0', 'r':'0', 'a':'', 'i':'', 'e':'', 'u':'', 'y':'',
       'o':'', '.':'', ',':''}
ans = []

for c in s:
    tmp = []
    for cc in c.lower():
        tmp.append(dic[cc])
    preans = ''.join(tmp)
    if preans != '':
        ans.append(''.join(tmp))
print(*ans, sep=' ')