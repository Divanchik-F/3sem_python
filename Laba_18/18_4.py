import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flight_delays.csv')

table = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Month').Month.count()
table = table.reset_index(name='count')
year_time_delay = [0] * 4
for i, row in table.iterrows():
    month = int(row['Month'].replace('c-', ''))
    year_time_delay[(month % 12) // 3] += row['count']

res = pd.DataFrame({
    'Time of year': ['winter', 'spring', 'summer', 'autumn'],
    'Proportion of delays': year_time_delay
    })

img = res.plot.bar(x='Time of year')
plt.xlabel('Destination')
plt.ylabel('Proportion of delays')
img.figure.savefig('images/18_4.png', bbox_inches='tight')