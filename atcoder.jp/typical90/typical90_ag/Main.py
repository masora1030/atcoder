a,b=map(int, input().split())
if a==1 or b==1:
  print(max(a,b))
else:
  a=(a+1)//2
  b=(b+1)//2
  print(a*b)