import sys
import bisect
from collections import deque
import itertools
import math

# sys.setrecursionlimit(10**4)
from sys import stdin
# readline = stdin.readline
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n,m = lr()
    e = [lr() for i in range(m)]
    # 強連結分解

    import numpy as np
    from scipy.sparse import csr_matrix
    from scipy.sparse.csgraph import connected_components

    edge=np.array(e, dtype=np.int64).T
    tmp=np.ones(m, dtype=np.int64).T
    graph=csr_matrix((tmp, (edge[:]-1)), (n, n))
    num, parents=connected_components(graph, directed=True, connection='strong')
    dic = {}
    for root in parents:
        if root in dic:
            dic[root]+=1
        else:
            dic[root]=1
    ans = 0
    for _,v in dic.items():
        ans+=v*(v-1)//2
    print(ans)