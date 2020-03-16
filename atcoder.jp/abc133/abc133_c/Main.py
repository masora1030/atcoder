# C
l,r = map(int, input().split())
mod = 2019
if r-l >= mod:
    print(0)
else:
    minnum = 2019
    for i in range(l,r):
        for j in range(i+1,r+1):
            tmp = ((i%mod)*(j%mod))%mod
            if tmp < minnum:
                minnum = tmp
    print(minnum)