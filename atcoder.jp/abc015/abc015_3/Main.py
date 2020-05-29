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
n,k = map(int, input().split())
t = [list(map(int, input().split())) for i in range(n)]
def judge(num, total):
    if num > 0:
        ret = True
        for i in range(k):
            ret = judge(num-1, total^t[n-num][i])
            if not ret:
                break
        return ret
    else:
        if total == 0:
            return False
        else:
            return True
if judge(n,0):
    print('Nothing')
else:
    print('Found')