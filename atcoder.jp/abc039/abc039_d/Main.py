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

h,w = map(int, input().split())
s = [input() for i in range(h)]
ans = [['#' for i in range(w+2)]for i in range(h+2)]
for i in range(h):
    for j in range(w):
        now = s[i][j]
        if now == '.':
            ans[i][j] = '.'
            ans[i][j+1] = '.'
            ans[i][j+2] = '.'
            ans[i+1][j] = '.'
            ans[i+1][j+1] = '.'
            ans[i+1][j+2] = '.'
            ans[i+2][j] = '.'
            ans[i+2][j+1] = '.'
            ans[i+2][j+2] = '.'
flag = True
for i in range(h):
    for j in range(w):
        now = s[i][j]
        if now == '#':
            if i == 0 and j == 0:
                if ans[i+1][j+1] == '.' and ans[i+2][j+1] == '.' and ans[i+1][j+2] == '.' and ans[i+2][j+2] == '.':
                    flag = False
                    break
            elif i == h-1 and j == 0:
                if ans[i+1][j+1] == '.' and ans[i][j+1] == '.' and ans[i][j+2] == '.' and ans[i+1][j+2] == '.':
                    flag = False
                    break
            elif i == 0 and j == w-1:
                if ans[i+1][j+1] == '.' and ans[i+2][j+1] == '.' and ans[i+1][j] == '.' and ans[i+2][j] == '.':
                    flag = False
                    break
            elif i == h-1 and j == w-1:
                if ans[i+1][j+1] == '.' and ans[i][j+1] == '.' and ans[i+1][j] == '.' and ans[i][j] == '.':
                    flag = False
                    break
            elif i == 0:
                if ans[i+1][j+1] == '.' and ans[i+2][j+1] == '.' and ans[i+1][j] == '.' and ans[i+2][j] == '.' and ans[i+1][j+2] == '.' and ans[i+2][j+2] == '.':
                    flag = False
                    break
            elif j == 0:
                if ans[i+1][j+1] == '.' and ans[i+2][j+1] == '.' and ans[i+1][j+2] == '.' and ans[i+2][j+2] == '.' and ans[i][j+1] == '.' and ans[i][j+2] == '.':
                    flag = False
                    break
            elif i == h-1:
                if ans[i+1][j] == '.' and ans[i+1][j+1] == '.' and ans[i+1][j+2] == '.' and ans[i][j] == '.' and ans[i][j+1] == '.' and ans[i][j+2] == '.':
                    flag = False
                    break
            elif j == w-1:
                if ans[i][j] == '.' and ans[i+1][j] == '.' and ans[i+2][j] == '.' and ans[i][j+1] == '.' and ans[i+1][j+1] == '.' and ans[i+2][j+1] == '.':
                    flag = False
                    break
            else:
                if ans[i][j] == '.' and ans[i][j+1] == '.' and ans[i][j+2] == '.' and ans[i+1][j] == '.' and ans[i+1][j+1] == '.' and ans[i+1][j+2] == '.' and ans[i+2][j] == '.' and ans[i+2][j+1] == '.' and ans[i+2][j+2] == '.':
                    flag = False
                    break
if flag:
    print('possible')
    for i in range(1,h+1):
        print(*ans[i][1:w+1], sep='')
else:
    print('impossible')