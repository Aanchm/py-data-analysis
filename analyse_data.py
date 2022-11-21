import pandas as pd
import numpy as np
from scipy.integrate import cumtrapz
from scipy import interpolate


def calculate_rms(df, rms_column):
    rms = np.sqrt(np.mean(df[rms_column] ** 2))
    return rms


def get_stats_on_cols(df, col):
    standard_dev = df[col].std()
    standard_error = standard_dev/np.sqrt(len(df))

    return [standard_dev, standard_error]


def get_stats_on_col_by_groups(df, groupby_col, stats_col):

    stats = pd.DataFrame()
    grouped_data = df.groupby(groupby_col)

    for iter, group in grouped_data:
        mean = group[stats_col].mean()
        stddev = group[stats_col].std()
        new_row = pd.DataFrame([iter, mean, stddev], columns = [groupby_col, f"{stats_col}_Mean", f"{stats_col}_Std_Dev"])
        stats = pd.concat([stats, new_row], ignore_index = True)

    return stats


def count_data_cycle_number(df, cycle_col):
    df[f"{cycle_col} Count"] = 0
    count = 0
    prev_value = 0

    for index, row in df.iterrows():
        value = row[cycle_col]

        if value < prev_value:
            count += 1

        df[f"{cycle_col} Count"] = count
        prev_value = value
        
    return df


def integrate_data_col(df, col_x, col_y):
    df = df.reset_index(drop = True)
    df[f"{col_y}_integral"] = cumtrapz(df[col_y], df{col_y})

    return df


