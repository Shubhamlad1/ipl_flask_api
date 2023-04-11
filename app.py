from flask import Flask,jsonify
from ipl import *

app= Flask(__name__)

@app.route('/')
def home():

    text_data='''
        Please Go through the below api's.
        1. http://127.0.0.1:7000/api/team_names : Will return all team names in ipl.
        2. Here another API will come
        '''
    return text_data

@app.route('/api/team_names')
def team_names():
    teams = Team_Names()
    print(teams)
    return jsonify(teams)



app.run(debug=True, port=7000)