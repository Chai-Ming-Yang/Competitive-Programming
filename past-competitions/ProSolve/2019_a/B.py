DIM = 4
g = [list(map(int, input().split())) for _ in range(DIM)]
O = int(input())

def merge(a):
    a = [n for n in a if n]
    res = []
    i = 0
    while i < len(a):
        if i+1 < len(a) and a[i] == a[i+1]:
            res.append(a[i] * 2)
            i += 2
        else:
            res.append(a[i])
            i += 1

    return res + [0] * (DIM - len(res))

if O == 0:    # left
    for r in range(DIM):
        g[r] = merge(g[r])

if O == 1:    # up
    for c in range(DIM):
        col = [g[r][c] for r in range(DIM)]
        col = merge(col)

        for r in range(DIM):
            g[r][c] = col[r]

if O == 2:    # right
    for r in range(DIM):
        g[r] = merge(g[r][::-1])[::-1]

if O == 3:    # down
    for c in range(DIM):
        col = [g[r][c] for r in range(DIM)]
        col = merge(col[::-1])[::-1]
        
        for r in range(DIM):
            g[r][c] = col[r]

for row in g:
    print(*row)