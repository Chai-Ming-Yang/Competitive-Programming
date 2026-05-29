T = int(input())
res = []
for _ in range(T):
    s = input().split('(')[1:]
    s = ''.join(s).split(')')[:-1]
    s = map(len, ''.join(s).split('_'))

    res.append(str(max(s)))
print('\n'.join(res))