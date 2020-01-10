import math
n = int(input())
count_p = 1
count_q = 1
p_list = [i+1 for i in range(n)]
q_list = [i+1 for i in range(n)]
p = list(map(int, input().split()))
q = list(map(int, input().split()))
for i in range(n):
    count_p += p_list.index(p[i])*math.factorial(n-i-1)
    p_list.remove(p[i])
    count_q += q_list.index(q[i])*math.factorial(n-i-1)
    q_list.remove(q[i])
print(abs(count_p-count_q))