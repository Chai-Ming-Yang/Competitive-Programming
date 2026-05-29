T = int(input())
res = []

for _ in range(T):
    a = list(map(int, input().split()))
    total = sum(a)
    res.append([total, total//10])

for ans in res:
    print(ans[0], ans[1])