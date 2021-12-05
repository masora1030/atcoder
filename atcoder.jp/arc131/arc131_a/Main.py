sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    a=ir()
    b=ir()
    tmp1 = a
    tmp2 = b//2
    if b%2 == 0:
        if tmp2 == 0:
            tmp2 = ''
        ans = ''.join([str(tmp2), '0', str(tmp1)])
    else:
        if tmp2 == 0:
            tmp2 = ''
        ans = ''.join([str(tmp2), '5', str(tmp1)])
    print(ans)
