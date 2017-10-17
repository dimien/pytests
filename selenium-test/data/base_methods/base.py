# !/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import random
import unittest
from datetime import datetime, timedelta
from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

import config as conf


class BaseClass(unittest.TestCase):
    def setUp(self):
        env = conf.current_env()
        self.display = Display(visible=env.get('show_display'), size=(1360, 768))
        self.display.start()
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-setuid-sandbox")
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', chrome_options=chrome_options)
        self.driver.set_window_size(1366, 768)
        self.wait = WebDriverWait(self.driver, 5)

    def tearDown(self):
        self.driver.quit()
        self.display.stop()

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
            raise Exception, '%s not found at ' % item + self.get_current_url(), self.get_screenshot()

    def get_screenshot(self):
        timestamp = format(datetime.now() + timedelta(hours=2), '%Y-%m-%d %H:%M:%S')
        self.driver.save_screenshot('./data./screenshots/' + self.get_class_name() + '_' + timestamp + '.png')

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
            raise Exception, 'URL is: ' + self.get_current_url() + ' .Text %s not in %s' % (txt.encode('utf-8'), elem.encode('utf-8')), self.get_screenshot()

    def get_elements(self, items):
        try:
            elements = self.driver.find_elements_by_xpath(items)
            return elements
        except:
            raise Exception, 'URL is: ' + self.get_current_url() + ' .Screenshot location ./data./screenshots/', self.get_screenshot()

    def find_list_elements(self, items):
        try:
            for i in items:
                self.find(i)
        except:
            raise Exception, 'URL is: ' + self.get_current_url() + ' .Screenshot location ./data./screenshots/', self.get_screenshot()

    def clear(self, item):
        self.find(item).clear()

    def click(self, item):
        self.find(item).click()

    def send_keys(self, item, data):
        self.find(item).send_keys(data)

    def refresh(self):
        self.driver.refresh()

    def back(self):
        self.driver.execute_script("window.history.go(-1)")

    def count_elements(self, element):
        elements = self.driver.find_elements_by_xpath(element)
        return len(elements)

    def switch_onoff_js(self):
        self.open_url("about:config")
        action = ActionChains(self.driver)
        action.send_keys(Keys.ENTER)
        self.wait_element(mpe.TEXTBOX)
        self.send_keys(Keys.TAB)
        action.send_keys("javascript.enabled")
        sleep(2)
        self.send_keys(Keys.TAB)
        self.send_keys(Keys.ENTER)
        self.refresh()
        self.wait_element(mpe.TEXTBOX)

    def hover(self, element):
        action = ActionChains(self.driver)
        el = self.find(element)
        action.move_to_element(el)
        action.perform()

    def switch_to_frame(self, frame):
        inbox = self.find(frame)
        self.driver.switch_to.frame(inbox)

    def switch_to_window(self):
        window = self.driver.window_handles[-1]
        self.driver.switch_to.window(window)

    def get_rand_item_text(self, items_text):
        rand_text = random.choice(items_text)
        return rand_text

    def accept_alert(self):
        alert = self.driver.switch_to_alert()
        alert.accept()