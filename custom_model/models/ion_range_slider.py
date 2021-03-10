from bokeh.core.properties import Bool, Float, Tuple
from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, InputWidget, Slider
from bokeh.plotting import Figure

class IonRangeSlider(InputWidget):
    # The special class attribute ``__implementation__`` should contain a string
    # of JavaScript or TypeScript code that implements the web browser
    # side of the custom extension model or a string name of a file with the implementation.

    __javascript__ = [
        "https://code.jquery.com/jquery-3.1.1.min.js",
        "https://cdnjs.cloudflare.com/ajax/libs/ion-rangeslider/2.1.4/js/ion.rangeSlider.js",
    ]
    __css__ = [
        "https://cdnjs.cloudflare.com/ajax/libs/normalize/4.2.0/normalize.css",
        "https://cdnjs.cloudflare.com/ajax/libs/ion-rangeslider/2.1.4/css/ion.rangeSlider.css",
        "https://cdnjs.cloudflare.com/ajax/libs/ion-rangeslider/2.1.4/css/ion.rangeSlider.skinFlat.min.css",
    ]

    # Below are all the "properties" for this model. Bokeh properties are
    # class attributes that define the fields (and their types) that can be
    # communicated automatically between Python and the browser. Properties
    # also support type validation. More information about properties in
    # can be found here:
    #
    #    https://docs.bokeh.org/en/latest/docs/reference/core/properties.html#bokeh-core-properties

    disable = Bool(default=True, help="""
    Enable or disable the slider.
    """)

    grid = Bool(default=True, help="""
    Show or hide the grid beneath the slider.
    """)

    start = Float(default=0, help="""
    The minimum allowable value.
    """)

    end = Float(default=1, help="""
    The maximum allowable value.
    """)

    range = Tuple(Float, Float, help="""
    The start and end values for the range.
    """)

    step = Float(default=0.1, help="""
    The step between consecutive values.
    """)