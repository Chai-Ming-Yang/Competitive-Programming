T = int(input())

for _ in range(T):
    S = input()
    A, B, C = S[0] + S[2], S[:2], S[1:]
    D, E, F = A[::-1], B[::-1], C[::-1]

    if (int(S) == sum(map(int, [A, B, C, D, E, F]))):
        print(S + ' is an Osiris number')
    else:
        print(S + ' is not an Osiris number')
