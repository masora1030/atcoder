import bisect
import heapq  # 優先度付きキュー(最小値取り出し)

inf = 10 ** 15
mod = 10 ** 9 + 7

p = [] # i*2-1番までで取りうる最大の数
m = [] # i*2番までで取りうる最小の数
prep = 0
prem = 0
kaijou = []
for i in range(0,35,2):
    p.append(2**i+prep)
    m.append(2**(i+1)+prem)
    kaijou.append(2**i)
    kaijou.append(2**(i+1))
    prep = 2**i+prep
    prem = 2**(i+1)+prem

def getAns(n,i):

    if i == 0:
        if n == 0:
            return '0'
        if n == 1:
            return '1'
    else:
        if n == 0 or n == 1:
            return ''.join(['0', getAns(n, i-1)])
        elif n > 0:
            ind = bisect.bisect_left(p, n)
            if ind*2 == i:
                n -= kaijou[i]
                return ''.join(['1', getAns(n, i-1)])
            else:
                return ''.join(['0', getAns(n, i-1)])
        else:
            ind = bisect.bisect_left(m, abs(n))
            if ind*2+1 == i:
                n += kaijou[i]
                return ''.join(['1', getAns(n, i-1)])
            else:
                return ''.join(['0', getAns(n, i-1)])


n = int(input())
if n >= 0:
    ind = bisect.bisect_left(p, n)
    print(getAns(n,ind*2))
else:
    ind = bisect.bisect_left(m, abs(n))
    print(getAns(n,ind*2+1))