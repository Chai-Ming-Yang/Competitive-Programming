T = int(input())
res = []
for _ in range(T):
    x, y = map(int, input().split())
    ans = (x*(x-1))//2 * (y*(y-1))//2
    res.append(str(ans))
print('\n'.join(res))