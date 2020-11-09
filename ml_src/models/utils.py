import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from gensim.models import Word2Vec


def get_words():
    with open('./temp.txt') as file:
        lines = []
        for line in file:
            lines.append(line)
    return lines

def encode_df(df):
    one_hot = OneHotEncoder()
    encoded = one_hot.fit_transform(df.to_numpy()).toarray()
    return encoded


def split_data(x_size, y_size, df):
    x = df[0: x_size, :]
    y = df[x_size: x_size + y_size, :]
    return x, y


def shift_y(y):
    zeros = np.zeros([1, y.shape[1]])
    y = np.concatenate([zeros, y])
    return y[:-1, :]


def organize_data(x, y):
    y_shift = shift_y(y)
    x = np.concatenate([x, y_shift])
    return x, y


if __name__ == '__main__':
    frame = encode_df(frame)
    dx, dy = split_data(12, 4, frame)
    dx, dy = organize_data(dx, dy)
    print()