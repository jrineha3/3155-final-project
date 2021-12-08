import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import os
import glob

# type defined is choropleth to
# plot geographical plots

os.chdir("web_app/Datasets/County")
extensionCounty = 'csv'
all_filenames_County = [i for i in glob.glob('*.{}'.format(extensionCounty))]
#combine all files in the list
combined_csv_County = pd.concat([pd.read_csv(f) for f in all_filenames_County ])
#export to csv
combined_csv_County.to_csv( "county.csv", index=False, encoding='utf-8-sig')
df = pd.read_csv(combined_csv_County)

data = dict(type='choropleth',

            # location: Arizoana, California, Newyork
            locations=['AZ', 'CA', 'NY'],

            # States of USA
            locationmode='USA-states',

            # colorscale can be added as per requirement
            colorscale='Portland',

            # text can be given anything you like
            text=['text 1', 'text 2', 'text 3'],
            z=df['90th Percentile AQI'],
            colorbar={'title': 'AQI Levels'})

layout = dict(geo={'scope': 'usa'})

# passing data dictionary as a list
choromap = go.Figure(data=[data], layout=layout)


# Plot the figure and saving in a html file
pyo.plot(choromap, filename='choromap.html', auto_open=False)
