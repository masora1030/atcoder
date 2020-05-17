import math
import sys
import bisect
import heapq  # 優先度付きキュー(最小値取り出し)

inf = 10 ** 15
mod = 10 ** 9 + 7
a,b,h,m = map(int, input().split())
p = math.pi

arg = 2*p*(h/12)
arg = arg-11/360*p*m
arg = min(abs(arg), 2*p-abs(arg))
xx = a*a+b*b-2*a*b*math.cos(arg)
print(math.sqrt(xx))