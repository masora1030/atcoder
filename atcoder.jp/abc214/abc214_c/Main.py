sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

inf=10**18
# mod=10**9+7
mod = 998244353

if __name__=='__main__':
    n=ir()
    s=lr()
    t=lr()
    st = []
    min_t_ind=-1
    min_t = inf
    for i in range(n):
        st.append([s[i], t[i]])
        if min_t > t[i]:
            min_t = t[i]
            min_t_ind = i
    now = min_t
    ans = [-1 for i in range(n)]
    for j in range(n):
        ind = (min_t_ind+j)%n
        if st[ind][1] < now:
            now = st[ind][1]
            ans[ind] = now
            now+=st[ind][0]
        else:
            ans[ind] = now
            now+=st[ind][0]
    for i in range(n):
        print(ans[i])