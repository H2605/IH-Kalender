import json

#mport streamlit as st
#from streamlit_calendar import calendar
from flask import jsonify
from flask import Flask
from flask import request
from flask import render_template
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
data = os.path.join(my_path, "./sources/250518_allevents.json")
with open(data, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
app = Flask(__name__)
events = data
@app.route('/')
def index():
    return render_template('kalender.html')
@app.route('/events')
def get_events():
    return jsonify(events)
if __name__ == '__main__':
    app.run(debug=True)


#render_