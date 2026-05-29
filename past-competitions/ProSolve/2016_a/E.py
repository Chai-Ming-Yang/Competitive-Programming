T = int(input())
res = []
for _ in range(T):
    inp = list(map(int, input().split()))
    nStd = inp[0]
    cost = sum(inp[1:])
    if (nStd <= 20 and cost <= 2000 or
        nStd <= 50 and cost <= 4000 or
        nStd > 50 and cost <= 10000):
        res.append("APPROVED")
    else:
        res.append("DENIED")
for ans in res:
    print(ans)