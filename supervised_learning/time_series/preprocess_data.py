#!/usr/bin/env python3
"""
Preprocesses data used to train and predict the value of Bitcoin
"""

import pandas as pd
import matplotlib.pyplot as plt


def preprocess_data():
    """
    Preprocesses the data used to train and predict the value of Bitcoin.

    Returns:
        tuple: A tuple containing the preprocessed training, validation, and testing data.
    """
    
    # Read the Bitcoin data from a CSV file
    data = pd.read_csv("coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv")

    # Remove missing values
    data = data.dropna()

    # Split the data for training (70%), validation (20%), and testing (10%)
    data_length = len(data)
    train_data = data[0:int(data_length * 0.7)]
    valid_data = data[int(data_length * 0.7):int(data_length * 0.9)]
    test_data = data[int(data_length * 0.9):]

    # Normalize the data based on training data
    train_mean = train_data.mean()
    train_std = train_data.std()
    train_data = (train_data - train_mean) / train_std
    valid_data = (valid_data - train_mean) / train_std
    test_data = (test_data - train_mean) / train_std

    # Generate a plot to visualize the data
    plot_features = data['Close']
    plot_features.index = data['Timestamp']
    plot_features.plot(subplots=True)

    # Generate another plot to visualize the processed data
    plot_features = data['Close']
    plot_features.index = data['Timestamp']
    plt.plot(plot_features.index, plot_features, 'r--', label='Processed')
    plt.xlabel('Time')
    plt.ylabel('Bitcoin Close Value')
    plt.title("Preprocessed Bitcoin Data")
    plt.legend()
    plt.show()

    return train_data, valid_data, test_data
