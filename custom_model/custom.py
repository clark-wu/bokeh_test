"""Example implementation of two double ended sliders as extension widgets"""
import os

from bokeh.command.util import build_single_handler_application

from bokeh.server.server import Server

application = build_single_handler_application(os.path.join(os.path.dirname(__file__), "bkapp"))
server = Server({'/bkapp': application}, num_procs=1,debug=True)
server.start()

if __name__ == '__main__':
    from bokeh.util.browser import view

    print('Opening Tornado app with embedded Bokeh application on http://localhost:5006/bkapp')

    #server.io_loop.add_callback(view, "http://localhost:5006/bkapp")
    server.io_loop.start()
