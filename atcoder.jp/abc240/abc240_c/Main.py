n,x = map(int,input().split())
visited = set()
visited.add(0)
for _ in range(n):
  next_set = set()
  a,b = map(int, input().split())
  for num in visited:
    if a+num <= x:
      next_set.add(a+num)
    if b+num <= x:
      next_set.add(b+num)
    visited = next_set
if x in visited:
  print("Yes")
else:
  print("No")