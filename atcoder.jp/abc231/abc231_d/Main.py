# Union Find
class UnionFind():
    def __init__(self, n):
        self.n=n
        self.parents=[-1]*n

    def find(self, x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x=self.find(x)
        y=self.find(y)

        if x==y:
            return

        if self.parents[x]>self.parents[y]:
            x, y=y, x

        self.parents[x]+=self.parents[y]
        self.parents[y]=x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def members(self, x):
        root=self.find(x)
        return [i for i in range(self.n) if self.find(i)==root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x<0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def all_family_count(self):
        return [-min(0, x) for i, x in enumerate(self.parents)]

    def memberlist(self):
        self.L=[set() for _ in range(self.n)]
        for i in range(self.n):
            if self.parents[i]<0:
                self.L[i].add(i)
            else:
                self.L[self.find(i)].add(i)
        return self.L

import sys

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    n,m = lr()
    if m > n-1:
        print("No")
        sys.exit()
    uf = UnionFind(n)
    dic = {}
    flg = True
    for _ in range(m):
        a,b = lr()
        a-=1
        b-=1
        if uf.same(a,b):
            flg = False
            break
        else:
            uf.union(a,b)
        if a in dic:
            dic[a]+=1
        else:
            dic[a]=1
        if b in dic:
            dic[b]+=1
        else:
            dic[b]=1
        if dic[a] > 2 or dic[b] > 2:
            flg = False
            break
    if flg:
        print("Yes")
    else:
        print("No")