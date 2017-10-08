# -*- coding: utf-8 -*-

import urllib2
import unittest
import json
import datetime
import random
import re
from multiprocessing import Process
import threading
import Queue
import timeout_decorator

class TestMonitor(unittest.TestCase):
    def read_url(self, url):
        data = urllib2.urlopen(url)
        return data

    def get_campaigns(self):
        url = BASE_URL + CAMPAIGNS_URL
        res = self.read_url(url)
        r = json.loads(res.read())
        try:
            assert(res.getcode() == 200)
        except:
            raise Exception, "%s returns %s" % (res.read(), res.getcode())
        return r

    def get_current_campaigns_ids(self):
        now = datetime.datetime.now()
        campaigns = self.get_campaigns()
        ids = []

        for c in campaigns["items"]:
            starts_at = datetime.datetime.strptime(c["starts_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
            finishes_at = datetime.datetime.strptime(c["finishes_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
            if starts_at < now and finishes_at > now and c["code_name"] != "black":
                ids.append(c["id"])
        return ids

    def get_product_lst_by_campaign_id(self, campaign_id):
        url = BASE_URL + PRODUCT_LIST_URL + '/%s' % campaign_id
        try:
            res = self.read_url(url)
        except:
            raise Exception, "%s returns %s" (url, res.getcode())
        r = json.loads(res.read())
        return r

    def create_product_lst(self):
        ids = self.get_current_campaigns_ids()
        ids = random.sample(ids, 2)
        product_lst = []
        for campaign_id in ids:
            products = self.get_product_lst_by_campaign_id(str(campaign_id))
            product_lst.extend(products.values()[0][:50])
        return product_lst

    def create_products_img_lst(self):
        lst = self.create_product_lst()
        url = BASE_URL + PRODUCT_URL
        img_lst = []
        for p in lst:
            pp_id = re.search("\d*", p).group(0)
            url += "pp-id=%s&" % pp_id

        res = self.read_url(url)
        r = json.loads(res.read())

        for product in r["items"]:
            img_lst.extend(product["images"])
        try:
            assert(res.getcode() == 200)
        except:
            raise Exception, "%s returns %s" % (res.read(), res.getcode())
        return img_lst

    @timeout_decorator.timeout(20)
    def test_availability_imgs(self):
        img_lst = self.create_products_img_lst()
        for img in img_lst:
            url = IMG_URL + img
            res = self.read_url(url)
            try:
                assert(res.getcode() == 200)
            except:
                raise Exception, "%s returns %s" % (url ,res.getcode())


if __name__ == '__main__':
    unittest.main()