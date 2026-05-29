T = int(input())
res = []
for _ in range(T):
    a = sorted(list(map(int, input().split())))
    res.append(f'Case {len(res) + 1}: {a[1]}')
for ans in res:
    print(ans)