# input()
# int(input())
# map(int, input().split())
# list(map(int, input().split()))
import sys
inf = 10**9+7
mod = 10**9+7

n = int(input())
s = input()
judge = [[[True for k in range(10)]for j in range(10)]for i in range(10)]
judge_first = [True for i in range(10)]
judge_second = [[True for j in range(10)] for i in range(10)]
ans = 0
for i in range(n-2):
    fir = int(s[i])
    if judge_first[fir]:
        for j in range(i+1,n-1):
            sec = int(s[j])
            if judge_second[fir][sec]:
                for k in range(j+1,n):
                    thr = int(s[k])
                    if judge[fir][sec][thr]:
                        ans+=1
                        judge[fir][sec][thr] = False
                judge_second[fir][sec] = False
        judge_first[fir] = False
print(ans)