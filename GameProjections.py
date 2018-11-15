import numpy as np
import pandas as pd
import tensorflow as tf
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
    if row['RushingYards'] != '--':
        total += float(row['RushingYards'])*0.1
    if row['RushingTDs'] != '--':
        total += float(row['RushingTDs'])*6
    if row['FumblesLost'] != '--':
        total -= float(row['FumblesLost'])*2
    return total



data = pd.read_csv('/Users/patrickbutler/documents/NFLDataScience/nflstatistics/rec_game_logs.csv')

# Remove the spaces in column names
data.columns = [c.replace(' ', '') for c in data.columns]

# We want to restrict data to only 2004 and later due to changed defensive pass
# inference rules - I believe this will have a significant effect on receiver trends
data = data[data.Year >= 2004]
data = data[data.Season == "Regular Season"]

# Calculate fantasy points in half PPR for each game log
data['halfPPR'] = data.apply (lambda row: halfPPRFantasyPoints (row), axis=1)

# Now look at the next row to get the fantasy scpre for the next game
data['nextGameScore'] = data['halfPPR'].shift(-1)

# Remove the last game for each player (Where the "next" score is from another player)
data['nextRowPlayer'] = data['PlayerId'].shift(-1)
data = data[data.PlayerId == data.nextRowPlayer]

train, test = train_test_split(data, test_size=0.2)
