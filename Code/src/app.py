from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

df = pd.read_csv('/users/alidaneshmand/Desktop/PowerBI Dim Project Development.csv')




#pd.options.plotting.backend = "plotly"
#from IPython.display import HTML

#db_connection_str = 'mysql+pymysql://alidaneshmand:Golnesha@localhost/Staging_DataSource'
#db_connection = create_engine(db_connection_str)






#results_df = pd.read_sql('SELECT * FROM City_Bike_Data.main_city_bike;', con=db_connection)

#start_stations = results_df['Start Station Name'].unique()
#start_stations_freq = results_df['Start Station Name'].value_counts()

#toHTML = results_df.to_html()
#print(toHTML)

#fig = start_stations_freq.plot()
#fig.show()

#fig2 = start_stations_freq.plot.bar()
#fig2.show()

#fig.write_image("linechart.jpeg")
#fig2.write_image("barchart.jpeg")

#plt.hist(start_stations_freq, 100)
#plt.show()

#plt.scatter(start_stations, start_stations_freq)
#plt.show()
