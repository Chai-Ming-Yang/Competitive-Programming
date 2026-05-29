from collections import Counter
S = input()
freq = Counter(S)

for k, v in sorted(freq.items(), key=lambda a: a[0]):
    print(f'{k}:{v}')