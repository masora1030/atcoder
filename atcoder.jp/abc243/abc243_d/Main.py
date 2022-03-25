sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

import sys

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    n,x = lr()
    s = sr()
    def_roots = []
    while x != 1:
        if x%2 == 0:
            def_roots.append('L')
            x//=2
        else:
            def_roots.append('R')
            x//=2
    def_roots.reverse()
    def_roots.append(s)
    roots = ''.join(def_roots)

    f = 0
    stack = []
    w = 0
    for c in roots:
        if c == 'U':
            f-=1
            dir = stack.pop()
            if dir == 'R':
                w-=1
            else:
                w+=1
        elif c=='R':
            f+=1
            stack.append('R')
            w+=1
        else:
            f+=1
            stack.append('L')
            w-=1

    ans = 1
    for c in stack:
        if c=='R':
            ans*=2
            ans+=1
        else:
            ans*=2
    print(ans)


if __name__ == '__main__':
    main()
