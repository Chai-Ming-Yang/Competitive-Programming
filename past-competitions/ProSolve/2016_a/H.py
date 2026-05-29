T = int(input())
res = []

for _ in range(T):
    s = input()
    if len(s) <= 10:
        res.append(s)
    else:
        res.append(s[0] + str(len(s) - 2) + s[-1])
for ans in res:
    print(ans)