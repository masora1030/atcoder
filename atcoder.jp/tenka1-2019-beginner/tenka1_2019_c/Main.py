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
s = input()
siro = [0 for i in range(n+1)]
kuro = [0 for j in range(n+1)]
for i,c in enumerate(s):
    siro[i+1] = siro[i]
    kuro[i+1] = kuro[i]
    if c == '#':
        kuro[i+1]+=1
    else:
        siro[i+1]+=1
def getSiro(l,r):
    return siro[r]-siro[l]

def getKuro(l,r):
    return kuro[r]-kuro[l]

ans = inf
for i in range(n+1):
    ans = min(ans, getKuro(0,i)+getSiro(i,n))
print(ans)
