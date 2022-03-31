sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

num_l = 0

def main():
    t=ir()
    for _ in range(t):
        n,m=lr()
        ans=-inf
        xy = [lr() for _ in range(n)]
        b_totals1 = [0]
        for x,y in xy:
            b_totals1.append(b_totals1[-1]+x*y)
        pre_ans=0
        for i in range(n):
            l_num = b_totals1[i]+xy[i][0]
            r_num = b_totals1[i+1]
            if l_num >= 0 and r_num < 0:
                nums_tmp = l_num // (-xy[i][0])
                r_num_tmp = l_num+nums_tmp*xy[i][0]
                nums_tmp+=1
                pre_pre_ans=pre_ans+(l_num+r_num_tmp)*nums_tmp//2
                ans=max(ans,pre_pre_ans)
            nums = xy[i][1]
            pre_ans+=(l_num+r_num)*nums//2
            ans=max(ans,pre_ans)
        if ans < 0:
            ans=max(ans,xy[0][0])
        print(ans)

if __name__ == '__main__':
    main()
