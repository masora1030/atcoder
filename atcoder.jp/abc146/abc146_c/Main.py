def num2dim(num):
    if num == 0:
        return 1
    dim = 0
    while num != 0:
        dim+=1
        num = num//10
    return dim

def getCost(n,a,b):
    return a*n + num2dim(n)*b

a,b,x = map(int, input().split())
max = 10**9
if getCost(max,a,b) <= x:
    print(max)
elif getCost(0,a,b) > x:
    print(0)
else:
    l = 0
    r = max
    mean = (l + r)//2
    while l != r:
        if x > getCost(mean,a,b):
            l = mean + 1
        else:
            r = mean
        mean = (l + r)//2
    ans = mean
    if getCost(ans,a,b) > x:
        ans = mean - 1
    print(ans)