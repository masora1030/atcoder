from collections import deque

import sys

# input=sys.stdin.buffer.readline

# from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
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
    n,m = lr()
    dic = {}
    next_list = deque([])
    qs = [[] for _ in range(m)]
    inds = [[] for _ in range(n)]
    nums=0
    for i in range(m):
        k = ir()
        a = lr()
        qs[i] = deque(a)
        a0 = a[0]-1
        if a0 in dic and dic[a0] == 1:
            dic[a0] += 1
            next_list.append(a0)
            inds[a0].append(i)
        elif not a0 in dic:
            dic[a0] = 1
            inds[a0].append(i)
    while next_list:
        now_a = next_list.popleft()
        nums+=1
        ind1, ind2 = inds[now_a]
        qs[ind1].popleft()
        qs[ind2].popleft()
        if qs[ind1]:
            ne1 = qs[ind1][0]-1
            if ne1 in dic and dic[ne1]==1:
                dic[ne1]+=1
                next_list.append(ne1)
                inds[ne1].append(ind1)
            elif not ne1 in dic:
                dic[ne1]=1
                inds[ne1].append(ind1)

        if qs[ind2]:
            ne2 = qs[ind2][0]-1
            if ne2 in dic and dic[ne2] == 1:
                dic[ne2] += 1
                next_list.append(ne2)
                inds[ne2].append(ind2)
            elif not ne2 in dic:
                dic[ne2] = 1
                inds[ne2].append(ind2)

        dic[now_a]-=2
    if nums == n:
        print("Yes")
    else:
        print("No")

