import sys

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
    n = ir()

    def judge(a):
        stack = []
        for c in a:
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append('(')
        if stack:
            return False
        else:
            return True

    for i in range(2**n):
        a = []
        for j in range(n):
            if (i >> j) & 1:
                a.append(')')
            else:
                a.append('(')
        a.reverse()
        if judge(a):
            print(''.join(a))