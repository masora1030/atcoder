import heapq, sys
input = sys.stdin.readline
n, q = map(int, input().split())
 
where = [0 for _ in range(n)]
rate = [0 for _ in range(n)]
yochi = [[] for _ in range(200000)]
saikyo = []
#yochi...(-rate, i)
#saikyo...(rate, en)
 
for i in range(n):
    a, b = map(int, input().split())
    rate[i] = a
    where[i] = b - 1
    heapq.heappush(yochi[where[i]], (-rate[i], i))
 
for l in yochi:
    if len(l) > 0:
        a, i = l[0]
        heapq.heappush(saikyo, (-a, where[i]))
 
 
 
for _ in range(q):
    c, d = map(int, input().split())
    c, d = c - 1, d - 1
 
    res = where[c]
    where[c] = d
    #yochi[res]の処理
    while yochi[res]:
        _, i = yochi[res][0]
        if where[i] == res:
            break
        heapq.heappop(yochi[res])
 
    #yochi[where[c]]の処理
    heapq.heappush(yochi[where[c]], (-rate[c], c))
 
    #saikyoの処理
    if len(yochi[res]) > 0:
        heapq.heappush(saikyo, (-yochi[res][0][0], res))
    heapq.heappush(saikyo, (-yochi[where[c]][0][0], where[c]))
    while saikyo:
        t, en = saikyo[0]
        if len(yochi[en]) > 0 and -yochi[en][0][0] == t:
            break
        heapq.heappop(saikyo)
 
 
    print(saikyo[0][0])