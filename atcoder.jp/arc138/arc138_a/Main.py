import bisect
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res

def main():
    n,k = lr()
    a = lr()
    val_ind = [[num,i] for i,num in enumerate(a[k:])]
    val_ind.sort()
    vals = [num for num,i in val_ind]
    inds = [i for num,i in val_ind]
    seg = SegmentTree(len(inds), min, inf)
    for i, num in enumerate(inds):
        seg.update(i, num)
    ans = inf
    for i,num in enumerate(a[:k]):
        ind = bisect.bisect_left(vals, num+1)
        if ind < len(inds):
            target_ind = seg.query(ind, len(inds))
            ans = min(ans, target_ind+k-i)
    if ans != inf:
        print(ans)
    else:
        print(-1)

if __name__ == '__main__':
    main()
