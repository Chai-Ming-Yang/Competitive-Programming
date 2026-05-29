shift = int(input())
s = input()
ordA = ord('A')
res = ''
for c in s:
    if c == ' ':
        res += ' '; continue
    ascii_c = ord(c) - ordA
    shifted = (ascii_c + shift) % 26
    res += chr(shifted + ordA)
print(res)