import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import os
import glob

# type defined is choropleth to
# plot geographical plots


df = pd.read_csv('./annual_aqi_by_county_2019.csv')


data = dict(type='choropleth',

            # location: Arizoana, California, Newyork
            locations=["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA","HI", "ID","IL","IN",
                        "IA","KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV","NH", "NJ",
                        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
                        "VT", "VA", "WA", "WV", "WI", "WY"],

            # States of USA
            locationmode='USA-states',

            # colorscale can be added as per requirement
            colorscale='Reds',
            autocolorscale=False,
            reversescale=False,

            # text can be given anything you like
            z=df['Median AQI'],
            colorbar={'title': 'Median AQI Levels'})

layout = dict(geo={'scope': 'usa'})

# passing data dictionary as a list
choromap = go.Figure(data=[data], layout=layout)
#choromap.show()



# Plot the figure and saving in a html file
pyo.plot(choromap, filename='choromap.html', auto_open=False)
