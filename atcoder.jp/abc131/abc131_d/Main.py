# D
import sys
n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
ab.sort(key=lambda x: x[1])
time = 0
for work in ab:
    if time+work[0] <= work[1]:
        time+=work[0]
    else:
        print('No')
        sys.exit()
print('Yes')