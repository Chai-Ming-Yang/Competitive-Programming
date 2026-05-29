T = int(input())

memo = { -1:0, 0:1 }
def dp(n, zero=False):
    if n in memo: return memo[n]
    memo[n] = dp(n-1) + dp(n-2)
    return memo[n]

for _ in range(T):
    n = int(input())
    
    print(dp(n) + dp(n-1))