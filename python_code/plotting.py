
import numpy as np
from numpy import *
import seaborn as sns

positions = [[1100.0, 1100.0, 92.08], [1300.0, 1100.0, 125.18], [1500.0, 1100.0, 28.91], [1700.0, 1100.0, 56.61], [1900.0, 1100.0, 98.39], [1900.0, 1300.0, 14.27], [1700.0, 1300.0, 99.37], [1500.0, 1300.0, 84.26], [1300.0, 1300.0, 11.59], [1100.0, 1300.0, 74.55], [1100.0, 1500.0, 26.82], [1300.0, 1500.0, 121.3], [1500.0, 1500.0, 133.7], [1700.0, 1500.0, 70.13], [1900.0, 1500.0, 108.08], [1900.0, 1700.0, 124.37], [1700.0, 1700.0, 120.36], [1500.0, 1700.0, 19.67], [1300.0, 1700.0, 24.08], [1100.0, 1700.0, 61.16], [1100.0, 1900.0, 28.91], [1300.0, 1900.0, 165.72], [1500.0, 1900.0, 124.78], [1700.0, 1900.0, 121.56], [1900.0, 1900.0, 0.93]]


posx = np.array(str([pos[0] for pos in positions]))
posy = np.array(str([pos[1] for pos in positions]))
distance = np.array([pos[2] for pos in positions])

df = pd.DataFrame.from_dict(np.array([posx,posy,distance]).T)
df.columns = ['X_value','Y_value','Z_value']
df['Z_value'] = pd.to_numeric(df['Z_value'])

pivotted= df.pivot('Y_value','X_value','Z_value')

sns.heatmap(pivotted,cmap='RdBu')




# distances =  [ [0]*5 for j in range(5)]
# i = 0
# for y in range(len(distances[0])):
#     for x in range(len(distances)):
#         distances[x][y] = positions[i][2]
#         i+=1

# print(distances)