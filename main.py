"""
    Title: Hotel Recommendation System
    Module Name: main.py
    Author: Hema Agrawal
    Language: Python
    Date Created: 20-12-2019
    Date Modified: 04-01-2020
"""
import pandas as pd
from scraping import *
from flask import Flask,render_template, request, url_for, redirect
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("main.html")
@app.route("/model_page", methods=['GET', 'POST'])
def page():
    if request.method == "POST":
        city_name1= request.form.get("mycity", None)
        check_in= request.form.get("check-in", None)
        check_out = request.form.get("check-out", None)
        city_name = city_name1.capitalize()
        obj = scrap(city_name, check_in, check_out)
        n=obj.func(city_name, check_in, check_out)
        if n=="Error":
            return render_template('index.html')
        else:
            df=pd.read_csv('data_scanner.csv')
            return render_template("result.html",df=df,m=15)
if __name__ == '__main__':
    app.run(debug=True)