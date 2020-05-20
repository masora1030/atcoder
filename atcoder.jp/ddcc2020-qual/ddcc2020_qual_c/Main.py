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

h,w,k = map(int, input().split())
s = [input() for i in range(h)]
ans = [[0 for j in range(w)]for i in range(h)]
count = 1
for i in range(h):
    counts = 0
    for a in range(w):
        if s[i][a] == '#':
            counts+=1
    if counts == 0:
        if count != 1:
            for j in range(w):
                ans[i][j] = ans[i-1][j]
    elif counts == 1:
        if count != 1:
            for j in range(w):
                ans[i][j] = count
        else:
            for g in range(i+1):
                for j in range(w):
                    ans[g][j] = count
        count+=1
    else:
        if count != 1:
            end = 0
            endcount = 0
            for b in range(w):
                if s[i][w-1-b] == '#':
                    endcount+=1
                    if endcount == 2:
                        end = w-1-b
                        break
                ans[i][w-1-b] = count
            count+=1
            for j in range(end+1):
                if s[i][j] == '#':
                    ans[i][j] = count
                    count+=1
                else:
                    ans[i][j] = count
        else:
            end = 0
            endcount = 0
            for b in range(w):
                if s[i][w - 1 - b] == '#':
                    endcount += 1
                    if endcount == 2:
                        end = w-1-b
                        break
                for g in range(i+1):
                    ans[g][w-1-b] = count
            count += 1
            for j in range(end + 1):
                if s[i][j] == '#':
                    for g in range(i + 1):
                        ans[g][j] = count
                    count += 1
                else:
                    for g in range(i + 1):
                        ans[g][j] = count

for i in range(h):
    print(*ans[i], sep=' ')
