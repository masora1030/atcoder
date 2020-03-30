s = input()
s1 = int(s[:2])
s2 = int(s[2:])
MMYY = False
YYMM = False
if 0<s1<13:
    MMYY = True
if 0<s2<13:
    YYMM = True
if MMYY and YYMM:
    print('AMBIGUOUS')
elif MMYY:
    print('MMYY')
elif YYMM:
    print('YYMM')
else:
    print('NA')