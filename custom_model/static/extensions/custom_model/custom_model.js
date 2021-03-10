/*!
 * Copyright (c) 2012 - 2021, Anaconda, Inc., and Bokeh Contributors
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 * 
 * Redistributions of source code must retain the above copyright notice,
 * this list of conditions and the following disclaimer.
 * 
 * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 * 
 * Neither the name of Anaconda nor the names of any contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
 * THE POSSIBILITY OF SUCH DAMAGE.
 */
(function(root, factory) {
  factory(root["Bokeh"], undefined);
})(this, function(Bokeh, version) {
  var define;
  return (function(modules, entry, aliases, externals) {
    const bokeh = typeof Bokeh !== "undefined" && (version != null ? Bokeh[version] : Bokeh);
    if (bokeh != null) {
      return bokeh.register_plugin(modules, entry, aliases);
    } else {
      throw new Error("Cannot find Bokeh " + version + ". You have to load it prior to loading plugins.");
    }
  })
({
"cb5e15b45d": /* index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    const tslib_1 = require("tslib");
    const custom_model = tslib_1.__importStar(require("50a1a36d23") /* ./models */);
    exports.custom_model = custom_model;
    const base_1 = require("@bokehjs/base");
    base_1.register_models(custom_model);
},
"50a1a36d23": /* models\index.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    var extensions_ion_range_slider_1 = require("146854bee1") /* ./extensions_ion_range_slider */;
    __esExport("IonRangeSlider", extensions_ion_range_slider_1.IonRangeSlider);
},
"146854bee1": /* models\extensions_ion_range_slider.js */ function _(require, module, exports, __esModule, __esExport) {
    __esModule();
    // HTML construction and manipulation functions
    const dom_1 = require("@bokehjs/core/dom");
    // We will subclass in JavaScript from the same class that was subclassed
    // from in Python
    const input_widget_1 = require("@bokehjs/models/widgets/input_widget");
    // This model will actually need to render things, so we must provide
    // view. The LayoutDOM model has a view already, so we will start with that
    class IonRangeSliderView extends input_widget_1.InputWidgetView {
        render() {
            // BokehJS Views create <div> elements by default, accessible as @el.
            // Many Bokeh views ignore this default <div>, and instead do things
            // like draw to the HTML canvas. In this case though, we change the
            // contents of the <div>, based on the current slider value.
            super.render();
            if (this.model.title != null) {
                this.value_el = dom_1.input({ type: "text", class: "bk-input", readonly: true, style: { marginBottom: "5px" } });
                this.group_el.appendChild(this.value_el);
            }
            this.input_el = dom_1.input({ type: "text" });
            this.group_el.appendChild(dom_1.div({ style: { width: "100%" } }, this.input_el));
            // Set up parameters
            const max = this.model.end;
            const min = this.model.start;
            const [from, to] = this.model.range || [max, min];
            const opts = {
                type: "double",
                grid: this.model.grid,
                min,
                max,
                from,
                to,
                step: this.model.step || (max - min) / 50,
                disable: this.model.disabled,
                onChange: (data) => this.slide(data),
                onFinish: (data) => this.slidestop(data),
            };
            jQuery(this.input_el).ionRangeSlider(opts);
            if (this.value_el != null)
                this.value_el.value = `${from} - ${to}`;
        }
        slidestop(_data) {
        }
        slide({ from, to }) {
            if (this.value_el != null)
                this.value_el.value = `${from} - ${to}`;
            this.model.range = [from, to];
        }
    }
    exports.IonRangeSliderView = IonRangeSliderView;
    IonRangeSliderView.__name__ = "IonRangeSliderView";
    class IonRangeSlider extends input_widget_1.InputWidget {
        constructor(attrs) {
            super(attrs);
        }
        static init_IonRangeSlider() {
            // If there is an associated view, this is boilerplate.
            this.prototype.default_view = IonRangeSliderView;
            // The @define block adds corresponding "properties" to the JS model. These
            // should basically line up 1-1 with the Python model class. Most property
            // types have counterparts, e.g. bokeh.core.properties.String will be
            // String in the JS implementation. Where the JS type system is not yet
            // as rich, you can use p.Any as a "wildcard" property type.
            this.define(({ Boolean, Number, Tuple }) => ({
                range: [Tuple(Number, Number)],
                start: [Number, 0],
                end: [Number, 1],
                step: [Number, 0.1],
                grid: [Boolean, true],
            }));
        }
    }
    exports.IonRangeSlider = IonRangeSlider;
    IonRangeSlider.__name__ = "IonRangeSlider";
    IonRangeSlider.init_IonRangeSlider();
},
}, "cb5e15b45d", {"index":"cb5e15b45d","models/index":"50a1a36d23","models/extensions_ion_range_slider":"146854bee1"}, {});});
//# sourceMappingURL=custom_model.js.map
