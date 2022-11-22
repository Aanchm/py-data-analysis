import pandas as pd
from scipy import signal

def standardise_data_col(df, col_to_standardise):
    if (col_to_standardise in df.columns) and df[col_to_standardise].dtypes != "object":
        df[col_to_standardise] = df[col_to_standardise] - df.at[0, col_to_standardise]
    return df


def normalise_data_col(df, col):
    if col in df.columns and df[col].dtypes != "object":
        df[col] = (df[col] - df[col].mean())
    return df


def filter_data_by_col_vals(df, col, col_vals_list):
    if col in df.columns:
        df = df[df[col].isin(col_vals_list)].reset_index(drop = "True")
    return df


def select_data_columns(df, col_list):
    df.drop(columns=[col for col in df if col not in col_list], inplace=True)
    return df


def start_data_after_first_peak(df, prominence, col):
    peaks = signal.find_peaks((df[col]).to_numpy(), prominence = prominence)
    first_peak_index = peaks[0][0]
    cropped_df = df[first_peak_index:df.index[-1]]
    cropped_df = cropped_df.reset_index(drop = True)

    return cropped_df


def get_data_with_col_greater_than_val(df, val, col):
    if col in df.columns and df[col].dtypes != "object":
        df = df[df[col] > val].reset_index(drop = True)
    
    return df