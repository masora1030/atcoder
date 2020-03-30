n, k = map(int, input().split())
ans = 0
i=0
pre = 0
tmp = 0
if n >= k:
    ans += (n-k+1)
    pre = k
    i = 1
    tmp = (pre+1)//2
else:
    pre = n+1
    tmp = k
    i=0
    while n < tmp:
        tmp = (tmp+1)//2
        i+=1
    ans += (pre-tmp)*((0.5)**i)
    pre = tmp
    i+=1
    tmp = (pre+1)//2
while pre != tmp:
    # i回コインで面出す必要あり 
    ans += (pre-tmp)*((0.5)**i)
    pre = tmp 
    i+=1
    tmp = (pre+1)//2
print(ans/n)