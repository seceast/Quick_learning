# -*- coding: utf-8 -*-
# @author: yangyd
# @file: strong_password.py
# @time: 2020/5/25 21:53

import re


def strong_pwd(pwd: str):
    if len(pwd) < 8:
        return False
    if