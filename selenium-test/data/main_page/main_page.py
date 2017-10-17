# !/usr/bin/env python
# -*- coding: utf-8 -*-

from data.base_methods.base import BaseClass
import main_page_elements as mpe
import data.base_methods.config as conf


class MainPage():
    def open_main_page(self):
        self.open_url(conf.BASE_URL, mpe.CAMPAIGN)
        self.check_main_page_elements()

    def open_auth_form(self):
        self.click(mpe.AUTH_LINK)
        self.wait_element(mpe.AUTH_FORM)

    def check_main_page_elements(self):
        lst = [mpe.LOGO,
                mpe.BLACK_IN_TOP,
                mpe.CSC_LINK,
                mpe.CAMPAIGN_BTN,
                mpe.MARKET_BTN,
                mpe.LOADED_CAMPAIGN_BANNER,
                mpe.SOON_END_CAMPAIGNS,
                mpe.COMING_SOON_FIRST_ITEM,
            ]
        self.find_list_elements(lst)