# coding=utf-8
"""
Create on 2021/3/15 14:49
@desc   : 
@author : wurenxi
@File   : server.py
"""
import os

from bokeh.command.util import build_single_handler_application

from bokeh.server.server import Server as bkServer
from tornado.web import RequestHandler

from .urls import per_app_patterns

class IndexHandler(RequestHandler):
    def get(self):
        self.render("templates/index.html")

class Server:
    def __init__(self, index_path=None):
        application = build_single_handler_application(os.path.join(os.path.dirname(__file__), "app"))
        self.server = bkServer({'/app': application}, num_procs=1, debug=True, extra_patterns=[('/', IndexHandler)])
        self.server.start()

    def start(self):
        """
        启动服务
        Returns:

        """
        print("http://localhost:5006/app")
        self.server.io_loop.start()

