inf = 10**15
mod = 10**9+7
n = int(input())
w = [int(input()) for i in range(n)]

import bisect
a = [1, 2, 3, 5, 6, 7, 8, 9, 11]
bisect.insort_left(a, 4)        #4を挿入
b=bisect.bisect_left(a, 9)   #8の位置はどこ？(0オリジン)


maxweigt = []
for i in range(n):
    ind = bisect.bisect_left(maxweigt, w[i])
    if ind < len(maxweigt):
        if maxweigt[ind] > w[i]:
            maxweigt[ind] = w[i]
    else:
        bisect.insort_left(maxweigt, w[i])
print(len(maxweigt))