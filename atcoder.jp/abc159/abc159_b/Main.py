s = input()
n = len(s)
a = s[:(n-1)//2]
b = s[((n+3)//2)-1:]
if a == b:
    a_rev = a[::-1]
    b_rev = b[::-1]
    if a == a_rev and b == b_rev:
        print('Yes')
    else:
        print('No')
else:
    print('No')