
import numpy as np
from numpy import *
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def plot_heatmap(coordinates):
    positions = np.array(coordinates)

    df = pd.DataFrame(positions, columns = ['X_value','Y_value','Z_value'])
    df.rolling(5).mean()
    df = df.iloc[::5, :]
    pivotted= df.pivot('Y_value','X_value','Z_value')
    map = sns.heatmap(pivotted,vmax=120,vmin=0,cmap='Blues_r')
    map.invert_yaxis()
    map.invert_xaxis()
    plt.show()
    print(df)

# test_positions = [[1100.0, 1100.0, 92.08], [1300.0, 1100.0, 125.18], [1500.0, 1100.0, 28.91], [1700.0, 1100.0, 56.61], [1900.0, 1100.0, 98.39], [1900.0, 1300.0, 14.27], [1700.0, 1300.0, 99.37], [1500.0, 1300.0, 84.26], [1300.0, 1300.0, 11.59], [1100.0, 1300.0, 74.55], [1100.0, 1500.0, 26.82], [1300.0, 1500.0, 121.3], [1500.0, 1500.0, 133.7], [1700.0, 1500.0, 70.13], [1900.0, 1500.0, 108.08], [1900.0, 1700.0, 124.37], [1700.0, 1700.0, 120.36], [1500.0, 1700.0, 19.67], [1300.0, 1700.0, 24.08], [1100.0, 1700.0, 61.16], [1100.0, 1900.0, 28.91], [1300.0, 1900.0, 165.72], [1500.0, 1900.0, 124.78], [1700.0, 1900.0, 121.56], [1900.0, 1900.0, 0.93]]
# plot_heatmap(test_positions)