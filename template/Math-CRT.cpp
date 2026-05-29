import math
MM, TT = 1, 0
for strt, freq in a:
  GCD = math.gcd(MM, freq)
  diff = (strt - TT) % freq
  if diff % GCD != 0:
    print('NO'); exit()

  # TT + k*MM = strt (mod freq)
  inv = pow(MM//GCD, -1, freq//GCD)

  k = (diff//GCD * inv) % (freq//GCD)
  TT += k*MM
  MM *= (freq // GCD)

print('YES', TT)
