# !/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import data.main_page.main_page_elements as mpe
import cabinet_elements as me


class Cabinet:
    def fb_login(self, user_name):
        self.click(mpe.FB_ICO)
        self.wait_element(mpe.HEADER_USER_NAME)
        self.find_text(mpe.HEADER_USER_NAME, user_name)

    def fb_full_login(self, user_name):
        """when login at first"""
        self.click(mpe.FB_ICO)
        sleep(2)
        self.send_keys(mpe.FB_LOGIN_INPUT, me.FB_LOGIN)
        self.send_keys(mpe.FB_PASS_INPUT, me.SOC_PASS)
        self.click(mpe.FB_LOGIN_BTN)
        sleep(2)
        self.find(mpe.HEADER_USER_NAME)
        if self.get_text(mpe.HEADER_USER_NAME) in me.USER_NAME:
            return True
        else:
            raise Exception, "User name is not match!"

    def logout(self):
        if self.get_text(mpe.HEADER_USER_NAME) in me.USER_NAME:
            pass
        else:
            raise Exception, "User name is not match!"
        self.click(mpe.HEADER_USER_NAME)
        self.wait_element(mpe.LOGOUT_LINK)
        self.click(mpe.LOGOUT_LINK)
        self.wait_element(mpe.AUTH_LINK)