import json
#import streamlit as st
#from streamlit_calendar import calendar
#from flask import Flask, render_template, jsonify
import os.path
from flask import jsonify
from flask import Flask
from flask import request
from flask import render_template

my_path = os.path.abspath(os.path.dirname(__file__))
data = os.path.join(my_path, "./sources/allevents_4.json")
with open(data, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
app = Flask(__name__)
events = data#[
#    {"title": "Meeting", "start": "2025-02-05"},
#    {"title": "Geburtstag", "start": "2025-02-12"},
#]

@app.route('/')
def index():
    return render_template('kalendar.html')
                           #/Users/huyduc/Downloads/dhvi_calendar_code/dash-full-calendar/assets/kalender.html')

@app.route('/events')
def get_events():
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)