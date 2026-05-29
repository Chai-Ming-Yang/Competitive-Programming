T = int(input())

for _ in range(T):
    s = input().replace(' ', '')
    if (len(s) == 3 and s[0].isnumeric() and s[2].isnumeric()):
        o = s[1]
        if o == '+':
            print(int(s[0]) + int(s[2]))
        elif o == '-':
            print(int(s[0]) - int(s[2]))
        elif o == '*':
            print(int(s[0]) * int(s[2]))
        elif o == '/':
            print(int(s[0]) // int(s[2]))
        else:
            print("INVALID")
    else:
        print("INVALID")