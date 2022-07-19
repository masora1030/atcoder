sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353


def main():
    n=ir()
    visited=set()
    best_s = -1
    best_t = -1
    for i in range(n):
        s,T=sr().split()
        t=int(T)
        if not s in visited:
            visited.add(s)
            if t > best_t:
                best_s = i+1
                best_t = t
    print(best_s)

if __name__=='__main__':
    main()
