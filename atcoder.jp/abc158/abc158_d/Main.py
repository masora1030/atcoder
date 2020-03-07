# D
from collections import deque
s = deque(str(input()))
q_count = int(input())
rev = False
for i in range(q_count):
    q = list(input().split())
    if q[0] == '1':
        rev = not(rev)
    else:
        if q[1] == '1':
            if rev:
                # 末尾にq[2]追加
                s.append(q[2])
            else:
                # 先頭にq[2]追加
                s.appendleft(q[2])
        else:
            if rev:
                # 先頭にq[2]追加
                s.appendleft(q[2])
            else:
                # 末尾にq[2]追加
                s.append(q[2])
if rev:
    s.reverse()
print(*s, sep='')