import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd
#######
# Objective: build a dashboard that imports OldFaithful.csv
# from the data directory, and displays a scatterplot.
# The field names are:
# 'D' = date of recordings in month (in August),
# 'X' = duration of the current eruption in minutes (to nearest 0.1 minute),
# 'Y' = waiting time until the next eruption in minutes (to nearest minute).
######
# title: Old Faithful Eruption Intervals v Durations
# x title: Duration of eruption (minutes)
# y title: Interval to next eruption (minutes)

# Perform imports here:


app = dash.Dash()

df = pd.read_csv('data/OldFaithful.csv')

duration_eruption = df['X']
waiting_eruption = df['Y']

app.layout = html.Div([
    dcc.Graph(
        id='old_faithful',
        figure={
            'data': [
                go.Scatter(
                    x = duration_eruption,
                    y = waiting_eruption,
                    mode = 'markers',
                    marker = {
                    'size': 6,
                    'color': 'rgb(51,204,153)'
                    }
                )
            ],
            'layout': go.Layout(
                title = 'Old Faithful Eruption Intervals v Durations',
                xaxis = {'title': 'Duration of eruption (minutes)'},
                yaxis = {'title': 'Interval to next eruption (minutes)'},
                hovermode='closest'
            )
        }
    )
])
if __name__ == '__main__':
    app.run_server()





# Launch the application:


# Create a DataFrame from the .csv file:


# Create a Dash layout that contains a Graph component:





















# Add the server clause: