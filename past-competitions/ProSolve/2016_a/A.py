T = int(input())
res = []

for _ in range(T):
    tmp = []
    s = input().split()[:-1]
    for w in s:
        tmp.append('*' * len(w))
    res.append(tmp)

for lis in res[:-1]:
    for ans in lis:
        print(ans)
    print()
for ans in res[-1]:
    print(ans)