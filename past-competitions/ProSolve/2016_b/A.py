import math
T = int(input())
res = []

for _ in range(T):
    x, y = map(int, input().split())
    res.append(f'{x**2 + math.sqrt(y):.2f}')

i = 0
for ans in res:
    i += 1
    print(f'Case {i}: {ans}')