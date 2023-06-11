import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flight_delays.csv')

quant = df.groupby('Month').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Month').Dest.count()
res = y / quant
img = res.plot.bar()
plt.xlabel('Month')
plt.ylabel('Proportion of delays')
img.figure.savefig('images/18_1.png', bbox_inches='tight')