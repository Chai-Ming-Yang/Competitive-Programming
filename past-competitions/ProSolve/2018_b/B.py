N, Q = map(int, input().split())
a = []
for _ in range(N):
    a.append(tuple(map(int, input().split())))
a.sort()

def bs(t):
    lo, hi = 0, len(a)-1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if a[mid][0] <= t:
            lo = mid
        else:
            hi = mid - 1
    return lo, a[lo][0] <= t

res = []
for _ in range(Q):
    last, found = bs(int(input()))
    if not a:
        res.append('-1 -1 -1')
        continue

    if not found:
        res.append(f'-1 -1 {a[0][0]}')
        continue

    else:
        res.append(f'{a[last][1]} {a[last][0]} {a[last+1][0] if last+1 < len(a) else -1}')

for ans in res:
    print(ans)