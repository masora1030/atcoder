# segment tree
class SegmentTree:
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x, y: x+y, default=0):
        self.size=2**(size-1).bit_length()  # 簡単のため要素数Nを2冪にする
        self.default=default
        self.dat=[default]*(self.size*2)  # 要素を単位元で初期化
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
                rres=self.f(self.dat[r], rres)  # モノイドでは可換律は保証されていないので演算の方向に注意
            l>>=1
            r>>=1
        res=self.f(lres, rres)
        return res

# from sys import stdin
# readline = stdin.readline
# sr=lambda: readline()
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    q=ir()
    qs=[lr() for _ in range(q)]
    # zaatu
    num2ind = {}
    ind2num = {}
    numlist = set()
    for ql in qs:
        numlist.add(ql[1])
    ind=0
    for num in sorted(numlist):
        num2ind[num]=ind
        ind2num[ind]=num
        ind+=1
    n=ind
    seg = SegmentTree(n)

    def judge2(mid, x, k):
        if seg.query(mid, x+1) >= k:
            return True
        else:
            return False
    def judge3(mid, x, k):
        if seg.query(x, mid+1) >= k:
            return True
        else:
            return False

    def get_ans2(x, k):
        l=0
        r=x+1
        while r-l > 1:
            mid = l+(r-l)//2
            if judge2(mid, x, k):
                l=mid
            else:
                r=mid
        return l

    def get_ans3(x, k):
        l=x-1
        r=n
        while r-l > 1:
            mid = l+(r-l)//2
            if judge3(mid, x, k):
                r=mid
            else:
                l=mid
        return r


    for ql in qs:
        if ql[0] == 1:
            ind_num = num2ind[ql[1]]
            seg.update(ind_num, seg.query(ind_num, ind_num+1)+1)
        elif ql[0] == 2:
            ind_num=num2ind[ql[1]]
            k=ql[2]
            if seg.query(0,ind_num+1) < k:
                print(-1)
            else:
                print(ind2num[get_ans2(ind_num, k)])
        else:
            ind_num=num2ind[ql[1]]
            k=ql[2]
            if seg.query(ind_num, n)<k:
                print(-1)
            else:
                print(ind2num[get_ans3(ind_num, k)])


if __name__ == '__main__':
    main()
