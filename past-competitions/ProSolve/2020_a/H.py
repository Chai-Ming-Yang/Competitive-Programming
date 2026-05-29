T = int(input())
res = []
for _ in range(T):
    b2 = int(input(), 2)
    res.append(f'{oct(b2)[2:]} {b2} {hex(b2)[2:].upper()} {chr(b2)}')
print('\n'.join(res))