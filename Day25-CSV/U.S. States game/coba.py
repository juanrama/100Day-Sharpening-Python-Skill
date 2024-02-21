import pandas as pd

data = pd.read_csv('50_states.csv')

state_coor = {}

for i in range(len(data)):
    state_coor[data['state'][i]] = [data['x'][i], data['y'][i]]

if 'Alabama' in state_coor:
    print('test')