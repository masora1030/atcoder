import sys
# from sys import stdin
# readline = stdin.readline
sr = lambda: input()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

import bisect

from sys import stdout

inf = 10 ** 18
# mod = 10 ** 9 + 7
mod = 998244353
# len(bin(n)) - bin(n).rfind("1") - 1

import random
import itertools

if __name__=='__main__':
    s = [sr() for i in range(3)]
    dic = {}
    for ss in s:
        for c in ss:
            dic[c] = -1
    n = len(dic.keys())
    for tuple in itertools.permutations(range(10), n):
        for i,k in enumerate(list(dic.keys())):
            dic[k] = tuple[i]
        ns = []
        if dic[s[0][0]] == 0 or dic[s[1][0]] == 0 or dic[s[2][0]] == 0:
            continue
        for ss in s:
            tmp = 0
            for c in ss:
                tmp*=10
                tmp+=dic[c]
            ns.append(tmp)
        if ns[0]+ns[1] == ns[2]:
            for j in range(3):
                print(ns[j])
            sys.exit()
    print("UNSOLVABLE")