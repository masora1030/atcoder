# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import deque
import pprint

inf = 10**18
mod = 10**9+7

s = input()
k = int(input())
leng = len(s)
dic = {}
if k > len(s):
    print(0)
else:
    for i in range(leng-k+1):
        tmp = s[i:i+k]
        if not tmp in dic:
            dic[tmp] = 1
    print(len(dic))