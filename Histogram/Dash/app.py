import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

app = dash.Dash(__name__)

marks_dict = {i: '{}'.format(i) for i in range(1,100+1, 10)}
marks_dict[100] = "100"

app.layout = html.Div([
    html.Div([
        html.H2(children="Graph a standard normal distribution")
    ]),
    html.Div([
        html.H4(children="Slides this to increase/decrease the number of values" ),
        dcc.Slider(
        id='myslider',
        min=1,
        max=100,
        value=30,
        marks = marks_dict)
    ], style={'width': '50%'}),

    html.Div([
        dcc.Graph(id="myhisto")
        ], style={'width': '50%', 'float': 'right'})
]) 



@app.callback(
    Output('myhisto', 'figure'),
    [Input('myslider', 'value')])
def update_figure(slider_value):
    vals = np.random.default_rng().standard_normal(slider_value)
    fig = px.histogram(vals, nbins=30)
    fig.update_layout(transition_duration=500)

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)


