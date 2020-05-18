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

n,d,k = map(int, input().split())
lr = [list(map(int, input().split())) for i in range(d)]
ans =[]
for i in range(k):
    s,t = map(int, input().split())
    rflag =  True # 右に行きたいと仮定
    if s > t:
        rflag = False
    for j,(l,r) in enumerate(lr):
        if l<=s<=r:
            if l<=t<=r:
                ans.append(j+1)
                break
            else:
                if rflag:
                    s = r
                else:
                    s = l
for tmp in ans:
    print(tmp)