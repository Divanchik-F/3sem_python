import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('flight_delays.csv')

res = df.loc[df['dep_delayed_15min'] == 'Y'].groupby('Distance').Dest.count()
img = res.plot(style = '.')
plt.xlabel('Distance')
plt.ylabel('Proportion of delays')
img.figure.savefig('images/18_2.png', bbox_inches='tight')