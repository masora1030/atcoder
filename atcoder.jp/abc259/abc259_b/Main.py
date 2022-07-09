sr=lambda: input()
ir=lambda: int(sr())
lr=lambda: list(map(int, sr().split()))

# dr=lambda: float(sr())
# dlr=lambda: list(map(float, sr().split()))
import math

inf=10**18
# mod = 10**9+7
mod=998244353

def main():
    a,b,d = lr()
    d_r = math.radians(d)
    print(a*math.cos(d_r)-b*math.sin(d_r), b*math.cos(d_r)+a*math.sin(d_r))

if __name__ == '__main__':
    main()
