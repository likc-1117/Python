#coding:utf-8

'''def calc_prod(lst):
    def product():
        def sy(x,y):
            return x*y
        return reduce(sy,lst)
    return product
f = calc_prod([1, 2, 3, 4])
print f()

def format_name(s):
    return s.capitalize()

print map(format_name, ['adam', 'LISA', 'barT'])

import math

def add(x, y, f):
    return f(x) + f(y)

print add(25, 9, math.sqrt)

def prod(x, y):
    return x*y

print reduce(prod, [2, 4, 5, 7, 12])

def cmp_ignore_case(s1, s2):
    if s1.lower()>s2.lower():
        return 1
    if s1.lower()<s2.lower():
        return -1
    return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)

def is_sqr(x):
    return math.sqrt(x).is_integer()

print filter(is_sqr, range(1, 101))

def count():
    fs = []
    for i in range(1, 4):
        def f(i=i):
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()'''
import re
b = 'absl-py                0.7.1       0.9.0      sdist'
a = 'google-auth-oauthlib   0.4.1      0.4.3     wheel'
re_result = re.findall(r'[^\s]+', b, re.I)
print(re_result)