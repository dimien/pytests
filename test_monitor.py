# -*- coding: utf-8 -*-

import urllib2
import unittest
import json
import datetime
import random
import re
from multiprocessing import Process


def read_url(url):
    data = urllib2.urlopen(url)
    return data

def get_campaigns():
    url = BASE_URL + CAMPAIGNS_URL
    res = read_url(url)
    r = json.loads(res.read())
    try:
        assert(res.getcode() == 200)
    except:
        raise Exception, "%s returns %s" % (res.read(), res.getcode())
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
    url = BASE_URL + PRODUCT_LIST_URL + '/%s' % campaign_id
    try:
        res = read_url(url)
    except:
        raise Exception, "%s returns %s" (url, res.getcode())
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
    url = BASE_URL + PRODUCT_URL
    for p in lst:
        pp_id = re.search("\d*", p).group(0)
        url += "pp-id=%s&" % pp_id

    res = read_url(url)
    r = json.loads(res.read())

    for product in r["items"]:
        img_lst.extend(product["images"])
    try:
        assert(res.getcode() == 200)
    except:
        raise Exception, "%s returns %s" % (res.read(), res.getcode())
    return img_lst

def get_img(img):
    url = IMG_URL + str(img)
    res = read_url(url)
    try:
        assert(res.getcode() == 200)
    except:
        raise Exception, "%s returns %s" % (url ,res.getcode())

class TestMonitor(unittest.TestCase):
    def test_threads(self):
        NUMBER_OF_PROCESSES = 2
        p = Process()
        img_lst = get_products_img_lst()
        for n in xrange(NUMBER_OF_PROCESSES):
            for img in img_lst:
                p = Process(target=get_img, args=(img, ))
        p.start()
        p.join()
        print 'Done!'

if __name__ == '__main__':
    unittest.main()