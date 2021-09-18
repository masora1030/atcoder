sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    s = [sr() for i in range(4)]
    s.sort()
    ans = ['2B', '3B', 'H', 'HR']
    flg = True
    for i,c in enumerate(s):
        if c != ans[i]:
            flg = False
            break
    if flg:
        print('Yes')
    else:
        print('No')