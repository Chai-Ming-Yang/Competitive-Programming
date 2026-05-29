T = int(input())
res = []

for _ in range(T):
    o, a, b = input().split()
    a, b = int(a, 3), int(b, 3)

    if o == '+':    ans = a + b
    elif o == '-':  ans = a - b
    elif o == '*':  ans = a * b
    elif o == '/':
        if not b: res.append('NAN'); continue
        ans = a // b

    base3 = []
    while ans:
        base3.append(str(ans % 3))
        ans //= 3
    
    res.append(''.join(base3[::-1]))

print('\n'.join(res))