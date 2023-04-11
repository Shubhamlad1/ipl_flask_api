from flask import Flask, jsonify, request
from ipl import *

app= Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/api/TeamToTeam/stat')
def TeamStats():
    team1= request.args.get('team1')
    team2= request.args.get('team2')

    team_data= TeamToTeam(team1, team2)
    print(team_data)
    return jsonify(team_data)

app.run(debug=True, port=7000)