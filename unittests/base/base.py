from time import sleep
import unittest
from selenium import webdriver
from . import config as c

class BaseClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=c.CHROMEDRIVER)

    def open_url(self, url, element):
        self.driver.get(url)
        sleep(1)
        self.find(element)

    def find(self, item):
        try:
            element = self.driver.find_element_by_xpath(item)
            return element
        except:
            raise Exception('%s not found at ' % item + self.get_current_url())

    def find_text(self, item, txt):
        elem = self.find(item).text
        if u'%s' % txt in elem:
            return True
        else:
            raise Exception('URL is: ' + self.get_current_url() + ' .Text %s not in %s' % (txt.encode('utf-8'), elem.encode('utf-8')))        
     
    def click(self, item):
        self.find(item).click()

    def send_keys(self, item, data):
        self.find(item).send_keys(data)