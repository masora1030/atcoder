inf = 10**9+7
mod = 10**9+7
n,x = map(int, input().split())
dp_s = [0 for i in range(n+1)]
dp_p = [0 for i in range(n+1)]
dp_s[0] = 1
dp_p[0] = 1
for i in range(n):
    dp_s[i+1] = dp_s[i]*2+3
for i in range(n):
    dp_p[i+1] = dp_p[i]*2+1

def getP(dim, rest):
    if dim == 0:
        if rest == 0:
            return 0
        elif rest == 1:
            return 1
    if rest == 1:
        return 0
    elif 1 < rest < dp_s[dim-1]+2:
        return getP(dim-1, rest-1)
    elif rest == dp_s[dim-1]+2:
        return dp_p[dim-1]+1
    elif dp_s[dim-1]+2 < rest < dp_s[dim]:
        return dp_p[dim-1]+1+getP(dim-1, rest-(dp_s[dim-1]+2))
    elif rest == dp_s[dim]:
        return dp_p[dim]

print(getP(n, x))