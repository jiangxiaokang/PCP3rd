import re

""" 1.4 python有效的标识符
    _或者字母开头,\w 数字，字母，下划线
"""
patt = r'[_a-zA-Z]\w*'
_ = "_a"
m = re.match(patt,_)
if m is not None:print(m.group())
else: print("not match")

_adfaf_ = '_adfaf_'
m = re.match(patt,_adfaf_)
if m is not None:print(m.group())
else: print("not match")

dfa1234 = 'adf1234'
m = re.match(patt,dfa1234)
if m is not None:print(m.group())
else: print("not match")