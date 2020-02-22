n = int(input())
x = list(map(int, input().split()))
mean1 = sum(x)//len(x)
mean2 = mean1+1
ans1 = 0
ans2 = 0
for num in x:
    ans1 += (num - mean1)**2
    ans2 += (num - mean2)**2
print(min(ans1,ans2))