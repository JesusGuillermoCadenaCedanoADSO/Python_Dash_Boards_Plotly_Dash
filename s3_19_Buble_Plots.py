import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')

data = [go.Scatter( # start with a normal scatter plot
x=df['horsepower'],
y=df['mpg'],
text=df['name'],
mode='markers',
marker=dict(size=1*df['weight']/100,color=df['cylinders'],showscale=True) # set the marker size
)]
layout = go.Layout(
title='Vehicle mpg vs. horsepower',
xaxis = dict(title = 'horsepower'), # x-axis label
yaxis = dict(title = 'mpg'), # y-axis label
hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')
