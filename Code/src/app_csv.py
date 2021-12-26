from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import os

pd.options.plotting.backend = "plotly"
from IPython.display import HTML

#seti_raw_data_df = pd.read_csv('/Users/alidaneshmand/Downloads/Shot B10 Blue Cal.csv', header=None, nrows=5)
seti_raw_data_df = pd.read_csv('/Users/alidaneshmand/Downloads/Shot B10 Blue Cal.csv')
print (seti_raw_data_df)

toHTML = seti_raw_data_df.to_html('test.html')

#print(toHTML)


#fig = px.scatter(seti_raw_data_df['y(cm)'], seti_raw_data_df['y(cm)'])
#fig.show()

#fig = start_stations_freq.plot()
#fig.show()

#fig2 = start_stations_freq.plot.bar()
#fig2.show()

#fig.write_image("linechart.jpeg")
#fig2.write_image("barchart.jpeg")

#plt.scatter(seti_raw_data_df['x(nm)'], seti_raw_data_df['y(cm)'])
plt.scatter(seti_raw_data_df['y(cm)'], seti_raw_data_df['I(uW/cm3-sr-nm)'])
plt.show()
