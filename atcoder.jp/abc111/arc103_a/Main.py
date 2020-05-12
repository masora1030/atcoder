# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)

inf = 10 ** 15
mod = 10 ** 9 + 7
n = int(input())
v = list(map(int, input().split()))

# 偶数番目の要素において、iの数が何個あったか
even = [0 for i in range(100001)]
# 奇数番目の要素において、iの数が何個あったか
odd = [0 for i in range(100001)]

# 偶数番目、奇数番目の要素、それぞれ数える
for i in range(0, n-1, 2):
    even[v[i]] += 1
    odd[v[i+1]] += 1

# 偶数番目の要素のうち最も多かった数値
maxeveni = -1
# 偶数番目の要素のうち最も多かった数値の個数
maxeven = 0
# 偶数番目の要素のうち2番目に多かった数値の個数
preeven = 0

# 奇数番目の要素のうち最も多かった数値
maxoddi = -1
# 奇数番目の要素のうち最も多かった数値の個数
maxodd = 0
# 奇数番目の要素のうち2番目に多かった数値の個数
preodd = 0

# 偶数番目の要素を走査
for i in range(1, 100001):
    num = even[i]
    if maxeven <= num:
        maxeveni = i
        preeven = maxeven
        maxeven = num
    elif preeven <= num:
        preeven = num

# 奇数番目の要素を走査
for i in range(1, 100001):
    num = odd[i]
    if maxodd <= num:
        maxoddi = i
        preodd = maxodd
        maxodd = num
    elif preodd <= num:
        preodd = num

ans = 0

# 要素のうち最も多かった数値が偶数番目と奇数番目で一致していなかった場合
if maxeveni != maxoddi:
    ans = n - maxeven - maxodd
# 要素のうち最も多かった数値が偶数番目と奇数番目で一致していた場合
else:
    ans = min(n - preeven - maxodd, n - maxeven - preodd)
print(ans)