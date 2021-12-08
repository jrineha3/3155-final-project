from flask import Flask, render_template, url_for, request, jsonify, redirect, send_file
import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import io
import os
import glob
import plotly.offline as pyo
import plotly.graph_objs as go


app = Flask(__name__)

os.chdir("web_app/Datasets/County")
extensionCounty = 'csv'
all_filenames_County = [i for i in glob.glob('*.{}'.format(extensionCounty))]
#combine all files in the list
combined_csv_County = pd.concat([pd.read_csv(f) for f in all_filenames_County ])
#export to csv
combined_csv_County.to_csv( "county.csv", index=False, encoding='utf-8-sig')


#county19 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2019.csv')
#county20 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2020.csv')
#county21 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2021.csv')

#monitor19 = pd.read_csv('web_app/Datasets/annual_conc_by_monitor_2019.csv')
#monitor20 = pd.read_csv('web_app/Datasets/annual_conc_by_monitor_2020.csv')
#monitor21 = pd.read_csv('web_app/Datasets/annual_conc_by_monitor_2021.csv')
os.chdir("web_app/Datasets/Monitor")
extensionMonitor = 'csv'
all_filenames_Monitor = [i for i in glob.glob('*.{}'.format(extensionMonitor))]
#combine all files in the list
combined_csv_Monitor = pd.concat([pd.read_csv(f) for f in all_filenames_Monitor ])
#export to csv
combined_csv_Monitor.to_csv( "monitor.csv", index=False, encoding='utf-8-sig')


@app.route('./index.html', methods=['GET', 'POST'])
def barchart(request):

        df = pd.read_csv(combined_csv_County)

        filtered_df= df["Years"]
        # Removing empty spaces from State column to avoid errors
        filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        # Creating sum of number of cases group by State Column
        new_df =  filtered_df.groupby(['Years'])['90th Percentile AQI'].sum().reset_index()
        # Sorting values and select first 20 states
        new_df = new_df.sort_values(by=['90th Percentile AQI'], ascending=[True]).head(20)
        # Preparing data
        data = [go.Bar(x=new_df['Years'], y=new_df['90th Percentile AQI'])]
        # Preparing layout
        layout = go.Layout(title='Average AQI by Years', xaxis_title="Years",
                   yaxis_title="AQI Value")            
        # Plot the figure and saving in a html file
        fig = go.Figure(data=data, layout=layout)
        pyo.plot(fig, filename='barchart.html', auto_open=False)
        return redirect("./barchart.html")
    


@app.route('./index.html', methods=['GET', 'POST'])
def chloropleth(request):
            df = pd.read_csv(combined_csv_Monitor)
            data = dict(type='choropleth',
            # location: Arizoana, California, Newyork
            locations=['AZ', 'CA', 'NY'],


            # States of USA
            locationmode='USA-states',

            # colorscale can be added as per requirement
            colorscale='Reds',

            # text can be given anything you like
            text=['2019', '2020', '2021'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'AQI levels'})

            layout = dict(geo={'scope': 'usa'})

            # passing data dictionary as a list
            choromap = go.Figure(data=[data], layout=layout)



            # Plot the figure and saving in a html file
            pyo.plot(choromap, filename='choromap.html', auto_open=False)
            return redirect("./choropleth.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
