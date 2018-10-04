import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('/Users/patrickbutler/documents/NFLDataScience/nflstatistics/rec_game_logs.csv')

data = data[data.Year >= 2004]
data = data[data.Season == "Regular Season"]

train, test = train_test_split(data, test_size = 0.2, stratify = data.Year)
