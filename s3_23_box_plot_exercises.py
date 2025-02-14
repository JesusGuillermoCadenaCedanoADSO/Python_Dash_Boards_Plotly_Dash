import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np
#######
# Objective: Make a DataFrame using the Abalone dataset (../data/abalone.csv).
# Take two independent random samples of different sizes from the 'rings' field.
# HINT: np.random.choice(df['rings'],10,replace=False) takes 10 random values
# Use box plots to show that the samples do derive from the same population.
######

# Perform imports here:

df = pd.read_csv('data/abalone.csv')

sample_1 = np.random.choice(df['rings'],10,replace=False)

sample_2 = np.random.choice(df['rings'],10,replace=False)

data = [
    go.Box(
    y=sample_1,
    boxpoints='all', # display the original data points
    jitter=0.3, # spread them out so they all appear
    pointpos=-1.8, # offset them to the left of the box
    name ='sample_1'
    ),
    go.Box(
    y=sample_2,
    boxpoints='all', # display the original data points
    jitter=0.3, # spread them out so they all appear
    pointpos=-1.8,
    name='sample_2' # offset them to the left of the box
    )
]

layout = go.Layout(title='2 random samples')
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig, filename='box1.html')

# create a DataFrame from the .csv file:


# take two random samples of different sizes:



# create a data variable with two Box plots:











# add a layout




# create a fig from data & layout, and plot the fig