N = int(input())
pts = [tuple(map(int, input().split())) for _ in range(N)]
pts.sort()

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

lower = []

for p in pts:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

upper = []
for p in pts[::-1]:
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)

hull = lower[:-1] + upper[:-1]
hull.sort(key=lambda p: (p[0] + p[1], p[1], p[0]))

for x, y in hull:
    print(x, y)