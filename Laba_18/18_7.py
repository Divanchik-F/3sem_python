import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flight_delays.csv')

quant = df.groupby('DayOfWeek').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('DayOfWeek').Dest.count()
res = y / quant
img = res.plot.bar()
plt.xlabel('DayOfWeek')
plt.ylabel('Proportion of delays')
img.figure.savefig('images/18_7.png', bbox_inches='tight')