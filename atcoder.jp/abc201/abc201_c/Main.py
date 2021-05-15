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
    s = sr()
    ans = 0
    must = [i for i,num in enumerate(s) if num=='o']
    for i in range(10000):
        a = [i%10, (i//10)%10, (i//100)%10, (i//1000)%10]
        flg = True
        judge = [False for j in range(10)]
        for num in a:
            judge[num] = True
            if s[num]=='x':
                flg = False
                break
        for ind in must:
            if not judge[ind]:
                flg=False
                break
        if flg:
            ans+=1
    print(ans)