# -*- coding: utf-8 -*-
# @author: yangyd
# @file: strong_password.py
# @time: 2020/5/25 21:53

import re


def strong_pwd(pwd: str):
    count = 0
    if len(pwd) < 8:
        return False
    if re.search(r'[a-z]+', pwd) :
        count += 1
    if re.search(r'[A-Z]+', pwd):
        count += 1
    if re.search(r'[0-9]+', pwd):
        count += 1
    if count == 3:
        return True
    return False


a = 'dad123as'
b = '1231asAS'

print(strong_pwd(a), strong_pwd(b))
