T = int(input())
res = []
for _ in range(T):
    s = input()
    vowel = consonant = 0
    for c in s:
        if c in 'aeiouAEIOU':
            vowel += 1
        else:
            consonant += 1
    res.append(f'Case {len(res) + 1}: {vowel} {consonant}')
for ans in res:
    print(ans)