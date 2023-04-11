import pandas as pd
import numpy as np


ipl_data = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRy2DUdUbaKx_Co9F0FSnIlyS-8kp4aKv_I0-qzNeghiZHAI_hw94gKG22XTxNJHMFnFVKsO4xWOdIs/pub?gid=1655759976&single=true&output=csv")


def Team_Names():
    Teams= list(set(list(ipl_data['Team1']) + list(ipl_data['Team2'])))
    team_dic= {'Teams': Teams}

    return team_dic
