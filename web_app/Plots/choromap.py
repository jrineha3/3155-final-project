import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# type defined is choropleth to
# plot geographical plots
data = dict(type='choropleth',

            # location: Arizoana, California, Newyork
            locations=['AZ', 'CA', 'NY'],

            # States of USA
            locationmode='USA-states',

            # colorscale can be added as per requirement
            colorscale='Portland',

            # text can be given anything you like
            text=['text 1', 'text 2', 'text 3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title Goes Here'})

layout = dict(geo={'scope': 'usa'})

# passing data dictionary as a list
choromap = go.Figure(data=[data], layout=layout)


# Plot the figure and saving in a html file
pyo.plot(choromap, filename='choromap.html', auto_open=False)
