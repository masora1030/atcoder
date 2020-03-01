# D 解き直し
# Union Find
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    
n,m,k = map(int, input().split())
not_ans = [1 for i in range(n)]
ans = [0 for i in range(n)]
unions = UnionFind(n)
for i in range(m):
    a,b = map(int, input().split())
    not_ans[a-1] += 1
    not_ans[b-1] += 1
    unions.union(a-1, b-1)
for i in range(k):
    a,b = map(int, input().split())
    if unions.same(a-1, b-1):
        not_ans[a-1] += 1
        not_ans[b-1] += 1
for i in range(n):
    ans[i] = unions.size(i) - not_ans[i]
print(*ans)