T = int(input())
res = []

for _ in range(T):
    p = int(input())
    if p > 2000:
        p *= (1 - 0.15)
    elif p > 1000:
        p *= (1 - 0.08)
    elif p > 500:
        p *= (1 - 0.05)
    res.append(f'RM {p:.2f}')

for ans in res:
    print(ans)