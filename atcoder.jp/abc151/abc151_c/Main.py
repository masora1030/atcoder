n,m = map(int, input().split())
AC = 0
WA = 0
ACflag = [False for i in range(n)]
thisWA = [0 for i in range(n)]
for i in range(m):
    p,S = map(str, input().split())
    if ACflag[int(p)-1] == False:
        if S == 'AC':
            AC+=1
            ACflag[int(p)-1] = True
        if S == 'WA':
            thisWA[int(p)-1]+=1
            
for i in range(n):
    if ACflag[i] == True:
        WA+=thisWA[i]

print('{} {}'.format(AC, WA))