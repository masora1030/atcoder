import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)

inf = 10 ** 15
mod = 10 ** 9 + 7

s = input()
length = len(s)
if s[0] == 'A':
    tmp = s[2:length-1]
    count = 0
    if s[1].isupper():
        print('WA')
        sys.exit()
    for c in tmp:
        if c.isupper():
            if c == 'C':
                count += 1
            else:
                print('WA')
                sys.exit()
    if count == 1 and s[-1].islower():
        print('AC')
    else:
        print('WA')

else:
    print('WA')