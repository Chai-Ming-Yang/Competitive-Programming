T = int(input())
res = []

for _ in range(T):
    N = int(input())
    g = []
    for spacing in range((N-1)//2, -1, -1):
        line = ''
        for width in range(N, 2, -2):
            if spacing * 2 > width:
                break
            line += ' ' * spacing
            line += '*' * (width - 2*spacing)
            line += ' ' * spacing
        g.append(line)

    res.append(g)

for i, ans in enumerate(res):
    for row in ans:
        print(row)
    if i == T-1: break
    print()