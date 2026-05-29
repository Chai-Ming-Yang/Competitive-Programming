MOD = 10**9 + 7

a = eval(input())
s = int(input())
t = int(input())
fuel = int(input())
N = len(a)

dp = [[0] * N for _ in range(fuel+1)]
dp[fuel][s] = 1

for f in range(fuel, -1, -1):
    for u in range(N):
        if not dp[f][u]: continue

        for v in range(N):
            if v == u: continue
            df = abs(a[u] - a[v])

            if f - df < 0: continue
            dp[f - df][v] = (dp[f - df][v] + dp[f][u]) % MOD

print(sum([dp[i][t] for i in range(fuel+1)]))