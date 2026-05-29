import math
T = int(input())
res = []
for _ in range(T):
    m, n, a = map(int, input().split())
    row = math.ceil(m / float(a))
    col = math.ceil(n / float(a))
    res.append(f'Case {len(res) + 1}: {row * col}')
for ans in res:
    print(ans)