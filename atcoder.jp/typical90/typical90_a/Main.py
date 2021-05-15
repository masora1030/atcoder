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


def get_primes(x):
    n=x
    primes=set(range(2, n+1))
    for i in range(2, int(n**0.5+1)):  # nのルート+1
        primes.difference_update(range(i*2, n+1, i))
    primes=list(primes)
    return primes

if __name__=='__main__':
    n,L = lr()
    k = ir()
    a = lr()

    def judge(x):
        pre = 0
        ind = 0
        now=0
        for i in range(k):
            now=0
            while now < x and ind < n:
                now += a[ind]-pre
                pre = a[ind]
                ind += 1
            if now < x:
                return False
        if L-pre >= x:
            return True
        else:
            return False

    def get_score():
        l=0
        r=10**18
        while r-l > 1:
            mid = (l+r)//2
            if judge(mid):
                l = mid
            else:
                r = mid
        return l

    print(get_score())