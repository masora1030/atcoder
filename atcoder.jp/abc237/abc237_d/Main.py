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
    n=ir()
    s=list(sr())
    ans_ind = [-1 for i in range(n+1)]
    l_ind = 0
    r_ind = n
    pre=s[0]
    if pre == 'R':
        ans_ind[0] = l_ind
        l_ind+=1
    else:
        ans_ind[0] = r_ind
        r_ind-=1

    for i,c in enumerate(s[1:]):
        now=i+1
        if pre == 'L':
            if c == 'L':
                ans_ind[now] = r_ind
                r_ind-=1
            else:
                ans_ind[now] = l_ind
                l_ind+=1
        else:
            if c == 'L':
                ans_ind[now] = r_ind
                r_ind-=1
            else:
                ans_ind[now] = l_ind
                l_ind+=1
        pre = c
    ans = [-1 for i in range(n+1)]
    for i,num in enumerate(ans_ind):
        if num != -1:
            ans[num] = i
    for i in range(n+1):
        if ans[i] == -1:
            ans[i] = n
            break
    print(*ans, sep=' ')
