a = sorted(eval(input()), key=len)
dp = {}
res = 1
for w in a:
    dp[w] = dp.get(w, 1)
    for i in range(len(w)):
        pre = w[:i] + w[i+1:]
        if pre not in dp: continue
        dp[w] = max(dp[w], dp[pre] + 1)
    res = max(res, dp[w])
print(res)
