import re
T = int(input())

res = []
for _ in range(T):
    words = input().split()
    ans = []
    apply_exclamation = False
    for word in words:
        if apply_exclamation:
            i = len(word)
            while i > 0 and not word[i-1].isalpha():
                i -= 1
            word = word[:i] + '!' + word[i:]
            apply_exclamation = False

        if re.sub(r'[^\w]', '', word) == 'Hello':
            start_idx = word.find('Hello')
            word = word[:start_idx] + 'olleH' + word[start_idx+5:]
            apply_exclamation = True

        ans.append(word)

    res.append(' '.join(ans))
print('\n'.join(res))