T = int(input())
for _ in range(T):
    a, op, b = input().split()
    a, b = float(a), float(b)
    if op == '+': print(f'{a+b:.2f}')
    if op == '-': print(f'{a-b:.2f}')
    if op == '*': print(f'{a*b:.2f}')
    if op == '/': print(f'{a/b:.2f}')
