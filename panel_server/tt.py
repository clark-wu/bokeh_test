# coding=utf-8
"""
Create on 2021/3/10 16:08
@desc   : 
@author : wurenxi
@File   : tt.py
"""
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Slider, CustomJS
from bokeh.plotting import figure
from bokeh.sampledata.sea_surface_temperature import sea_surface_temperature

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