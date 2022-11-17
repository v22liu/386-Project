
import numpy as np
from numpy import *
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def plot_heatmap(coordinates):
    positions = np.array(coordinates)

    df = pd.DataFrame(positions, columns = ['X_value','Y_value','Z_value'])
    pivotted= df.pivot('Y_value','X_value','Z_value')
    sns.heatmap(pivotted,cmap='RdBu')
    plt.show()
