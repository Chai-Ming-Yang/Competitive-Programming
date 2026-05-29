import math
from collections import Counter
freq = Counter(eval(input()))
a = eval(input())

GCD = a[0]
for i in range(1, len(a)):
    GCD = math.gcd(GCD, a[i])

res = 0
for k in sorted(freq.keys()):
    if GCD % k == 0: 
        print(res); exit()
    res += freq[k]
print(-1)