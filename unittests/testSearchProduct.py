import unittest
from base.base import BaseClass
from main_page.main_page import MainPage

from ad_page import ad_page_elements as ad

class TestProductInfo(BaseClass, MainPage):

    def testProductInfo(self):
        TEXT = u"шоссейный велосипед"
        TITLE_TEXT = u"оссейн"

        self.open_main_page()
        self.search(TEXT)
        self.close_tip()
        self.open_first_ad()

        self.find_text(ad.TITLE, TITLE_TEXT)
               

if __name__ == "__main__":
    unittest.main()