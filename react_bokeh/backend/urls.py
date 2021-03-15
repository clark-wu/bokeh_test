# coding=utf-8
"""
Create on 2021/3/15 16:05
@desc   : 
@author : wurenxi
@File   : urls
"""
from bokeh.server.urls import per_app_patterns
from .new_doc_handler import NewDocHandler
per_app_patterns.extend([
    (r"/newdoc", NewDocHandler)
])
