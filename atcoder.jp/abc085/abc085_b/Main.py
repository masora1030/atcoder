inf = 10 ** 15
mod = 10 ** 9 + 7

n = int(input())
d = [list(map(int, input().split())) for i in range(n)]
d.sort()
pre = 0
count= 0
for num in d:
    if pre != num:
        count+=1
    pre = num
print(count)