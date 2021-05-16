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
    a = lr()
    a1 = [0]
    for i,num in enumerate(a):
        if i%2 == 0:
            a1.append(a1[-1]+num)
        else:
            a1.append(a1[-1]-num)
    dic = {}
    for num in a1:
        if num in dic:
            dic[num]+=1
        else:
            dic[num]=1
    ans = 0
    for _,c in dic.items():
        ans+=(c*(c-1)//2)
    print(ans)