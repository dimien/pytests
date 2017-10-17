# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


path = os.path.dirname(os.path.realpath(__file__))
emails = {'user_name':'email'}
users = emails.keys()
for i in users:
    if i in path:
        USER_EMAIL = emails.get(i)
        break
    else:
        USER_EMAIL = emails.get('default')
        continue

USER_NAME = u"мктест"
SOC_PASS = "qwe123qwe123"
FB_LOGIN = "+380684757394"

HEADER_USER_NAME = "//div[@class='header-top_user']/span"