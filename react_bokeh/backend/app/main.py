# coding=utf-8
"""
Create on 2021/3/10 17:11
@desc   : 
@author : wurenxi
@File   : main.py
"""
from bokeh.application import Application
from bokeh.core.properties import Bool, Float, Tuple
from bokeh.io import show, curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, InputWidget, Slider, CustomAction
from bokeh.plotting import Figure
from bokeh.server.server import Server
from custom_model.models.ion_range_slider import IonRangeSlider
from custom_model.models.param_tool import ParamTool

x = [x * 0.005 for x in range(2, 198)]
y = x

source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6, color='#ed5565')
plot.add_tools(ParamTool())

callback_single = CustomJS(args=dict(source=source), code="""
            var data = source.data;
            var f = cb_obj.value
            var x = data['x']
            var y = data['y']
            for (var i = 0; i < x.length; i++) {
                y[i] = Math.pow(x[i], f)
            }
            source.change.emit();
        """)

callback_ion = CustomJS(args=dict(source=source), code="""
            var data = source.data;
            var f = cb_obj.range
            var x = data['x']
            var y = data['y']
            var pow = (Math.log(y[100])/Math.log(x[100]))
            console.log(pow)
            var delta = (f[1] - f[0])/x.length
            for (var i = 0; i < x.length; i++) {
                x[i] = delta*i + f[0]
                y[i] = Math.pow(x[i], pow)
            }
            source.change.emit();
        """)

slider = Slider(start=0, end=5, step=0.1, value=1, title="Bokeh Slider - Power")
slider.js_on_change('value', callback_single)

ion_range_slider = IonRangeSlider(start=0.01, end=0.99, step=0.01, range=(min(x), max(x)),
                                  title='Ion Range Slider - Range')
ion_range_slider.js_on_change('range', callback_ion)

layout = column(plot, slider, ion_range_slider)
curdoc().add_root(layout)
