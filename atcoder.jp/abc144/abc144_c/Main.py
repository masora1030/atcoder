import math
n = int(input())
s = math.sqrt(n)
s = int(s)
for i in range(s):
    if n%(s-i) == 0:
        k = n//(s-i)
        print(k+s-i-2)
        break