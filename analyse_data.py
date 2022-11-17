import pandas as pd
import numpy as np
from scipy.signal import butter, lfilter


def calculate_rms(df, rms_column):
    rms = np.sqrt(np.mean(df[rms_column] ** 2))
    return rms


def butter_lowpass(cutoff, fs, order=5):
    return butter(order, cutoff, fs=fs, btype='low', analog=False)


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def filter_data(df, cols_to_filter, cutoff):
    for col in cols_to_filter:
        filtered_col = butter_lowpass_filter(df[col], cutoff, 1000) 
        new_col_name = col + "_Filt"
        df[new_col_name] = filtered_col

    return df


def get_stats_on_columns(data, col):
    standard_dev = data[col].std()
    standard_error = standard_dev/np.sqrt(len(data))

    return [standard_dev, standard_error]


