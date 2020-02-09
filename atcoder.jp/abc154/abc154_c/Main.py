import sys
n = int(input())
s = list(map(int, input().split()))
s.sort()
k = 0
for i in s:
    if i == k:
        print('NO')
        sys.exit()
    k = i
print('YES')