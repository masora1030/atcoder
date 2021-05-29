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
    n=ir()
    a = [[] for i in range(3)]
    dic = {'R':0, 'B':1, 'G':2}
    for i in range(2*n):
        x = sr().split()
        k = int(x[0])
        col = dic[x[1]]
        a[col].append(k)
    for i in range(3):
        a[i].sort()
    is_odd = [len(a[i])%2 for i in range(3)]
    if sum(is_odd) == 0:
        print(0)
        sys.exit()
    if sum(is_odd) == 2:
        ans = inf
        pre = [[[inf, -1], [inf, -2], [inf, -3]], [[inf, -1], [inf, -2], [inf, -3]]]
        odds = []
        even=0
        for i,num in enumerate(is_odd):
            if num == 1:
                odds.append(i)
        for i in range(3):
            if not i in odds:
                even=i
        for ii, now in enumerate(odds):
            dif = 0
            for i in odds:
                if i != now:
                    dif = i
            for num in a[now]:
                ind = bisect.bisect_left(a[dif], num)
                ind2 = max(ind-1, 0)
                if ind < len(a[dif]):
                    ans = min(abs(num-a[dif][ind]), ans)
                ans = min(abs(num-a[dif][ind2]), ans)

                if a[even]:
                    ind = bisect.bisect_left(a[even], num)
                    ind2 = ind-1
                    if ind < len(a[even]):
                        if pre[ii][0][0] >= abs(num-a[even][ind]):
                            pre[ii][2] = pre[ii][1]
                            pre[ii][1] = pre[ii][0]
                            pre[ii][0] = abs(num-a[even][ind]), ind
                        elif pre[ii][1][0] >= abs(num-a[even][ind]):
                            pre[ii][2]=pre[ii][1]
                            pre[ii][1]=abs(num-a[even][ind]), ind
                        elif pre[ii][2][0] >= abs(num-a[even][ind]):
                            pre[ii][2]=abs(num-a[even][ind]), ind
                    if ind2 >= 0:
                        if pre[ii][0][0]>=abs(num-a[even][ind2]):
                            pre[ii][2]=pre[ii][1]
                            pre[ii][1]=pre[ii][0]
                            pre[ii][0]=abs(num-a[even][ind2]), ind2
                        elif pre[ii][1][0]>=abs(num-a[even][ind2]):
                            pre[ii][2]=pre[ii][1]
                            pre[ii][1]=abs(num-a[even][ind2]), ind2
                        elif pre[ii][2][0]>=abs(num-a[even][ind2]):
                            pre[ii][2]=abs(num-a[even][ind2]), ind2

        kouho = []
        for i in range(3):
            for j in range(3):
                if pre[0][i][1] != pre[1][j][1]:
                    kouho.append(pre[0][i][0]+pre[1][j][0])
        if kouho:
            kouho.sort()
            ans = min(ans, kouho[0])
        print(ans)
