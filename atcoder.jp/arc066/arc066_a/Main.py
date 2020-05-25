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

def power(a,n,mod):
    x = 1
    while n:
        if n & 1:
            x *= a % mod
        n >>= 1
        a *= a % mod
    return x % mod

n = int(input())
evenflag = n%2==0
a = list(map(int, input().split()))
kouho = [0 for i in range(n)]
for num in a:
    if (evenflag and num%2==0) or (not evenflag and num%2==1):
        print(0)
        sys.exit()
    x = (n-1+num)//2
    y = n-1-x
    kouho[min(x,y)]+=1
ans = 0
if n%2 == 1:
    if kouho[n//2] != 1:
        print(0)
        sys.exit()
for i in range(n//2):
    if kouho[i] == 2:
        ans+=1
    else:
        print(0)
        sys.exit()

print(power(2,ans,mod))