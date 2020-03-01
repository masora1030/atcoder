# B
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
ans = 0
past = -2
for index in a:
    ans += b[index-1]
    if past == index-1:
        ans += c[index-2]
    past = index
print(ans)