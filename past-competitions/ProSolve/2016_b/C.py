T = int(input())
res= []
for _ in range(T):
    n = int(input())
    ans = 1
    while n:
        ans *= n
        n -= 1
    res.append(f'Case {len(res) + 1}: {ans}')
for ans in res:
    print(ans)