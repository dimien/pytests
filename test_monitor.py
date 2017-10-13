# -*- coding: utf-8 -*-

import urllib2
import unittest
import json
import datetime
import random
import re
from multiprocessing.dummy import Pool as ThreadPool


BASE_URL = "https://staging.modnakasta.ua"
CAMPAIGNS_API_URL = "/api/v2/campaigns"
PRODUCT_API_URL = "/api/v2/product/?"
PRODUCT_LIST_API_URL = "/api/v2/product-list"
IMG_URL = "https://m.cdnmk.net/imgw/loc/1x1/"

PRODUCT_URL = BASE_URL + "/product/4254712:671/?campaign=s-43262-ezhednevnyj-uhod"
PRODUCT_WIHOUT_CAMPAIGN_URL = BASE_URL + "/product/340938:671/"
CAMPAIGN_URL = BASE_URL + "/campaign/s-43273-colin-s/"
MARKET_URL = BASE_URL + "/market/tovary-dlya-kuhni/"

MAIN_URLS = [BASE_URL, CAMPAIGN_URL, PRODUCT_URL, MARKET_URL, PRODUCT_WIHOUT_CAMPAIGN_URL]


def read_url(url):
    res = urllib2.urlopen(url)
    try:
        assert(res.getcode() == 200)
    except:
        raise Exception, "%s returns %s" % (url ,res.getcode())
    return res

def get_campaigns():
    url = BASE_URL + CAMPAIGNS_API_URL
    res = read_url(url)
    r = json.loads(res.read())
    return r

def get_current_campaigns_ids():
    now = datetime.datetime.now()
    campaigns = get_campaigns()
    ids = []

    for c in campaigns["items"]:
        starts_at = datetime.datetime.strptime(c["starts_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
        finishes_at = datetime.datetime.strptime(c["finishes_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
        if starts_at < now and finishes_at > now and c["code_name"] != "black":
            ids.append(c["id"])
    return ids

def get_product_lst_by_campaign_id(campaign_id):
    url = BASE_URL + PRODUCT_LIST_API_URL + '/%s' % campaign_id
    res = read_url(url)
    r = json.loads(res.read())
    return r

def create_product_lst():
    ids = get_current_campaigns_ids()
    ids = random.sample(ids, 2)
    product_lst = []
    for campaign_id in ids:
        products = get_product_lst_by_campaign_id(str(campaign_id))
        product_lst.extend(products.values()[0][:50])
    return product_lst

def get_products_img_lst():
    lst = create_product_lst()
    img_lst = []
    url = BASE_URL + PRODUCT_API_URL
    for p in lst:
        pp_id = re.search("\d*", p).group(0)
        url += "pp-id=%s&" % pp_id

    res = read_url(url)
    r = json.loads(res.read())

    for product in r["items"]:
        img_lst.extend(product["images"])
    return img_lst

def get_img(img):
    url = IMG_URL + str(img)
    res = read_url(url)

def get_main_urls(url):
    res = read_url(url)


class TestMonitor(unittest.TestCase):
    def test_threads(self):
        img_lst = get_products_img_lst()

        # check photos availability
        pool1 = ThreadPool(100)
        pool1.map(get_img, img_lst)
        pool1.close()
        pool1.join()

        # check main urls availability
        pool2 = ThreadPool(100)
        pool2.map(read_url, MAIN_URLS)
        pool2.close()
        pool2.join()

        print 'MK is alive.'
if __name__ == '__main__':
    unittest.main()