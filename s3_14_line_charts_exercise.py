import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# #
# objective: using the file 2010YumaAZ.csv, develop a Line Chart
# that plots seven days worth of temperature data on one graph.
# You can use a for loop to assing each day to its own trace.

# Perform imports here:


# Create a pandas DataFrame from 2010YumaAZ.csv
df = pd.read_csv('data/2010YumaAZ.csv')
days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']
print(days[0])

x_values = df[df['DAY']==days[0]]['LST_TIME']


# Use a for loop (or list comprehension to create traces for the data list)

# using list comprehension

# data = [{
#     'x':df['LST_TIME'],
#     'y':df[df['DAY']==day]['T_HR_AVG'],
#     'name':day
# } for day in df['DAY'].unique()]

data = []

for day in days:
    # What should go inside this Scatter call?
    y_values = df[df['DAY']==day]['T_HR_AVG']
    trace = go.Scatter(x=x_values,y=y_values,mode='lines',name=day)
    data.append(trace)

# Define the layout

layout = go.Layout( title='Line charts',
                    xaxis={'title':'TIME'},
                    yaxis=dict(title='TEMP_AVG'))

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig)