n,k,q = map(int, input().split())
pdic = {}
for i in range(q):
    p = int(input())
    if p in pdic:
        pdic[p] += 1
    else:
        pdic[p] = 1
for i in range(1,n+1):
    if i in pdic:
        if k + pdic[i] - q <= 0:
            print('No')
        else:
            print('Yes')
    else:
        if k - q <= 0:
            print('No')
        else:
            print('Yes')