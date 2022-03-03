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



#county19 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2019.csv')
#county20 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2020.csv')
#county21 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2021.csv')

#monitor19 = pd.read_csv('web_app/Datasets/annual_conc_by_monitor_2019.csv')
#monitor20 = pd.read_csv('web_app/Datasets/annual_conc_by_monitor_2020.csv')




@app.route('./index.html', methods=['GET', 'POST'])
def barchart(request):
        df = pd.read_csv('web_app/Datasets/County/annual_aqi_by_county_2019.csv')
        form=request.form
        for field in form:
         if field.has_key('state'):
                filtered_df= df["State"]
                new_df =  filtered_df.groupby(['State'])['Median AQI'].sum().reset_index()
                data = [go.Bar(x=new_df['State name'], y=new_df['Median AQI'])]
                layout = go.Layout(title='Average AQI 2021', xaxis_title="State",
                yaxis_title="AQI Value")            
                fig = go.Figure(data=data, layout=layout)
                pyo.plot(fig, filename='barchart.html', auto_open=False)
        
         elif  field.has_key('county'): #if user enters filter by county
                filtered_df= df["County"]
                new_df =  filtered_df.groupby(['County'])['Median AQI'].sum().reset_index()
                data = [go.Bar(x=new_df['State name'], y=new_df['Median AQI'])]
                layout = go.Layout(title='Average AQI 2021', xaxis_title="State",
                yaxis_title="AQI Value")            
                fig = go.Figure(data=data, layout=layout)
                pyo.plot(fig, filename='barchart.html', auto_open=False)

         elif  field.has_key('aqi'): # if user enters by median AQI
                filtered_df= df["Median AQI"]
                new_df =  filtered_df.groupby(['State name'])['Median AQI'].sum().reset_index()
                data = [go.Bar(x=new_df['State name'], y=new_df['Median AQI'])]
                layout = go.Layout(title='Average AQI 2021', xaxis_title="State",
                yaxis_title="AQI Value")            
                fig = go.Figure(data=data, layout=layout)
                pyo.plot(fig, filename='barchart.html', auto_open=False)


        return redirect("./barchart.html")
    

if __name__ == '__main__':
  app.run()



