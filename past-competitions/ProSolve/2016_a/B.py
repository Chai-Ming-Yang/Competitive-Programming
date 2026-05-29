T = int(input())

for _ in range(T):
    a = input()
    b = input()
    
    i, j = len(a)-1, len(b) - 1
    carry = 0
    ans = []

    while i >= 0 or j >= 0 or carry:
        x = int(a[i]) if i >= 0 else 0
        y = int(b[j]) if j >= 0 else 0
        
        total = x + y + carry
        carry = total // 10
        ans.append(str(total % 10))
        i -= 1
        j -= 1
    print(''.join(ans[::-1]))