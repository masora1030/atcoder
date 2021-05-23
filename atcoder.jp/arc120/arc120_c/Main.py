class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)

    def __iter__(self):
        psum = 0
        for i in range(self.size):
            csum = self.sum(i+1)
            yield csum - psum
            psum = csum
        raise StopIteration()

    def __str__(self):  # O(nlogn)
        return str(list(self))

    def sum(self, i):
        # [0, i) の要素の総和を返す
        if not (0 <= i <= self.size): raise ValueError("error!")
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def __getitem__(self, key):
        if not (0 <= key < self.size): raise IndexError("error!")
        return self.sum(key+1) - self.sum(key)

    def __setitem__(self, key, value):
        # 足し算と引き算にはaddを使うべき
        if not (0 <= key < self.size): raise IndexError("error!")
        self.add(key, value - self[key])

import sys

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    a=lr()
    b=lr()
    if sum(a) != sum(b):
        print(-1)
        sys.exit()
    a_0 = {}
    b_0 = {}
    dp = [0 for i in range(n)]
    for i in range(n):
        if a[i]+i in a_0:
            a_0[a[i]+i].append(i)
        else:
            a_0[a[i]+i]=[i]
        if b[i]+i in b_0:
            b_0[b[i]+i].append(i)
        else:
            b_0[b[i]+i]=[i]
    ans = 0
    for k,v in b_0.items():
        if (not k in a_0) or len(v) != len(a_0[k]):
            print(-1)
            sys.exit()
        for i in range(len(v)):
            dp[a_0[k][i]]=b_0[k][i]

    bit=Bit(max(dp)+1)
    ans=0
    for i, a in enumerate(dp):
        ans+=i-bit.sum(a+1)
        bit.add(a, 1)
    print(ans)