# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
# list(map(int, list(input()))) # スペースがない数字リストを読み込み
import math
import fractions
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
import collections
from collections import deque
import pprint

inf = 10**18
mod = 10**9+7

n,m = map(int, input().split())
s = input()
t = input()
f=fractions.gcd(n,m)           #最大公約数
f2=n*m//f                          #最小公倍数


x = f2//n
y = f2//m

for i in range(n):
    if (x*i)%y==0:
        if s[i] != t[x*i//y]:
            print(-1)
            sys.exit()
print(f2)