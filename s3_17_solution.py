import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mocksurvey.csv', index_col=0)

x_values = df.index

# create traces using a list comprehension
#vertical bars
#data = [go.Bar(x=df.index,y=df[response],name=response) for response in df.columns]
#horizontal bars
data = [go.Bar(x=df[response],y=df.index,orientation='h',name=response) for response in df.columns]

layout = go.Layout(title='Survey Results',barmode='stack')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)