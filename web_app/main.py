from flask import Flask, render_template, url_for, request, jsonify, redirect, send_file
import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)


county19 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2019.csv')
county20 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2020.csv')
county21 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2021.csv')
monitor19 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2019.csv')
monitor20 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2020.csv')
monitor21 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2021.csv')
data=pd.read_csv(csvfile)


@app.route('/index.html', methods=['GET', 'POST'])
def update_file(request):

        with open('web_app/Datasets/annual_aqi_by_county_2019.csv', 'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                Names.append(row[0])
                Values.append(int(row[1]))
        redirect('barchart.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0')
