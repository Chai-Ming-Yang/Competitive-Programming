res = ''
s = eval(input())
n = len(s)

for i in range(1, n):
    if s[:i] == s[n-i:]:
        res = s[:i]
print(res)