import sys
inf = 10**15
mod = 10**9+7
n, y = map(int, input().split())
ans=0
A = y//10000
for i in range(A+1):
    restY = y-i*10000
    restN = n-i
    if restY >= 0 and restN >= 0:
        B = restY//5000
        for j in range(B+1):
            restYY = restY-j*5000
            restNN = restN-j
            if restNN>=0 and restYY == restNN*1000:
                print('{} {} {}'.format(i,j,restNN))
                sys.exit()
print('{} {} {}'.format(-1,-1,-1))