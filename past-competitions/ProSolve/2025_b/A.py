import re
s = eval(input())
t = eval(input()) 

def dp(s, t):
    if len(t) < 2: return t==s

    if s[0] != t[0] and t[0].isalpha(): return False
    
    if t[1] != '*': return dp(s[1:], t[1:])

    i = 0
    while i < len(s) and (s[i] == t[0] or t[0]=='.'):
        if dp(s[i+1:], t[2:]): return True
        i += 1

    return False

print(str(dp(s, t)).lower())