# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 10:55
# @Author  : Seceast
# @File    : isPhoneNumber.py


# 不使用正则表达式判断号码

def is_phone_number(text: str):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


phone1 = '400-800-8820'
phone2 = 'sdada'
print(is_phone_number(phone1))
print(is_phone_number(phone2))

