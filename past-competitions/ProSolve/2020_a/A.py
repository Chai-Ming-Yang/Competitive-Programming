T = int(input())
oA = ord('A')
res = []
for _ in range(T):
    n = int(input())
    ans = ''
    while n:
        ans += chr(oA + (n % 26) - 1)
        n //= 26
    res.append(ans[::-1])
print('\n'.join(res))