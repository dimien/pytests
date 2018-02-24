# -*- coding: utf-8 -*-

import sys, os

# ROOT_DIR = os.path.dirname(__file__) # get current directory (..\pytests\selenium_test)
# sys.path.append(os.path.join(ROOT_DIR, 'data'))

from time import sleep
import unittest

from data.base.base import BaseClass
from data.base.wait import Wait

import data.search.search_elements as se


class TestSearch(BaseClass, Wait):

    def testSearch(self):
        self.open_url(se.BASE_URL, se.INPUT)
        self.send_keys(se.INPUT, u"шоссейный велосипед")
        self.click(se.BTN)
        sleep(1)
        self.click(se.CLOSE_BTN)
        sleep(1)
        self.scroll_vertically(500)
        sleep(1)
        self.click(se.ITEM)
        sleep(1)
        

if __name__ == "__main__":
    print('running')
    unittest.main()