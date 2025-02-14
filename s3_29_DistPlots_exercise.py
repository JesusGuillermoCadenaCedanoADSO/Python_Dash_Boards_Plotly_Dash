#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: '../data/iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Perform imports here:
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd



# create a DataFrame from the .csv file:

df = pd.read_csv('data/iris.csv')

flower_labels = ['Iris-setosa','Iris-versicolor','Iris-virginica']
setosa_lenghts = df[df['class']=='Iris-setosa']['petal_length']
versicolor_lenghts = df[df['class']=='Iris-versicolor']['petal_length']
virginica_lenghts = df[df['class']=='Iris-virginica']['petal_length']
Iris_data = [setosa_lenghts, versicolor_lenghts, virginica_lenghts]

#fig = ff.create_distplot(Iris_data, flower_labels, bin_size=[.005,.005])
fig = ff.create_distplot(Iris_data, flower_labels)
pyo.plot(fig)
# Define the traces

# HINT:
# This grabs the petal_length column for a particular flower
# df[df['class']=='Iris-some-flower-class']['petal_length']



# Define a data variable



# Create a fig from data and layout, and plot the fig