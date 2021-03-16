# coding=utf-8
"""
Create on 2021/3/16 14:35
@desc   : 事件类
@author : wurenxi
@File   : events
"""
from bokeh.events import ModelEvent


class MoveUpEvent(ModelEvent):
    ''' Announce a button click event on a Bokeh button widget.

    '''
    event_name = 'move_up'

    def __init__(self, model):
        from bokeh.models import Plot
        if model is not None and not isinstance(model, Plot):
            raise ValueError(f"{self.__class__.__name__} event only applies to Plot models")
        super(MoveUpEvent, self).__init__(model)
