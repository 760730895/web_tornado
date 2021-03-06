#!/usr/bin/env python
# coding=utf-8
"""
the url structure of website
"""

import importlib,sys     #utf-8，兼容汉字
importlib.reload(sys)

from handlers.index import IndexHandler    #假设已经有了
from handlers.user import UserHandler
from handlers.sleep import SleepHandler,SeeHandler

url = [
    (r'/', IndexHandler),
    (r'/user',UserHandler),
    (r'/sleep',SleepHandler),
    (r'/see',SeeHandler)
]
