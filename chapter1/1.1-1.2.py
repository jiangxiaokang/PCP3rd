import re

""" 1-1 bat/bit/but/hat/hit/hut"""
str='bit'
m = re.match(r'[bh][aiu]t',str)
print(m.group())
""" 1-2 """
str="Jack Ma"
m = re.match(r'[\w]+ [\w]+',str)
print(m.group())

str="Jack 3321"
m = re.match(r'[A-Za-z]+ [A-Za-z]+',str)
if m is not None:print(m.group())
else: print('not match')

""" 1-3 """
str='Isaac Newton'
str1="Jack M"
str2="Zhang,Fei"
str3='Li,B'
def test_1_3(str):
    m = re.findall('\w+',str,re.I)
    print(m)

test_1_3(str)
test_1_3(str1)
test_1_3(str2)
test_1_3(str3)