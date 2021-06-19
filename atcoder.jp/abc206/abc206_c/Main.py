import sys
import bisect
from collections import deque
import itertools

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    dic = {}
    for num in a:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    ans_rev = 0
    for _,v in dic.items():
        ans_rev+=v*(v-1)//2
    print(n*(n-1)//2 - ans_rev)