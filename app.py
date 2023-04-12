from flask import Flask, jsonify, request
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



@app.route('/api/TeamToTeam/stat')
def TeamStats():
    team1= request.args.get('team1')
    team2= request.args.get('team2')

    team_data= TeamToTeam(team1, team2)
    print(team_data)
    return jsonify(team_data)

@app.route('/api/team_information')

def Team_data_info():
    team1= request.args.get('team1')

    data= Team_information(team1)

    return jsonify(data)

app.run(debug=True, port=7000)