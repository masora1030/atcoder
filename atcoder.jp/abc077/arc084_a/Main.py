# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7
import bisect
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
b.sort()
c.sort()
b_len = len(b)
c_len = len(c)
count = 0
b_list = [0 for i in range(b_len)]

for i,num in enumerate(b):
    ind_c = bisect.bisect_left(c, num)
    if c_len == ind_c:
        continue
    else:
        if c[ind_c] == num:
            ind_c = bisect.bisect_left(c, num+1)
            if c_len == ind_c:
                continue
            else:
                b_list[i] = c_len - ind_c
        else:
            b_list[i] = c_len-ind_c

# 累積和
a2 = [0]
for i in b_list:a2.append(a2[-1]+i)
def SumArea(l, r):
    return a2[r]-a2[l]


for num in a:
    ind_b = bisect.bisect_left(b, num)
    if b_len == ind_b:
        continue
    else:
        if b[ind_b] == num:
            ind_b = bisect.bisect_left(b, num+1)
            if b_len == ind_b:
                continue
            else:
                count += SumArea(ind_b, b_len)
        else:
            count += SumArea(ind_b, b_len)
print(count)
