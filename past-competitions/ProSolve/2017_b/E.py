freq = {}
S = input().split()
for s in S:
    freq[s] = freq.get(s, 0) + 1

T = int(input())
for _ in range(T):
    print(freq.get(input(), 0))