# -*- coding: utf-8 -*-
'''
Created on 2017-08-02 12:25
---------
@summary:
---------
@author: Boris
'''


import web
from service import *
import config
import sys

def start_server():
    web.config.debug = config.DEBUG
    sys.argv.append('0.0.0.0:%s' % config.API_PORT)
    app = web.application(config.URLS, globals())
    app.run()


if __name__ == "__main__":
    start_server()