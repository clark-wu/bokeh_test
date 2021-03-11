# coding=utf-8
"""
Create on 2021/3/11 10:00
@desc   : 
@author : wurenxi
@File   : s1.py
"""
import panel as pn
from bokeh.io import curdoc

pn.extension()
row = pn.Row(
    pn.pane.Markdown('ABCDE', background='#f0f0f0', width=200, height=200),
    pn.pane.PNG('https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png', width=200),
    pn.widgets.FloatSlider(width=200))

pn.serve(row)