import sys
import bisect

# sys.setrecursionlimit(10**4)
# from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
mod=10**9+7
# mod = 998244353

if __name__=='__main__':
    n,q = lr()
    a = lr()
    a.sort()
    tmp = []
    pre = -1
    max_int = 10**18+10**7
    dic = {}

    for num in a:
        if pre != num:
            tmp.append(num)
            dic[num] = 1
        pre = num

    def judge(mid, x):
        ind = bisect.bisect_left(tmp, mid)
        flg = False
        if ind<len(tmp) and tmp[ind] == mid:
            ind+=1
            flg = True
        ret = mid-ind
        if flg:
            if ret <= x-1:
                return True
            else:
                return False
        else:
            if ret <= x:
                return True
            else:
                return False

    for i in range(q):
        x = ir()
        l = 1
        r = max_int
        mid = (l+r)//2
        while r-l > 1:
            mid = (l+r)//2
            if judge(mid, x):
                l = mid
            else:
                r = mid
        ans = l

        print(ans)