import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mocksurvey.csv', index_col=0)

x_values = df.index


data = []
for col in range(len(df.columns)):
    if col:
        trace = go.Bar(x=x_values,y=df[df.columns[col]],name=df.columns[col])
        data.append(trace)

layout = go.Layout(title='Questions',barmode='stack')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)
