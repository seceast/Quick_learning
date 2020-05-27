# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 15:09
# @Author  : Seceast
# @File    : phone_email.py


import pyperclip,re

phone_reg = re.compile(r'1\d{10}')
email_reg = re.compile(r'[a-zA-Z0-9]*@qq\.com')

match_str = '我的电话是19999999998，邮箱是1928jjjjaas@qq.com'

phone = phone_reg.search(match_str).group()
email = email_reg.search(match_str).group()
print(phone, email)
