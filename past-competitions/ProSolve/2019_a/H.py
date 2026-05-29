import math
from collections import deque
N = int(input())

isP = [True] * (N + 1)
isP[:2] = [False, False]
P = deque()

for i in range(2, N+1):
    if not isP: continue
    for j in range(i*2, N+1, i):
        isP[j] = False
    P.append(i)

res = []
while N != 1:
    prime = P.popleft()
    while N % prime == 0:
        N //= prime
        res.append(str(prime))
print(' x '.join(res))