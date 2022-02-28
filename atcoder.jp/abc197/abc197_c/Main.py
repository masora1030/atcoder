class SegmentTree:
    def __init__(self, size, f=lambda x, y: x+y, default=0):
        self.size=2**(size-1).bit_length()
        self.default=default
        self.dat=[default]*(self.size*2)
        self.f=f

    def update(self, i, x):
        i+=self.size
        self.dat[i]=x
        while i>0:
            i>>=1
            self.dat[i]=self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l+=self.size
        r+=self.size
        lres, rres=self.default, self.default
        while l<r:
            if l & 1:
                lres=self.f(lres, self.dat[l])
                l+=1

            if r & 1:
                r-=1
                rres=self.f(self.dat[r], rres)
            l>>=1
            r>>=1
        res=self.f(lres, rres)
        return res

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    seg = SegmentTree(n,lambda x, y: x|y, 0)
    for i in range(n):
        seg.update(i, a[i])
    ans = inf

    for i in range(2**(n-1)):
        sikiri = []
        for j in range(n-1):
            if (i >> j) & 1:
                sikiri.append(j+1)
        sikiri.append(n)
        now = 0
        tmp_ans = 0
        for pre in sikiri:
            tmp = seg.query(now, pre)
            tmp_ans ^= tmp
            now = pre
        ans = min(tmp_ans, ans)
    print(ans)