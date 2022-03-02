import re

patt = r'www\..*\.(?:(com)|(edu)|(net))'
s0 = 'www://www.yahoo.com/'
s1 = 'http://www.foothill.edu'

def print_match(m):
    if m is not None:print(m.group())
    eles : print("not match")

print_match(re.search(patt,s0))

print_match(re.search(patt,s1))