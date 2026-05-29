MOD = 10**9 + 7
pr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
a = eval(input())
cnt = [0] * 31
for i in a: cnt[i] += 1

msk = {}    # diff valid masks

for x in range(2, 31):
    y = x; m = 0; ok = 1
    
    for i, p in enumerate(pr):
        c = 0
        while y % p == 0:
            y //= p
            c += 1
        if c > 1: ok = 0; break
        if c: m |= (1 << i)

    if ok: msk[x] = m

dp = [0] * (1 << 10)    # track 10 bits    10 primes (<=30)
dp[0] = 1   # state init

for x in range(2, 31):
    if cnt[x] == 0 or x not in msk:
        continue
    m = msk[x]
    for s in range((1<<10)-1, -1, -1):
        if s & m: continue

        dp[s|m] = (dp[s|m] + dp[s] * cnt[x]) % MOD

ans = (sum(dp) - 1) % MOD
ans = ans * pow(2, cnt[1], MOD)
print(ans)