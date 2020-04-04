n,k = map(int, input().split())
kouho1 = n%k
kouho2 = abs(kouho1-k)
print(min(kouho1, kouho2))