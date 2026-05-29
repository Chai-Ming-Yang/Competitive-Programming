T = int(input())
res = 0

cur = int(input())
grad = 0

for _ in range(T-1):
    nex = int(input())

    if nex > cur:
        if grad == -1:
            res += 1
        grad = 1
    elif nex == cur:
        grad = cur
    else:
        if grad == 1:
            res += 1
        grad = -1

    cur = nex

print(f'Local Exima : {res}')