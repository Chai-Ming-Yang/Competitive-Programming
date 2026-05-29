S = list(map(lambda a: chr(int(a[2:], 16)), input().split()))
S = ''.join(S[:-1])

print(S)