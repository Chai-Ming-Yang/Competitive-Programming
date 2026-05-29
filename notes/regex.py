import re
        # not
r'\d'   r'\D'   # digit
r'\w'   r'\W'   # word
r'\s'   r'\S'   # space
''      r'.'    # anyChar
r'[a-zA-Z0-9]'  # group anyChar
r'[^a-zA-Z0-9]' # inverse 
r'(dog|cat)'    # exact match

r'.'      #  1  anyChar
r'.*'     # 0-n anyChar
r'.+'     # 1-n anyChar
r'.?'     # 0/1 anyChar
r'.?*'    # min anyChar
r'.{1,8}' # 1-8 anyChar

r'^a'     # start with 'a'
r'a$'     #  end  with 'a'
r'^a$'    # fullmatch

re.findall(r'', s)  # list (match)
re.search (r'', s)  # 1st  (match)
re.sub(r'', '', s)  # replace r'' with ''
re.split(r'', s)    # variable space split

re.search(r'^[a-zA-Z][a-zA-Z0-9]*@[a-z]+\.[a-zA-Z]+$', email)
re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])'+
        r'(?=.*[!@#$%^&*()_+-=`~])' +
        r'[a-zA-Z0-9!@#$%^&*()_+-=`~]{8,}$', paswd)
