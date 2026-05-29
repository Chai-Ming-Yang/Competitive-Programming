vis = {
    'pa', 'ba', 'da', 'za', 'ga',
    'pi', 'bi', 'ji', 'ji', 'gi',
    'pu', 'bu', 'zu', 'zu', 'gu',
    'pe', 'be', 'de', 'ze', 'ge',
    'po', 'bo', 'do', 'zo', 'go',
    'n',
    'wa', 'wo'
    'ra', 'ri', 'ru', 're', 'ro',
    'ya', 'yu', 'yo',
    'ma', 'mi', 'mu', 'me', 'mo',
    'ha', 'hi', 'fu', 'he', 'ho',
    'na', 'ni', 'nu', 'ne', 'no', 
    'ta', 'chi', 'tsu', 'tw', 'to',
    'sa', 'shi', 'su', 'se', 'so',
    'ka', 'ki', 'ku', 'ke', 'ko',
    'a', 'i', 'u', 'e', 'o'
}

T = int(input())

for _ in range(3):
    a = input().split()
    cnt = 0
    for s in a:
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in vis:
                cnt += 1
                i += 1
            elif s[i] in vis:
                cnt += 1
            i += 1
    print(cnt)