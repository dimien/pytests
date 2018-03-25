from selenium import webdriver
from main_page import main_page_elements as mpe
from time import sleep

class MainPage():
    def open_main_page(self):
        # self.driver.get(mpe.PAGE)
        # sleep(1)
        # self.driver.find_element_by_xpath(mpe.SEARCH_FIELD)
        self.open_url(mpe.PAGE, mpe.SEARCH_FIELD)

    def search(self, text):
        # self.driver.find_element_by_xpath(mpe.SEARCH_FIELD).send_keys(mpe.TEXT)    
        # self.driver.find_element_by_xpath(mpe.SEARCH_BTN).click()
        # self.driver.find_element_by_xpath(mpe.AD)
        self.send_keys(mpe.SEARCH_FIELD, text)
        self.click(mpe.SEARCH_BTN)
        self.find(mpe.AD)

    def close_tip(self):
        # self.driver.find_element_by_xpath(mpe.CLOSE_BTN).click()
        self.click(mpe.CLOSE_BTN)
        sleep(1)

    def open_first_ad(self):
        # self.driver.find_element_by_xpath(mpe.AD).click()
        self.click(mpe.AD)
        sleep(1)