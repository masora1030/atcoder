sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

if __name__=='__main__':
    s = input().split()
    t = input().split()
    diff_num = 0
    for i in range(3):
        if s[i] != t[i]:
            diff_num+=1
    if diff_num == 0:
        print("Yes")
    elif diff_num == 2:
        print("No")
    else:
        print("Yes")