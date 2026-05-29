import math
n = int(input())
circle = []
mnX = mnY = float('inf')
mxX = mxY = float('-inf')

for _ in range(n):
    x, y, r = map(float, input().split())
    mnX, mnY = min(mnX, x-r), min(mnY, y-r)
    mxX, mxY = max(mxX, x+r), max(mxY, y+r)
    circle.append((x, y, r))

EPS = 0.5
res = (-1, -1, -1)
for k in range(math.floor(mnY), math.ceil(mxY) + 1):
    for h in range(math.floor(mnX), math.ceil(mxX) + 1):
        cnt = 0
        for x, y, r in circle:
            nr = math.sqrt( (x-h)**2 + (y-k)**2 )
            if abs(r - nr) <= EPS:
                cnt += 1
        if cnt > res[0]:
            res = (cnt, h, k)

print(*res[1:])