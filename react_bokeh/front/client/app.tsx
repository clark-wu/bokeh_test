import React from 'react'
import * as Bokeh from "@bokeh/bokehjs"
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            token:"",
            use_for_title: "",
            bundle: {}
        };
    }

    componentDidMount() {
        axios.get(`/app/newdoc`).then(res => {
            console.log(res.data)
            this.setState(res.data)
            console.log(Bokeh.embed.embed_items)
            // let render_item = res.data
            // render_item = Object.assign(res.data,{"root_ids":["1044"],"roots":{"1044":"testPlot"}})
            // let docs_json = {}
            // Bokeh.embed.embed_items(docs_json, [render_item])
        });
    }

    render() {
        return (
            <div className="App" style={{ margin: 20 }}>
                Hello World
                <div id='testPlot' className="bk-root" data-root-id="1044"></div>
            </div>
        );
    }
}

export default App;
