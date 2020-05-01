import bisect
inf = 10**15
mod = 10**9+7
n, m = map(int, input().split())
ken = [[] for i in range(n)]
py = [list(map(int, input().split())) for i in range(m)]
for i in range(m):
    p, y = py[i]
    ken[p-1].append(y)
for tmp in ken:
    tmp.sort()
for i in range(m):
    p, y = py[i]
    ind = bisect.bisect_left(ken[p-1], y)
    print('{ans:06}{anse:06}'.format(ans=p, anse=ind+1))