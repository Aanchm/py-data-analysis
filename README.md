# Introduction 
This contains some basic function blocks for data analysis with python. This is updated as and when functions are needed and is focussed around working with using dataframes and creating plots. 

## Functions
clean_data.py: functions to filter a data by certain conditions
filter_data.py: low and band pass filters
analyse_data.py: generate statistics on data
plot_data.py: different types of plots on data (phasors, cartesian, FFTs)


# Requirements
- python 3
- All package requirements are in requirements.txt


# Build and Test
All functions are in the /src directory. To import the library: 
```
sys.path.append(rf"{Path(__file__).parent.parent}\src")
import push_pull_local as loc 
```
Tests are in the /tests directory

# Widgets
Widgets can be used when working with Jupyter notebooks.

Add the following lines to the notebook to use widgets:
```
%matplotlib ipympl
plt.style.use('seaborn-whitegrid')
```

# Limitations
- Further tests need to be written against pushing and pulling from Influx
- More functions needed to be added for working with different data files
- The Influx data pull and push can be further optimised
