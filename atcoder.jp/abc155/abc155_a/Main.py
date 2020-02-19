import sys
a,b,c = map(int, input().split())
if (a == b or b == c or a == c) and (not (a == b and b == c)):
    print('Yes')
    sys.exit()
print('No')