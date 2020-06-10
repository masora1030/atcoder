# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque

inf = 10**18
mod = 10**9+7

n = list(map(int, list(input())))
def getAns(now , giri, t,f,s):
    if now == len(n):
        if t and f and s:
            return 1
        else:
            return 0
    tmp = n[now]
    ret = 0
    if giri:
        if tmp > 7:
            ret += getAns(now+1, False, t, f, True)
            ret += getAns(now+1, False, t, True, s)
            ret += getAns(now+1, False, True, f, s)
        elif tmp == 7:
            ret += getAns(now+1, giri, t, f, True)
            ret += getAns(now+1, False, True, f, s)
            ret += getAns(now+1, False, t, True, s)
        elif tmp > 5:
            ret += getAns(now + 1, False, True, f, s)
            ret += getAns(now + 1, False, t, True, s)
        elif tmp == 5:
            ret += getAns(now + 1, False, True, f, s)
            ret += getAns(now + 1, giri, t, True, s)
        elif tmp > 3:
            ret += getAns(now + 1, False, True, f, s)
        elif tmp == 3:
            ret += getAns(now + 1, giri, True, f, s)
    else:
        ret+=getAns(now+1, giri, t,f,True)
        ret+=getAns(now+1, giri, t,True,s)
        ret+=getAns(now+1, giri, True, f, s)
    return ret

ans = 0
for i in range(len(n)-1):
    ans += getAns(i+1,False,False,False,False)
print(ans + getAns(0,True,False,False,False))