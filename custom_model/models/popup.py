# coding=utf-8
"""
Create on 2021/3/11 16:28
@desc   : 
@author : wurenxi
@File   : popup.py.py
"""
from bokeh.core.properties import Color, Float, List, Override, String
from bokeh.models import Callback


class Popup(Callback):
    """
    弹出框Model
    """
    message = String("", help="""
    Message to display in a popup window. This can be a template string,
    which will be formatted with data from the data source.
    """)
