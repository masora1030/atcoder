# C
n = int(input())
d = list(map(int, input().split()))
d.sort()
if n%2 == 1:
    print(0)
else:
    mi = n//2-1
    ml = d[mi]
    mr = d[mi+1]
    print(mr-ml)