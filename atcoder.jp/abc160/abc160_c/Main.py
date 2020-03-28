k,n = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
maxdis = 0
pre = a[-1] - k
for dis in a:
    t = dis - pre
    pre = dis
    if t > maxdis:
        maxdis = t
print(k-maxdis)