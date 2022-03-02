import re
'''1.11 匹配任意邮箱'''
patt=r'\w+[\w\d\.]*@\w+.\.com'
''' 1.12 匹配url'''
patt=r'http[s]?://wwww\.(?:\w+\.)+[(com)|(org)|(net)|(edu)]'

''' 1.13 提取类型'''
'''<type 'builtin_function_or_method'>'''
s = "<type 'builtin_function_or_method'>"
patt=r"<\w+\s'(\w+)'>"
m=re.search(patt,s)
if m is not None:print(m.groups())

''' 1.14 匹配剩余日期'''
patt=r'1[0-2]'