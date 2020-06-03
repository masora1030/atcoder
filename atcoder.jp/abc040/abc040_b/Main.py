n=int(input())
ans=10**9+7
for w in range(1,n+1):
    h = n//w
    amari = n-(h*w)
    sm = abs(w-h) + amari
    ans = min(sm,ans)
print(ans)