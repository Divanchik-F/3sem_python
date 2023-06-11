import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flight_delays.csv')

quant = df.groupby('Origin').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Origin').Dest.count()
res = y / quant
res = res.sort_values(ascending=False).head(10)
img = res.plot.bar()
plt.xlabel('Origin')
plt.ylabel('Proportion of delays')
img.figure.savefig('images/18_6.png', bbox_inches='tight')