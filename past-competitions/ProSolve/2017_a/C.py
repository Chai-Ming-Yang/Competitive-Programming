T = int(input())
res = []
for _ in range(T):
    P, Q = map(int, input().split())
    pre, cur = 1, 1
    for _ in range(P-2):
        pre, cur = cur, (pre + cur) % Q
    res.append(f'Case #{len(res) + 1}: {cur}')
for ans in res:
    print(ans)