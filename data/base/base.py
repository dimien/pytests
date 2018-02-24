# -*- coding: utf-8 -*-

import re
from time import sleep
import random
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from . import config as c


class BaseClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=c.CHROMEDRIVER)
        self.driver.set_window_size(c.WEIGHT, c.HEIGHT)

    def quit(self):
        self.driver.quit()

    def open_url(self, url, element):
        self.driver.get(url)
        self.wait_element(element)

    def get_current_url(self):
        return self.driver.current_url

    def close(self):
        self.driver.close()

    def find(self, item):
        try:
            element = self.driver.find_element_by_xpath(item)
            return element
        except:
            raise Exception('%s not found at ' % item + self.get_current_url())

    def get_text(self, item):
        element_text = self.find(item).text
        return element_text

    def get_attr(self, element, attr):
        value = self.find(element).get_attribute(attr)
        return value

    def compare_values(self, value_first, value_second):
        assert value_second in value_first

    def find_text(self, item, txt):
        elem = self.find(item).text
        if u'%s' % txt in elem:
            return True
        else:
            raise Exception('URL is: ' + self.get_current_url() + ' .Text %s not in %s' % (txt.encode('utf-8'), elem.encode('utf-8')))

    def get_elements(self, items):
        try:
            elements = self.driver.find_elements_by_xpath(items)
            return elements
        except:
            raise Exception('URL is: ' + self.get_current_url())

    def find_list_elements(self, items):
        try:
            for i in items:
                self.find(i)
        except:
            raise Exception('URL is: ' + self.get_current_url())

    def clear(self, item):
        self.find(item).clear()

    def click(self, item):
        self.find(item).click()

    def js_click(self, item):
        r = re.findall("(\@)(\w+)", item)
        element = r[-1][-1]

        r = re.findall("(\=')(\w+)", item)
        attribute = r[-1][-1]

        if "id" in element:
            print(attribute)
            self.execute("document.getElementById('{}').click()".format(attribute))
        elif "class" in element:
            print(attribute)
            self.execute("document.getElementsByClassName('{}').click()".format(attribute))
        else:
            r = re.findall("(\//)(\w+)", item)
            element = r[-1][-1]
            print(element)
            self.execute("document.getElementsByTagName('{}').click()".format(element))


    def send_keys(self, item, data):
        self.find(item).send_keys(data)

    def refresh(self):
        self.driver.refresh()

    def execute(self, script, *args):
        self.driver.execute_script(script, args)

    def back(self):
        self.driver.execute_script("window.history.go(-1)")

    def count_elements(self, element):
        elements = self.driver.find_elements_by_xpath(element)
        return len(elements)

    def hover(self, element):
        action = ActionChains(self.driver)
        el = self.find(element)
        action.move_to_element(el)
        action.perform()

    def switch_to_frame(self, frame):
        inbox = self.find(frame)
        self.driver.switch_to.frame(inbox)

    def switch_to_window(self):
        """switch to next (right) window tab"""
        window = self.driver.window_handles[-1]
        self.driver.switch_to.window(window)

    def get_rand_item_text(self, items_text):
        rand_text = random.choice(items_text)
        return rand_text

    def accept_alert(self):
        """click ok at js alerts"""
        alert = self.driver.switch_to_alert()
        alert.accept()

    def scroll_vertically(self, pixel_count):
        self.execute("window.scrollBy(0, {});".format(pixel_count))