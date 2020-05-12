import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)

inf = 10 ** 15
mod = 10 ** 9 + 7
n = int(input())
judge = []
w = input()
pre = w[-1]
judge.append(w)
for i in range(n-1):
    w = input()
    if w[0] == pre and (not w in judge):
        pre = w[-1]
        judge.append(w)
    else:
        print('No')
        sys.exit()
print('Yes')