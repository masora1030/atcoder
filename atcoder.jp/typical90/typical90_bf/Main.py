import sys
import bisect
from collections import deque
import itertools
import math
import heapq
import random

# import sys
# sys.setrecursionlimit(10**6)
from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()

import time
import random
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

# import numpy as np

if __name__=='__main__':
    n,k=lr()
    if n==0:
        print(0)
        sys.exit()
    mod = 10**5
    visited = [False for i in range(mod)]
    now = n
    base_nums = []
    while not visited[now]:
        visited[now] = True
        base_nums.append(now)
        add = 0
        ret = now
        for i in range(7):
            add+=ret%10
            ret = ret//10
        now+=add
        now%=mod
    roop_first_num = now
    roop_flg = False
    roop_nums = []
    for num in base_nums:
        if num == roop_first_num:
            roop_flg=True
        if roop_flg:
            roop_nums.append(num)
    roop_len = len(roop_nums)
    ret_len = len(base_nums)-roop_len
    if k<len(base_nums):
        print(base_nums[k])
    else:
        ret = k-ret_len
        ret%=roop_len
        print(roop_nums[ret])
