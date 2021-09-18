sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    di = sr()
    dic_a = {}
    for i in range(26):
        dic_a[di[i]] = chr(ord('a')+i)
    n=ir()
    dic = {}
    lis = []
    for _ in range(n):
        a = sr()
        tmp = []
        for c in a:
            tmp.append(dic_a[c])
        t = ''.join(tmp)
        lis.append(t)
        dic[t] = a
    lis.sort()
    for a in lis:
        print(dic[a])
