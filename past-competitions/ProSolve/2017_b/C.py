T = int(input())
res = []
for _ in range(T):
    a = input().split()
    res.append(' '.join(a[::-1]))
for ans in res:
    print(ans)