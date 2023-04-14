import pandas as pd
import numpy as np


ipl_data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv")
ipl_ball = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRu6cb6Pj8C9elJc5ubswjVTObommsITlNsFy5X0EiBY7S-lsHEUqx3g_M16r50Ytjc0XQCdGDyzE_Y/pub?output=csv"
balls = pd.read_csv(ipl_ball)

def Team_Names():
    Teams= list(set(list(ipl_data['Team1']) + list(ipl_data['Team2'])))
    team_dic= {'Teams': Teams}

    return team_dic

def TeamToTeam(team1, team2): 
  temp_data= ipl_data[(ipl_data['Team1'] == team1) & (ipl_data['Team2']==team2) | (ipl_data['Team1']== team2) & (ipl_data['Team2']==team1)]
  Total_Matches_played = temp_data.shape[0]
  matches_own_by_team1 = temp_data['WinningTeam'].value_counts()[team1]
  matches_own_by_team2 = temp_data['WinningTeam'].value_counts()[team2]

  draw_Matches = Total_Matches_played - (matches_own_by_team1 - matches_own_by_team2)

  data_dict = {
      "Total_matched_Played" : str(Total_Matches_played),
      "matches_Own_by_Team1" : str(matches_own_by_team1),
      "matches_Own_by_Team2" : str(matches_own_by_team2),
      "Draw_Matched" : str(draw_Matches)
  }

  return data_dict


def Team_information(team_name1):
  temp_df= ipl_data[(ipl_data['Team1']==team_name1) | (ipl_data['Team2']==team_name1)]
  Total_Matches_played = temp_df.shape[0]

  Total_Matches_Own = temp_df[temp_df['WinningTeam']==team_name1].shape[0]
  Total_Matches_Loss = temp_df[temp_df['WinningTeam']!=team_name1].shape[0]
  Draw = Total_Matches_played - (Total_Matches_Own +Total_Matches_Loss)

  title_count = temp_df[temp_df['MatchNumber']== 'Final']['WinningTeam']==team_name1
  count=0
  for i in title_count:
    if i == True:
      count+=1
  information_dict = {
          "Total_Matches_played" : str(Total_Matches_played),
          "Total_Matches_Own" : str(Total_Matches_Own),
          "Total_Matches_Loss" : str(Total_Matches_Loss),
          "Draw Matches" : str(Draw),
          "Number of Tile Own": count
      
  }

  return information_dict


def player_list():
  players_list = list(set(list(list(balls['batter']) + list(balls['non-striker']))))

  player_dict= {
    'Players' : players_list
  }

  return player_dict


def Batsman_stats(player_name): 
  temp_df= balls[(balls['batter']== player_name)]
  temp_df = temp_df[~(temp_df['extra_type']=='wides')]
  top_score= temp_df.groupby('ID')['batsman_run'].sum().sort_values(ascending=False).head(1).values[0]
  Match_runs = temp_df.groupby('ID')['batsman_run'].sum()
  Total_Number_Sixes = temp_df[temp_df['batsman_run']==6].shape[0]
  Total_Number_Fours = temp_df[temp_df['batsman_run']==4].shape[0]
  Number_of_fifties= Match_runs[Match_runs >= 50].shape[0]
  Number_of_Hundrades = Match_runs[Match_runs >= 100].shape[0]
  Strike_Rate= (temp_df['batsman_run'].sum()/temp_df['ballnumber'].count())*100
  Total_runs= temp_df['batsman_run'].sum() 

  Batsman_stats = {
      'Top_Score': str(top_score),
      'Total_Number_Sixes' : str(Total_Number_Sixes),
      'Total_Number_Fours' : str(Total_Number_Fours),
      'Number_of_fifties' : str(Number_of_fifties),
      'Number_of_Hundrades' : str(Number_of_Hundrades),
      'Total_Runs': str(temp_df['batsman_run'].sum()),
      'Strike_Rate': str(Strike_Rate)

  }

  return Batsman_stats