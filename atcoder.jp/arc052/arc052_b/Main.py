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
pi = math.pi

n,q = map(int, input().split())
xrh = [list(map(int, input().split())) for i in range(n)]
xrh.sort()
a2 = [0 for i in range(2*(10**4)+1)]
maxh = 0
for x,r,h in xrh:
    maxh = max(maxh, x+h)
    for i in range(h-1):
        tmp = r*((h-1-i)/h)
        a2[x+1+i] += (r*r*h-tmp*tmp*(h-1-i))*pi/3
    tmp = r*r*h*pi/3
    for i in range(x+h,2*(10**4)):
        a2[i] += tmp
def SumArea(l, r):
    return a2[r]-a2[l]

for i in range(q):
    a,b = map(int, input().split())
    print(SumArea(a, b))