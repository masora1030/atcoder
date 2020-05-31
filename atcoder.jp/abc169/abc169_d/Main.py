# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)
from collections import deque
inf = 10 ** 18
mod = 10 ** 9 + 7

def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

n = int(input())
tmp = factorization(n)
ans=0
judge = [(i*(i+1))//2 for i in range(1,10)]
def getC(x):
    ind = bisect.bisect_left(judge, x)
    if judge[ind] == x:
        return ind+1
    else:
        return ind
for a,b in tmp:
    ans+=getC(b)
print(ans)