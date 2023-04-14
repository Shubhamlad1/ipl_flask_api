from flask import Flask, jsonify, request, render_template
from ipl import *

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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

@app.route('/api/player_list')
def players():
    names= player_list()

    return jsonify(names)

@app.route('/api/player_stats/batting')
def player_statistics():
    name= request.args.get('player_name')

    stats_ = Batsman_stats(name)

    return jsonify(stats_)

app.run(debug=True, port=7000)