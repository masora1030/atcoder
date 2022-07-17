class Bit:
    def __init__(self, n):
        self.size=n
        self.tree=[0]*(n+1)
        self.depth=n.bit_length()

    def sum(self, i):
        s=0
        while i>0:
            s+=self.tree[i]
            i-=i & -i
        return s

    def add(self, i, x):
        while i<=self.size:
            self.tree[i]+=x
            i+=i & -i

    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_=0
        pos=0
        for i in range(self.depth, -1, -1):
            k=pos+(1 << i)
            if k<=self.size and sum_+self.tree[k]<x:
                sum_+=self.tree[k]
                pos+=1 << i
        return pos+1, sum_

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,k=lr()
    p=lr()
    bit = Bit(n+1)
    members = {} # root:[chi, chi, ...]
    last_num = {} # last:root
    ans = [-1 for _ in range(n)]
    if k == 1:
        for t,num in enumerate(p):
            ans[num-1] = t+1
    else:
        for t,num in enumerate(p):
            items = bit.lower_bound(bit.sum(num)+1)
            item = items[0]
            if item == n+2:
                bit.add(num,1)
                last_num[num] = num
                members[num] = [num]
            else:
                bit.add(item,-1)
                bit.add(num,1)
                last_num[num] = last_num[item]
                members[last_num[num]].append(num)
                if len(members[last_num[num]]) == k:
                    for chi in members[last_num[num]]:
                        ans[chi-1] = t+1
                    bit.add(num,-1)
    for a in ans:
        print(a)


if __name__ == '__main__':
    main()
