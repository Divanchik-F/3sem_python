import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flight_delays.csv')

quant = df.groupby('UniqueCarrier').Dest.count()
y = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('UniqueCarrier').Dest.count()
res = y / quant
res = res.sort_values().head(10)
img = res.plot.bar()
plt.xlabel('UniqueCarrier')
plt.ylabel('Proportion of delays')
img.figure.savefig('images/18_5.png', bbox_inches='tight')