from scipy.signal import butter, lfilter

def butter_lowpass(cutoff, fs, order):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    return butter(order, normal_cutoff, fs=fs, btype='low', analog=False)


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


def butter_bandpass(lowcut, highcut, fs, order):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


def filter_data_lowpass(df, cols_to_filter, cutoff, fs):
    for col in cols_to_filter:
        filtered_col = butter_lowpass_filter(df[col], cutoff, fs) 
        new_col_name = col + "_Filt"
        df[new_col_name] = filtered_col

    return df


def filter_data_bandpass(df, cols_to_filter, low_cutoff, high_cutoff, fs):
    for col in cols_to_filter:
        filtered_col = butter_bandpass_filter(df[col], low_cutoff, high_cutoff, fs) 
        new_col_name = col + "_Filt"
        df[new_col_name] = filtered_col

    return df