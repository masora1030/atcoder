sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf = 10**18
# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    s=list(sr())
    last_a_ind = len(s)
    for ind in range(len(s)-1, -1, -1):
        if s[ind] == 'a':
            last_a_ind = ind
        else:
            break
    first_not_ind = -1
    for ind in range(0, len(s)):
        if s[ind] == 'a':
            continue
        first_not_ind=ind
        break
    if first_not_ind == -1:
        print("Yes")
        sys.exit()
    if len(s)-last_a_ind < first_not_ind:
        print("No")
        sys.exit()
    flg = True
    for ind in range(last_a_ind-first_not_ind):
        if s[first_not_ind+ind] != s[last_a_ind-1-ind]:
            flg = False
            break
    if flg:
        print("Yes")
    else:
        print("No")