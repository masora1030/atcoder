sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# mod = 10**9+7
mod = 998244353

if __name__=='__main__':
    h,w = lr()
    c = [list(sr()) for i in range(h)]
    kouho = [[set() for j in range(w)] for i in range(h)]
    kind = ['1', '2', '3', '4', '5']
    dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for i in range(h):
        for j in range(w):
            if c[i][j] == '.':
                se = set()
                # 周辺の色をみて候補確定
                for dh,dw in dir:
                    nh,nw = i+dh, j+dw
                    if 0 <= nh < h and 0 <= nw < w:
                        se.add(c[nh][nw])
                for k in kind:
                    if not k in se:
                        kouho[i][j].add(k)
            else:
                kouho[i][j].add(c[i][j])
    ans = [['' for j in range(w)] for i in range(h)]
    for i in range(h):
        for j in range(w):
            se=set()
            for dh, dw in dir:
                nh, nw=i+dh, j+dw
                if 0<=nh<h and 0<=nw<w:
                    se.add(ans[nh][nw])
            for k in kouho[i][j]:
                if not k in se:
                    ans[i][j] = k
                    break
    for i in range(h):
        print(*ans[i], sep="")
