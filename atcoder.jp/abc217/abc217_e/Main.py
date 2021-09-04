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
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    sort_done = []
    now = deque([])
    q = ir()
    for i in range(q):
        qq = lr()
        if qq[0] == 1:
            now.append(qq[1])
        elif qq[0] == 2:
            if sort_done:
                ans = heapq.heappop(sort_done)
                print(ans)
            else:
                ans = now.popleft()
                print(ans)
        else:
            while now:
                num = now.pop()
                heapq.heappush(sort_done, num)
