import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "./../csv_file/market-price_2021.csv"
bitcoin_df = pd.read_csv(file_path, names = ['day', 'price'])

bitcoin_train_df = bitcoin_df.iloc[:361]