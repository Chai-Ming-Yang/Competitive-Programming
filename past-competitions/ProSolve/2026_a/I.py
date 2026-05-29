import math
n = int(input())
MM = 1
TT = 0

for _ in range(n):
    p, o = map(int, input().split())

    GCD = math.gcd(MM, p)
    diff = (o - TT) % p
    if diff % GCD != 0:
        print("NO"); exit()
    
    # TT + k*MM = o (mod p)
    inv = pow(MM//GCD, -1, p//GCD)

    k = (diff//GCD * inv) % (p//GCD)
    TT = TT + k*MM
    MM *= (p//GCD)

print("YES", TT % (10**9+7))
