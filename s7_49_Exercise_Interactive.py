#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd



# Launch the application:

app = dash.Dash()

# Create a Dash layout that contains input components

app.layout = html.Div([
    dcc.RangeSlider(
        id='my-id',
        min=-5,
        max=10,
        step=0.5,
        marks={i: i for i in range(-5,11)},
        value=[0,6]
        ),
    html.Div(id='my-div',style={'border':'2px blue solid'})
])

# and at least one output. Assign IDs to each component:

@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'result "{}"'.format(input_value[0]*input_value[1])

if __name__ == '__main__':
    app.run_server()









# Create a Dash callback:






# Add the server clause: