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

# segment tree

def main():
    n=ir()
    st_dic = {}
    st = [sr().split() for _ in range(n)]
    for s,t in st:
        if s in st_dic:
            st_dic[s]+=1
        else:
            st_dic[s]=1
        if t in st_dic:
            st_dic[t]+=1
        else:
            st_dic[t]=1
    for s,t in st:
        if s != t:
            if st_dic[s]-1 >= 1 and st_dic[t]-1 >= 1:
                print("No")
                sys.exit()
        else:
            if st_dic[s]-2 >= 1:
                print("No")
                sys.exit()
    print("Yes")


if __name__ == '__main__':
    main()
