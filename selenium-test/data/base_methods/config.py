# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os


path = os.path.dirname(__file__)
BASE_URL = "https://modnakasta.ua"
TIMEOUT = 250
envs = ['gitlab-runner', 'project', 'jenkins']
SHOW_DISPLAY = "show_display"

PROD = {SHOW_DISPLAY: 0,
        "db":"""
                dbname=''
                user=''
                password=''
                port=''
            """
        }

LOCAL = {SHOW_DISPLAY:1,
        "db":"""
                host=''
                dbname=''
                user=''
                password=''
                port=''
            """
        }

def current_env():
    for env in envs:
        if env in path:
            return PROD
    return LOCAL