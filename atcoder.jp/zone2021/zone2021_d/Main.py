import sys
from collections import deque

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf=10**18
mod=10**9+7
# mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

if __name__=='__main__':
    s = sr()
    t = deque([])
    flg = True
    for c in s:
        if c == 'R':
            flg = not flg
        else:
            if flg:
                t.append(c)
            else:
                t.appendleft(c)

    stack = []
    for c in t:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if flg:
        print(*stack, sep='')
    else:
        print(*reversed(stack), sep='')