T = int(input())
res = []
for _ in range(T):
    a = input()
    b = input()
    i, j = len(a)-1, len(b)-1
    carry = 0
    ans = []
    while i>=0 or j>=0 or carry:
        total = ((int(a[i]) if i>=0 else 0) + 
                (int(b[j]) if j>=0 else 0) + 
                carry)
        ans.append(total % 10)
        carry = total // 10
        i -= 1; j -= 1
    res.append(''.join(map(str, ans))[::-1])

for ans in res:
    print(ans)