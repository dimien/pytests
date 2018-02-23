# -*- coding: utf-8 -*-

from time import sleep


class Wait():

    def wait_element(self, element):
        try:
            sleep(2)
            self.find(element)
            return True
        except:
            raise ElementIsNotFound('{1} on {2}'.format(element, self.get_current_url()))