a = list(map(int, input().split()))
diff = int(input())

vis = set()
res = []
for n in a:
    if n - diff in vis:
        res.append((n-diff, n))
    vis.add(n)

if not res:
    print('No Pair Found')
    exit()

print(f'Pair Found: {', '.join(map(str,res))}')