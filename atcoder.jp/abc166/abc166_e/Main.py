import bisect
inf = 10**15
mod = 10**9+7
n = int(input())
a = list(map(int, input().split()))
dicL = [a[i]+i for i in range(n)]
dicR = [i-a[i] for i in range(n)]
dicL.sort()
dicR.sort()
ans = 0
for x in range(n-1):
    indL = bisect.bisect_left(dicL, x)
    indR = bisect.bisect_left(dicR, x)
    countL = 0
    countR = 0
    while indL != n and dicL[indL] == x:
        countL+=1
        indL+=1
    while indR != n and dicR[indR] == x:
        countR+=1
        indR+=1
    ans+=countL*countR
print(ans)