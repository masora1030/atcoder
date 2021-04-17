import sys
# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random

if __name__=='__main__':
    n,m = lr()
    ans = []
    a = lr()
    b = lr()
    for num in range(1,max(max(a),max(b))+1):
        tmp1 = False
        tmp2 = False
        ind = bisect.bisect_left(a,num)
        if ind < n and a[ind] == num:
            tmp1 = True
        ind = bisect.bisect_left(b,num)
        if ind < m and b[ind]==num:
            tmp2=True
        if tmp1 or tmp2:
            if not (tmp1 and tmp2):
                ans.append(num)
    print(*ans, sep=' ')