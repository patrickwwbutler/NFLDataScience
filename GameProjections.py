import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Simple method to calculate fantasy points
def halfPPRFantasyPoints(row):
    total = 0
    if row['ReceivingYards'] != '--':
        total += float(row['ReceivingYards'])*0.1
    if row['ReceivingTDs'] != '--':
        total += float(row['ReceivingTDs'])*6
    if row['Receptions'] != '--':
        total += float(row['Receptions'])*0.5
    if row['Rushing Yards'] != '--':
        total += float(row['RushingYards'])*0.1
    if row['RushingTDs'] != '--':
        total += float(row['RushingTDs'])*6
    if row['FumblesLost'] != '--':
        total -= float(row['FumblesLost'])*2
    return total


def getNextGameScore(row, data):
    id = row['PlayerId']
    year = row['Year']
    week = row['Week'] + 1
    playerSet = data[data.PlayerId == id]
    playerSeason = playerSet[playerSet.Year == year]
    nextGame = playerSeason[playerSeason.Week == week]
    score = nextGame['halfPPR']
    return score


data = pd.read_csv('/Users/patrickbutler/documents/NFLDataScience/nflstatistics/rec_game_logs.csv')

# Remove the spaces in column names
data.columns = [c.replace(' ', '') for c in data.columns]

# We want to restrict data to only 2004 and later due to changed defensive pass
# inference rules - I believe this will have a significant effect on receiver trends
data = data[data.Year >= 2004]
data = data[data.Season == "Regular Season"]

data = data.sort(['PlayerId', 'GameDate'])

# Calculate fantasy points in half PPR for each game log
#data['halfPPR'] = data.apply (lambda row: halfPPRFantasyPoints (row), axis=1)

print(getNextGameScore(pd.Series(data.iloc[[12]]), data))
# We now need a way to create y - the fantasy points scored in that player's next game
#data['nextGamePoints'] = data.apply (lambda row: getNextGameScores(row, data), axis = 1)

print(data.head(5))
