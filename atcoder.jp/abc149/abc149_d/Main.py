n,k = map(int, input().split())
r,s,p = map(int, input().split())
t = input()
total = 0
pre = 'n'

def JSC(hand):
    if hand == 'r':
        return p
    elif hand == 's':
        return r
    else:
        return s

for i in range(k):
    pre = 'n'
    for j in range(n//k+1):
        l = i+j*k
        if l < n:
            if t[l] != pre:
                total += JSC(t[l])
                pre = t[l]
            else:
                pre = 'n'
print(total)