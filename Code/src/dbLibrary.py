from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import mysql.connector


class dbLibrary:

	def db_query(query, schema):


		hostname = "10.1.10.152"
		user = "alidaneshmand"
		password = "Golnesha"

		db_connection_str = f'mysql+pymysql://{user}:{password}@{hostname}/{schema}'
		db_connection = create_engine(db_connection_str) 

		results_df = pd.read_sql(query, con=db_connection)

		#print (results_df) 
		return results_df
