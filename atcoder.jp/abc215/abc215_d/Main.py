def factorization(n):
    arr = []
    temp = n
    if n == 1:
        return arr

    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n,m = lr()
    a = lr()
    ans = [True for i in range(m+1)]
    sos = {}
    for num in a:
        l = factorization(num)
        for k,v in l:
            sos[k] = True
    for k in sorted(list(sos.keys())):
        for tmp in range(k,m+1,k):
            ans[tmp] = False
    anss = []
    ans_len = 0
    for i in range(1,m+1):
        if ans[i]:
            anss.append(i)
            ans_len+=1
    print(ans_len)
    for num in anss:
        print(num)