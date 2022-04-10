from collections import deque

sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    q=ir()
    que = deque([])
    for _ in range(q):
        query = lr()
        if query[0] == 1:
            x,c = query[1:]
            que.append([x,c])
        else:
            c = query[1]
            ret = c
            ans = 0
            while que and ret >= que[0][1]:
                now_x, now_c = que.popleft()
                ans+=now_x*now_c
                ret-=now_c
            if ret:
                que[0][1]-=ret
                ans+=ret*que[0][0]
            print(ans)


if __name__ == '__main__':
    main()
