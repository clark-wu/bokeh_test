# coding=utf-8
"""
Create on 2021/3/15 16:05
@desc   : 
@author : wurenxi
@File   : urls
"""
import os

from bokeh.server.urls import per_app_patterns,toplevel_patterns
from tornado.web import StaticFileHandler

from .new_doc_handler import NewDocHandler
per_app_patterns.extend([
    (r"/newdoc", NewDocHandler)
])

toplevel_patterns.extend([
    (r"/dist/(.*)", StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "dist")))
])
