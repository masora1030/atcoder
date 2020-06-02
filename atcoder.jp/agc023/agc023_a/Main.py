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


# a^n
def power(a,n,mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod


n = int(input())
a = list(map(int, input().split()))
a2 = [0]
for i in a:
    a2.append(a2[-1]+i)
def sumArea(l,r):
    return a2[r]-a2[l]

# a2に同じ数が何個あるか
dic = {}
for num in a2:
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=1
ans = 0
for _,tmp in dic.items():
    if tmp != 1:
        ans += tmp*(tmp-1)//2
print(ans)

