import re

""" 1-1 bat/bit/but/hat/hit/hut"""
str='bit'
m = re.match(r'[b|h][a|i|u]t',str)
print(m.group())
""" 1-2 """
str="Jack Ma"
m = re.match(r'[\w]+ [\w]+',str)
print(m.group())

str="Jack"
m = re.match(r'[\w]+ [\w]+',str)
if m is not None:print(m.group())
else: print('not match')