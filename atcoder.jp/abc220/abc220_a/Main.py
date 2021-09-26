import sys
A, B, C=(int(x) for x in input().split())
ans=C
while ans<=B:
    if ans>=A and ans<=B:
        print(ans)
        sys.exit()
    ans+=C
print(-1)