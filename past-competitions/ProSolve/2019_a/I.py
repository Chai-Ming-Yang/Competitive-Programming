T = int(input())

res = []
for _ in range(T):
    x, y = map(int, input().split())
    mn = min(x, y)

    ans = 0
    for i in range(mn):
        ans += (x - i) * (y - i)

    res.append(f'Number of squares are {ans}')

print('\n'.join(res))