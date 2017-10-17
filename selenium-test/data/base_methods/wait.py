# !/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class Wait():
    def __init__(self):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def wait_element(self, element):
        try:
            self.wait.until(lambda self: self.find_element_by_xpath(element))
            return True
        except:
            raise TimeoutException, 'URL is: ' + self.get_current_url() + ' .Screenshot location is: data.screenshots', self.get_screenshot()

    def wait_and_check(self, element):
        for i in xrange(60):
            i += 1
            print 'wait and check ', i
            try:
                self.wait_element(element)
                print 'wait_and_check: found'
                break
            except:
                # self.driver.refresh()
                self.driver.execute_script("location.reload()")
                continue