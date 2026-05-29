T = int(input())

res = []
for i in range(1, T+1):
    n = int(input())

    cur, num_zero = 1, 0
    for j in range(1, n+1):
        cur *= j
        while cur % 10 == 0:
            cur //= 10
            num_zero += 1
    res.append(f'Case {i}: {num_zero}')

print('\n'.join(res))