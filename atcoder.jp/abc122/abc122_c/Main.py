n,q = map(int, input().split())
s = input()
af = False
AClist = [0 for i in range(10**5)]
for i,c in enumerate(s):
    if af:
        if c == 'C':
            AClist[i-1]+=1
            af = False
        elif c != 'A':
            af = False
    else:
        if c == 'A':
            af = True

a2=[0]
for i in AClist:a2.append(a2[-1]+i)
def SumArea(l, r):
    return a2[r]-a2[l]

ans = []
for i in range(q):
    l,r = map(int, input().split())
    print(SumArea(l-1, r-1))