# A
import sys
s = input()
dic = {}
for c in s:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1
for v in dic.values():
    if v != 2:
        print('No')
        sys.exit()
print('Yes')