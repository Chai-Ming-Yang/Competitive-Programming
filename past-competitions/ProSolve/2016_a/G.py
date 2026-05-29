T = int(input())
res = []

for _ in range(T):
    n = int(input())
    g = [[1] * n for _ in range(n)]
    for r in range(n):
        g[r][r] = 0
        g[r][n-r-1] = 0
    res.append(g)

for ans in res:
    for row in ans:
        print(' '.join(map(str, row)))
    print()