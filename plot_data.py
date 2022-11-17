from scipy.fft import rfft, rfftfreq
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, fixed, interact_manual, Layout, HBox, IntRangeSlider, IntSlider
import ipywidgets as widgets


def plot_FFT(df, col, timestep):

    xf = rfftfreq(len(df), timestep)[:len(df)//2]
    yf = rfft(df[col].values)
    yplot = 2.0/len(df) * np.abs(yf[0:len(df)//2])

    plt.figure(figsize=(20, 10))
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='grey')
    plt.grid(which='minor', linestyle='-', linewidth='0.5', color='gainsboro')

    p1, = plt.plot(xf, yplot)

    plt.xlabel('Freq')
    plt.title('FFT')

    return p1


def plot_phasor(y_val, x_val, label):

    theta = np.arctan2(y_val, x_val)
    mag = np.sqrt((y_val**2)+(x_val**2))

    plt.figure(figsize=(20,20))
    p1, = plt.polar([0, theta], [0, mag], label = label)
    plt.legend(p1, label , loc='upper left')

    return p1


def get_slider_on_col_data(df, col_to_slice):
    first_val = df[col_to_slice].iat[0]
    last_val = df[col_to_slice].iat[-1]

    range =  widgets.IntRangeSlider(
                                    value=[first_val, last_val],
                                    min=first_val,
                                    max=last_val,
                                    step=1,
                                    description=col_to_slice,
                                    disabled=False,
                                    continuous_update=False,
                                    orientation='horizontal',
                                    readout=True,
                                    readout_format='d',
                                    layout=Layout(width='2000px', overflow='true')
    )
    display(range)
    return range


def slice_data (start_slice, end_slice, df, col_to_slice):
    df = df[(df[col_to_slice] > start_slice) & (df[col_to_slice] < end_slice)]     
    return df


def select_cols_to_plot(df, ignore_cols_list):
    check_list = []

    for col in df.columns:
        if col in ignore_cols_list:
            continue

        check_list.append(widgets.Checkbox(
                                value=False,
                                description=col,
                                disabled=False,
                                indent=False)
        )
        display(check_list[-1])

    return check_list


def plot_selected_cols(check_list, df, x_col, fig, ax):
    for check_box in check_list:
        if check_box.value == True:        
            df.plot(x = x_col, y = check_box.description, ax = ax, figsize=(30,15), label=check_box.description, legend=False)


    
