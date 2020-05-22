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

n = int(input())
d = list(map(int, input().split()))
Dlist = [0 for i in range(12)]
for num in d:
    if num == 0:
        print(0)
        sys.exit()
    Dlist[num-1]+=1
    if Dlist[num-1] == 3:
        print(0)
        sys.exit()
judge = [0]
unknown = []
if Dlist[11] >= 2:
    print(0)
    sys.exit()
elif Dlist[11] == 1:
    judge.append(12)
for i,num in enumerate(Dlist[1:11]):
    if num == 2:
        judge.append(i+2)
        judge.append(24-i-2)
    if num == 1:
        unknown.append(i+1)
nujeng = len(unknown)
ans = 0
for i in range(2**nujeng):
    tmp = []
    for num in judge:
        tmp.append(num)
    for j in range(nujeng):
        dnow = unknown[j]
        if ((i >> j) & 1):
            tmp.append(dnow+1)
        else:
            tmp.append(24-dnow-1)
    dic = 50
    if tmp:
        tmp.sort()
        pre = -inf
        for num in tmp:
            if num-pre < dic:
                dic = num-pre
            pre = num
        if 24-tmp[-1] < dic:
            dic = 24-tmp[-1]
        ans = max(dic, ans)
print(ans)
