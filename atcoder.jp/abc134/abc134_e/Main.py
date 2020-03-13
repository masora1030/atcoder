# E
n = int(input())
from collections import deque
import bisect
first = int(input())
a = [first]
a = deque(a) # でキュー化

for i in range(n-1):
    num = int(input())
    
    if num <= a[0]:
        a.appendleft(num)
    else:
        ind = bisect.bisect_left(a, num)
        ind-=1
        a[ind]=num
print(len(a))