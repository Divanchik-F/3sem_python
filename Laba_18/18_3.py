import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flight_delays.csv')

quant = df.groupby('Dest').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Dest').Dest.count()
res = y / quant
res = res.sort_values(ascending=False).head(5)
img = res.plot.bar()
plt.xlabel('Destination')
plt.ylabel('Proportion of delays')
img.figure.savefig('images/18_3.png', bbox_inches='tight')