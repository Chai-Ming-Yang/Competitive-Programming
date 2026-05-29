N = int(input())
L = int(input())
g = [[0] * (N+1) for _ in range(N+1)]

res = []
for _ in range(L):
    A = input().split()
    if A[0] == 'F':
        r1, c1, r2, c2, cost = map(int, A[1:])
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                g[r][c] += cost
    else:
        r, c = map(int, A[1:])
        res.append(str(g[r][c]))
print('\n'.join(res))