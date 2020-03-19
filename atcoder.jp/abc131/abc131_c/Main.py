# C
a,b,c,d = map(int,input().split())

import fractions

f=fractions.gcd(c,d)           #最大公約数
f2=c*d//f                          #最小公倍数

# a未満でcかdで割れるかず
a-=1
x = a//c
y = a//d
z = a//f2
ac = x+y-z

# b以下でcかdで割れるかず
x = b//c
y = b//d
z = b//f2
bc = x+y-z

print(b-a-(bc-ac))