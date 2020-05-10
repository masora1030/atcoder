inf = 10**15
mod = 10**9+7

n,k = map(int, input().split())
a = list(map(int, input().split()))
firstkouho = []
roopkouho = []
visited = [False for i in range(n)]
tmp = 0
while visited[tmp] == False:
    visited[tmp] = True
    tmp2 = a[tmp] - 1
    tmp = tmp2
roopstart = tmp


tmp = 0
countstart = 0
while tmp != roopstart:
    firstkouho.append(tmp)
    tmp2 = a[tmp]-1
    tmp = tmp2
    countstart += 1

length = 1
roopkouho.append(roopstart)
if a[roopstart]-1 != roopstart:
    tmp = a[roopstart]-1
    while tmp != roopstart:
        roopkouho.append(tmp)
        length += 1
        tmp2 = a[tmp] - 1
        tmp = tmp2



if k < countstart:
    if countstart != 0:
        print(firstkouho[k]+1)
    else:
        print(1)
else:
    r = k-countstart
    print(roopkouho[r%length]+1)