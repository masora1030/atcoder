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

inf = 10**18
mod = 10**9+7

n,k = map(int, input().split())
a = [int(input()) for i in range(n)]
ans=0
right=0
for left in range(n):
    if left==right: right+=1
    while right<n and a[right-1] < a[right]:
        right += 1
        if right-left >= k:
            ans+=1
if k==1:
    ans=n
print(ans)