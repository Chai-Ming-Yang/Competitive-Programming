T = int(input())
res = []

for _ in range(T):
    n = int(input())
    if n % 4:
        res.append(f'Case {len(res) + 1}: No')
    elif n % 100:
        res.append(f'Case {len(res) + 1}: Yes')
    elif n % 400:
        res.append(f'Case {len(res) + 1}: No')
    else:
        res.append(f'Case {len(res) + 1}: Yes')
for ans in res:
    print(ans)