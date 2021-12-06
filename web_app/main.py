from flask import Flask, render_template, url_for, request
import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib as plt

app = Flask(__name__)

cbsa19 = pd.read_csv('web_app/Datasets/annual_aqi_by_cbsa_2019.csv')
cbsa20 = pd.read_csv('web_app/Datasets/annual_aqi_by_cbsa_2020.csv')
cbsa21 = pd.read_csv('web_app/Datasets/annual_aqi_by_cbsa_2021.csv')
county19 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2019.csv')
county20 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2020.csv')
county21 = pd.read_csv('web_app/Datasets/annual_conc_by_monitor_2019.csv')
monitor19 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2019.csv')
monitor20 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2020.csv')
monitor21 = pd.read_csv('web_app/Datasets/annual_aqi_by_county_2021.csv')


@app.route('/update_file', methods=['GET', 'POST'])
def update_file(request):
    if request.is_ajax():
        data = request.POST.get('form_data')

        lat = data.lat
        long = data.long

    return render_template("stats.html")


# main driver function

if __name__ == '__main__':
    app.run(host='0.0.0.0')
