import re

s0 = '1180 Bordeaux Drive'
s1 = '3120 De la Cruz Boulevard'

patt = '\d+\s(?:[a-zA-Z]+\s?)+'

def print_match(m):
    if m is not None:print(m.group())
    eles : print("not match")

print_match(re.match(patt,s0))

print_match(re.match(patt,s1))