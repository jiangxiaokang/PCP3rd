import re

num0 = -1234
num1 = +1234
num2 = 1234
''' 1.7 整型 '''
patt = r'[+-]?\d+'
''' 1.8 长整型'''
patt1 = r'[+-]?\d+[L]'
''' 1.9 浮点数'''
patt2 = r'[+-]?\d+.\d+'
''' 1.10 复数'''
1-2j
-2j
2j
patt3 = r'\d*-?\d+j'