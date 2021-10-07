import random
sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=100
    max_score = 200000000
    a = [lr() for i in range(n)]
    b = [[0 for i in range(n)]for j in range(n)]
    m_p = [[0 for i in range(n)]for j in range(n)]

    def init_b():
        # sigma(i)(hi) ;= a0 + sigma(i!=k)(|xi-xk|+|yi-yk|)
        total_dist = 2*n-2
        ind=0
        for i in range(32):
            for j in range(32):
                if ind<999:
                    total_dist+=(i+j)*3
                    ind+=1
                else:
                    break
        total_h = a[0][0] + total_dist
        total_h //= 2000

        m_p[n-1][n-1]=total_h
        ind=0
        for i in range(32):
            for j in range(32):
                if ind<999:
                    m_p[i*3][j*3]=total_h
                    ind+=1
                else:
                    break

    def submit():
        q = 0
        ans = []
        for i in range(n):
            for j in range(n):
                if m_p[i][j] > 0:
                    q+=1
                    ans.append([j,i,m_p[i][j]])
        print(q)
        for l in ans:
            print(*l, sep=' ')

    init_b()
    submit()