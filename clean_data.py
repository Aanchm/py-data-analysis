import pandas as pd

def standardise_data_columns(df, column_to_standardise):
    df[column_to_standardise] = df[column_to_standardise] - df.at[0, column_to_standardise]
    return df


def filter_data_by_col_val(df, col, col_val):
    df = df[df[col] == col_val].reset_index(drop = 'True')
    return df


def filter_data_by_col_vals(df, col, col_vals_list):
    df = df[df[col].isin(col_vals_list)]
    return df


def select_data_columns(df, col_list)
    df.drop(columns=[col for col in df if col not in col_list], inplace=True)
    return df