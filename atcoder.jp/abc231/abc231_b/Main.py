sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    dic={}
    for i in range(n):
        s=sr()
        if not s in dic:
            dic[s] = 1
        else:
            dic[s]+=1
    a = list(dic.items())
    a.sort(key=lambda x:x[1])
    print(a[-1][0])