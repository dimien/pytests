# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os


ROOT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(ROOT_DIR, 'data'))

import timeout_decorator
import unittest

from data.base_methods.base import BaseClass
from data.base_methods.wait import Wait
from data.main_page.main_page import MainPage
from data.cabinet.cabinet import Cabinet

import data.cabinet.cabinet_elements as me
import data.base_methods.config as config

class TestAuthFacebook(BaseClass, MainPage, Wait, Cabinet):

    @timeout_decorator.timeout(config.TIMEOUT)
    def testAuthFacebook(self):
        self.open_main_page()
        self.open_auth_form()
        self.fb_full_login(me.USER_NAME)
        self.logout()
        self.open_auth_form()
        self.fb_login(me.USER_NAME)
        self.logout()

if __name__ == "__main__":
    print 'running'
    unittest.main()