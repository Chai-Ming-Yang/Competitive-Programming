T = int(input())

res = []
for _ in range(T):
    s = input().split()

    low = ' '.join(map(str.lower, s))
    up = ' '.join(map(str.upper, s))
    cap1 = ' '.join([s[0].capitalize()] + s[1:])
    tog = ' '.join(
        ''.join(c.upper() if c.islower() else c.lower() for c in word)
        for word in s
    )
    cap = ' '.join(
        word[0].upper() + word[1:] for word in s
    )

    res.append([low, up, cap1, tog, cap])

for ans in res:
    print('\n'.join(ans))