# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 11:13
# @Author  : Seceast
# @File    : reg_number.py


import re

num_red = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = num_red.search('My number is 415-555-4242.')

print(mo.group())
