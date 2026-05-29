s = eval(input())

L = len(s)
res = 0
left = right = ''

for i in range(L):
    left += s[i]
    right = s[L-i-1] + right
    if left == right:
        left = right = ''
        res += 1

print(res)