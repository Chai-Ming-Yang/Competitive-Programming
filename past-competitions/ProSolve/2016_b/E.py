from collections import Counter
T = int(input())
res = []

for _ in range(T):
    a, b = input().split()
    if Counter(a) == Counter(b):
        res.append(f'Case {len(res) + 1}: Yes')
    else:
        res.append(f'Case {len(res) + 1}: No')
for ans in res:
    print(ans)