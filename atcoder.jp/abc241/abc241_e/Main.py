sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
# mod = 10**9+7
mod=998244353

import bisect

def main():
    n,k = lr()
    a = lr()
    total = 0
    inds = []
    totals = [0]
    ind2k = {}
    count=0
    roop_first_ind = -1
    while True:
        next_ind = total%n
        next_num = a[next_ind]
        if next_ind in ind2k:
            ind2k[next_ind].append(count)
            roop_first_ind = next_ind
            break
        else:
            total+=next_num
            totals.append(total)
            ind2k[next_ind] = [count]
            count+=1
            inds.append(next_ind)
    roop_first_by_inds = ind2k[roop_first_ind][0]
    roop_end_by_inds = ind2k[roop_first_ind][1]
    roop_total = totals[-1]-totals[roop_first_by_inds]
    first_total = totals[roop_first_by_inds]-totals[0]
    first_length = roop_first_by_inds
    roop_length = roop_end_by_inds-roop_first_by_inds
    first_0 = totals[:roop_first_by_inds+1]
    roop_1 = [0]
    for i in range(roop_first_by_inds, roop_first_by_inds+roop_length):
        roop_1.append(roop_1[-1]+(totals[i+1]-totals[i]))
    if k <= first_length:
        print(first_0[k]-first_0[0])
    else:
        ret = k-first_length
        ans = first_total
        tmp = ret//roop_length
        amari = ret%roop_length
        ans += tmp*roop_total
        ans += roop_1[amari]-roop_1[0]
        print(ans)


if __name__ == '__main__':
    main()
