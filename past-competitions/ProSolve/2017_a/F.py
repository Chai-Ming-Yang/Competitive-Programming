from collections import Counter

n = int(input())
a = list(map(int, input().split()))
freq = Counter(a)


Q = int(input())
Q = list(map(int, input().split()))
for q in Q:
    print(f'{q} = {freq[q]}')