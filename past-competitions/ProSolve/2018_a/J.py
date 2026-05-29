N = int(input())
M = int(input())
coins = sorted(list(map(int, input().split())), reverse=True)

dp = [float('inf')] * (N+1)
dp[0] = 0
for coin in coins:
    for i in range(N+1-coin):
        if dp[i] != float('inf'):
            dp[i+coin] = min(dp[i+coin], dp[i] + 1)

print(dp[N])