nums = sorted([(v, i) for i, v in enumerate(eval(input()))])
MAX = nums[-1][0]
n = len(nums)

spf = list(range(MAX+1))
for i in range(2, MAX+1):
    if spf[i] != i: continue
    for j in range(i*i, MAX+1, i):
        if spf[j] == j: spf[j] = i

def get_primes(num):
    res = set()
    while num > 1:
        res.add(spf[num])
        num //= spf[num]
    return res

par = list(range(n))
def find(a):
    if a != par[a]:
        par[a] = find(par[a])
    return par[a]
def same(a, b): return find(a) == find(b)
def union(a, b):
    a, b = find(a), find(b)
    if a != b: par[a] = b

pf_to_idx = {}
for v, i in nums:
    factors = get_primes(v)
    for p in factors:
        if p in pf_to_idx:
            union(i, pf_to_idx[p])
        else:
            pf_to_idx[p] = i

for u, (_, v) in enumerate(nums):
    if not same(u, v): print('false'); exit()
print('true')
