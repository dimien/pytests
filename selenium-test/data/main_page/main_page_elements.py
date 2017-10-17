# !/usr/bin/env python
# -*- coding: utf-8 -*-


LOGO = "//a[@href='/']/img[contains(@src,'https://m.cdnmk.net/')]"
CSC_LINK = "//a[@class='header-top_department']"

CAMPAIGN_BTN = "//a[contains(text(),'Акции')]"
MARKET_BTN = "//span[contains(text(),'Каталог')]"

BLACK_IN_TOP = "//a[@class='header-top_karta']"

HEADER_USER_NAME = "//div[@class='header-top_user']/span"
LOGOUT_LINK = "//a[contains(text(),'Выход')]"

AUTH_LINK = "//div[@class='header-top_login']"
AUTH_FORM = "//form[@class='popup__left-form']/h2"

FB_ICO = "//span[@class='popup__facebook-icon']"
FB_LOGIN_INPUT = "//input[@id='email']"
FB_PASS_INPUT = "//input[@id='pass']"
FB_LOGIN_BTN = "//button[@id='loginbutton']"

CAMPAIGN = "//a[contains(@href,'/campaign/')]"
LOADED_CAMPAIGN_BANNER = "//a[contains(@href,'/campaign/')]//div[@class='pictholder']/img[contains(@src,'jpg')]"
SOON_END_CAMPAIGNS = "//div[@id='last-minutes']/div/div"
COMING_SOON_FIRST_ITEM = "//*[@class='soon-item_name']"