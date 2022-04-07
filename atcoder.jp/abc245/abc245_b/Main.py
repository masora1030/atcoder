import sys
import random
import time

# from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n=ir()
    a=lr()
    a=list(set(a))
    a.sort()
    ans=0
    for num in a:
        if ans!=num:
            print(ans)
            sys.exit()
        ans+=1
    print(ans)


if __name__ == '__main__':
    main()
