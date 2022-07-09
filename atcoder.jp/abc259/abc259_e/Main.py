sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))

inf=10**18
mod = 10**9+7
# mod=998244353

def main():
    n=ir()
    p_max_i={} # p : [max_i1, max_i2, ... ,max_ik]
    p_max = {} # p : max_e
    maxs=[set() for _ in range(n)]
    for i in range(n):
        m = ir()
        for _ in range(m):
            p,e = lr()
            if p in p_max:
                if p_max[p] < e:
                    # update max
                    for pre_i in p_max_i[p]:
                        maxs[pre_i].remove(p)
                    maxs[i].add(p)
                    p_max[p] = e
                    p_max_i[p] = [i]
                elif p_max[p] == e:
                    # add p
                    maxs[i].add(p)
                    p_max_i[p].append(i)
            else:
                p_max[p] = e
                p_max_i[p] = [i]
                maxs[i].add(p)

    # print(maxs)
    ans_hash = set()

    for l in maxs:
        tmp_list = []
        for num in l:
            if len(p_max_i[num]) == 1:
                tmp_list.append(num)
        fs = frozenset(tmp_list)
        ans_hash.add(fs)

    print(len(ans_hash))


if __name__ == '__main__':
    main()
