n=int(input())
m=n*2
print(m)
num4=n//4
ret=n%4
x_list=['4' for _ in range(num4)]
if ret > 0:
  x_list.append(str(ret))
x=''.join(reversed(x_list))
print(x)