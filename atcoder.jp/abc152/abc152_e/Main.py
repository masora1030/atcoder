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

dic = {}

# mod で割り算(フェルマー、逆元利用)
mod = 10**9+7

N = 10**6+1
inv_t = [0]+[1]

for i in range(2,N):
    inv_t += [inv_t[mod % i] * (mod - int(mod / i)) % mod]

def moddiv(a, b):
    return a*inv_t[b]%mod

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
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
a = list(map(int, input().split()))
j = []
for num in a:
    tmp = factorization(num)
    j.append(tmp)
    for p,x in tmp:
        if p in dic:
            dic[p] = max(dic[p],x)
        else:
            dic[p] = x
gc = 1
for k,v in dic.items():
    gc*=(k**v)%mod
ans = 0
for num in a:
    ans += moddiv(gc, num)
    ans %= mod
print(ans)
