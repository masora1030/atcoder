sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n=sr()
    if len(n) == 1:
        print(''.join(['AGC00', n]))
    else:
        if int(n) >= 42:
            n = str(int(n)+1)
        print(''.join(['AGC0', n]))
