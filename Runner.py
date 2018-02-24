# -*- coding: utf-8 -*-

import sys, os
import unittest
from testSearch import TestSearch

def my_suite():
    suite = unittest.TestSuite() # create suite instance

    suite.addTest(unittest.makeSuite(TestSearch)) # copy this at the next line & add new test into makeSuite()

    runner = unittest.TextTestRunner() # create runner instance
    print(runner.run(suite)) # print is shown statistic: <unittest.runner.TextTestResult run=1 errors=0 failures=0>


my_suite()