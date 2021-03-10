# coding=utf-8
"""
Create on 2021/3/4 14:38
@desc   : 
@author : wurenxi
@File   : main.py
"""

from tornado.web import RequestHandler
from bokeh.settings import settings
import os
import sys

from bokeh.server.server import Server
from bokeh.command.util import build_single_handler_application

import logging.config
logging.config.fileConfig("logger.conf")
logger = logging.getLogger()


settings.allowed_ws_origin = '*'
app = build_single_handler_application(os.path.join(os.path.dirname(__file__), "app"))

num_procs = 1 if sys.platform == "win32" else 4
server = Server({'/app': app}, num_procs=num_procs, port=8080)
server.start()

if __name__ == '__main__':
    from bokeh.util.browser import view

    print('Opening Tornado app with embedded Bokeh application on http://localhost:8080/app')

    server.io_loop.add_callback(view, "http://localhost:8080/app")
    server.io_loop.start()



