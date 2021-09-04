sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    s = [sr() for i in range(3)]
    pre_ans = ["ABC", "ARC", "AGC", "AHC"]
    for ans in pre_ans:
        if not ans in s:
            print(ans)