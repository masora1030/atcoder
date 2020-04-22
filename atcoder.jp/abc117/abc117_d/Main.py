inf = 10**9+7
mod = 10**9+7
n, k = map(int, input().split())
a = list(map(int, input().split()))
rep = len(bin(k)) - 2
ans = 0
totala = 0
if k != 0:
    for i in range(rep):
        count1 = 0
        count0 = 0
        for j in range(n):
            if ((a[j] >> (rep-1-i)) & 1): # 最大でrep-1回シフト
                count0+=1
            else:
                count1+=1
        if count1 > count0:
            ans += (2**(rep-1-i))
    anslist = []
    for i in range(rep):
        tmp = 0
        if (k >> (rep-1-i) & 1):
            for j in range(rep):
                if j > i:
                    tmp+=(ans>>(rep-1-j) & 1)*(2**(rep-1-j))
                if j < i:
                    tmp+=(k>>(rep-1-j) & 1)*(2**(rep-1-j))
            anslist.append(tmp)
    anslist.append(k)
    for num in anslist:
        total = 0
        for i in range(n):
            total += (num ^ a[i])
        totala = max(totala, total)
else:
    for i in range(n):
        totala += (ans ^ a[i])

print(totala)