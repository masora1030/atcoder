# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import math
import sys
import bisect
import heapq # 優先度付きキュー(最小値取り出し)

inf = 10**15
mod = 10**9+7
s = list(input())
t = list(input())
dict = {}
dict_t = {}
s_judge = [True for i in range(26)] # 全種類使っていない
t_judge = [True for i in range(26)] # 全種類使っていない
aint = ord('a')
flag = True
for i,c in enumerate(s):
    tmp = t[i]
    sint = ord(c)-aint
    tint = ord(tmp)-aint
    if s_judge[sint]:
        dict[sint] = tint
        s_judge[sint] = False
    else:
        if dict[sint] != tint:
            flag = False
            break
    if t_judge[tint]:
        dict_t[tint] = sint
        t_judge[tint] = False
    else:
        if dict_t[tint] != sint:
            flag = False
            break
if flag:
    print('Yes')
else:
    print('No')



