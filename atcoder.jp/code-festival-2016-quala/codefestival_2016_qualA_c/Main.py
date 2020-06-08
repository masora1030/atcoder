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

s = input()
k = int(input())
n = len(s)
ans = []
for c in s[:n-1]:
    if c == 'a':
        ans.append('a')
        continue
    if ord('z')-ord(c)+1 <= k:
        k-=(ord('z')-ord(c)+1)
        ans.append('a')
    else:
        ans.append(c)
ans.append(chr(ord('a')+(ord(s[n-1])-ord('a')+k)%26))
print(*ans, sep='')