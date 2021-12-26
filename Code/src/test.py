import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from dbLibrary import dbLibrary as std_db

mysql_db = std_db

query_results_db = pd.DataFrame(mysql_db.db_query('SELECT * FROM City_Bike_Data.main_city_bike;','City_Bike_Data'))


startStation = query_results_db['Start Station Name'].value_counts();

startStation_df = pd.DataFrame(startStation)


text_file = open("index.html", "w")
startStationHTML = startStation_df.to_html() 

text_file.write(startStationHTML())
text_file.close()
