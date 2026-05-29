T = int(input())

res = []
for _ in range(T):
    a = sorted(list(map(int, input().split())))
    res.append(str(a[4]*a[0] + a[0]*a[2] + a[2]*a[1] + a[1]*a[3]))
print('\n'.join(res))
