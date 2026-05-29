T = int(input())
res = []

for _ in range(T):
    s = input()
    alp = num = 0
    for c in s:
        if c.isalpha():
            alp += 1
        elif c.isnumeric():
            num += 1
    res.append(f'Alphabet: {alp}, Digit: {num}')
    
for ans in res: 
    print(ans)