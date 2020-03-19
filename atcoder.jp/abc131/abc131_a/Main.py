# A
import sys
s = input()
pre = ''
for c in s:
    if c == pre:
        print('Bad')
        sys.exit()
    pre = c
print('Good')