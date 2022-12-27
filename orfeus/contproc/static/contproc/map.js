function set_up_ui() {
    if (Object.keys(plotly_map).length > 0){
        let gid = document.getElementById("map");
        Plotly.newPlot(gid, plotly_map['data'], plotly_map['layout'], plotly_map['config']);
    }
}

document.addEventListener("DOMContentLoaded", set_up_ui);

