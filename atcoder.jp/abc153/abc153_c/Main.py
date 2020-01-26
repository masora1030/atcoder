import sys
n,k = map(int, input().split())
hlist = list(map(int, input().split()))
hlist.sort(reverse=True)
total = 0
if k >= n:
    print(0)
    sys.exit()
else:
    for i in range(k,n):
       total += hlist[i]
    print(total)