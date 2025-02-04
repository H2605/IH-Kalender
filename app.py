import json

import streamlit as st
from streamlit_calendar import calendar
from flask import Flask, render_template, jsonify

data="/Users/huyduc/Downloads/dhvi_calendar_code/dash-full-calendar/assets/allevents_4.json"
#filename="/Users/huyduc/Downloads/dhvi_calendar_code/batch_data.json"
with open(data, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
app = Flask(__name__)
events = data#[
#    {"title": "Meeting", "start": "2025-02-05"},
#    {"title": "Geburtstag", "start": "2025-02-12"},
#]

@app.route('/')
def index():
    return render_template('calendar.html')
                           #/Users/huyduc/Downloads/dhvi_calendar_code/dash-full-calendar/assets/kalender.html')

@app.route('/events')
def get_events():
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)