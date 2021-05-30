import sys
import bisect

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    a = lr()
    dic = {}
    flg = False
    ans = 0
    for num in a:
        if num in dic:
            dic[num]+=1
            flg = True
        else:
            dic[num]=1
    if flg:
        for k,v in dic.items():
            if v == 1 or v == 3:
                print(k)
                sys.exit()
    else:
        print(0)