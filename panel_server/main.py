# coding=utf-8
"""
Create on 2021/3/10 16:02
@desc   : 
@author : wurenxi
@File   : main.py
"""

from bokeh.command.util import build_single_handler_application

from bokeh.util.serialization import make_id

from bokeh.embed.elements import script_for_render_items

from bokeh.embed.wrappers import wrap_in_script_tag

from bokeh.embed.util import RenderItem
from jinja2 import Environment, FileSystemLoader
from tornado.web import RequestHandler

from bokeh.application import Application
from bokeh.embed import server_document
from bokeh.embed.bundle import bundle_for_objs_and_resources
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider, CustomJS
from bokeh.plotting import figure
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature
from bokeh.server.server import Server
from bokeh.themes import Theme
import panel.io.server


def bkapp(doc):

    def handle_comm_message(message):
        print(message)
        print(doc)

    doc.on_comm_req = handle_comm_message
    df = sea_surface_temperature.copy()
    source = ColumnDataSource(data=df)

    plot = figure(x_axis_type='datetime', y_range=(0, 25), y_axis_label='Temperature (Celsius)',
                  title="Sea Surface Temperature at 43.18, -70.43")
    plot.line('time', 'temperature', source=source)

    def callback(attr, old, new):
        if new == 0:
            data = df
        else:
            data = df.rolling(f"{new}D").mean()
        source.data = ColumnDataSource.from_df(data)

    slider = Slider(start=0, end=30, value=0, step=1, title="Smoothing by N Days")
    #slider.on_change('value', callback)
    callback2 = CustomJS(code="console.log('wurenxi callback test')")
    slider.js_on_change('value', callback2)

    doc.add_root(column(slider, plot))


# Setting num_procs here means we can't touch the IOLoop before now, we must
# let Server handle that. If you need to explicitly handle IOLoops then you
# will need to use the lower level BaseServer class.
# The `static/` end point is reserved for Bokeh resources, as specified in
# bokeh.server.urls. In order to make your own end point for static resources,
# add the following to the `extra_patterns` argument, replacing `DIR` with the desired directory.
# (r'/DIR/(.*)', StaticFileHandler, {'path': os.path.normpath(os.path.dirname(__file__) + '/DIR')})

print(Application)
from bokeh.application.handlers.function import FunctionHandler
application = Application(FunctionHandler(bkapp))
server = Server({'/bkapp': application},
                num_procs=1)
server.start()

if __name__ == '__main__':
    from bokeh.util.browser import view

    print('Opening Tornado app with embedded Bokeh application on http://localhost:5006/')

    server.io_loop.add_callback(view, "http://localhost:5006/")
    server.io_loop.start()
