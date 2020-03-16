# B
n,d = map(int, input().split())
xi = [list(map(int, input().split())) for i in range(n)]
heihou = [i*i for i in range(200)]
count=0
for i in range(n-1):
    for j in range(i+1, n):
        total = 0
        for k in range(d):
            h = xi[i][k] - xi[j][k]
            hpow = h*h
            total+=hpow
        if total in heihou:
            count+=1
print(count)