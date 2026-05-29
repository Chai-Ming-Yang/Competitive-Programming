import bisect
n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]

jobs.sort(key=lambda a: a[1])
end = [job[1] for job in jobs]

dp = [0] * n

for i in range(n):
    l, r, p = jobs[i]
    idx = bisect.bisect_right(end, l) - 1

    take = p
    if idx != -1:
        take += dp[idx]
    
    skip = dp[i-1] if i > 0 else 0
        
    dp[i] = max(skip, take)

print(dp[-1])