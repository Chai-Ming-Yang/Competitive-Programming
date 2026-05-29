T = int(input())
res = []
for _ in range(T):
    n = int(input())
    m = int()
    for i in range(1, 10):
        m = int(str(n)[::-1])
        if m == n:
            res.append(f'{str(n)};Palindrome;{i}')
            break
        n += m
    else:
        res.append(f'{str(n)};None')
        
for ans in res:
    print(ans)