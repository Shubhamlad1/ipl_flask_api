import pandas as pd
import numpy as np


ipl_data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv")


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
