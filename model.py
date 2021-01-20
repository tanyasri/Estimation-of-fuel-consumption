# import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('MyEstimation.csv')

dataset['time'].fillna(0, inplace=True)

dataset['load'].fillna(dataset['load'].mean(), inplace=True)
dataset['temp'].fillna(dataset['temp'].mean(), inplace=True)
dataset['fuel'].fillna(dataset['fuel'].mean(), inplace=True)
X = dataset.iloc[:, :3]


def convert_to_int(word):
    word_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
                 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'zero': 0, 0: 0}
    return word_dict[word]


X['time'] = X['time'].apply(lambda x: convert_to_int(x))

y = dataset.iloc[:, -1]

regressor = LinearRegression()

regressor.fit(X, y)

pickle.dump(regressor, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))
