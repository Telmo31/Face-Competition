import pandas as pd
import numpy as np




def make_file(dataframe):
	
	i = 0
	counter = 0

	while (i <= 9.98):
		j = 0
		while (j <= 7.50):
			df_bar =dataframe[dataframe['y'] <=i + 0.02]
			df_bar =df_bar[df_bar['y'] >=i]
			df_bar =df_bar[df_bar['x'] <=j+2.5]
			df_bar =df_bar[df_bar['x'] >=j]

			X = df_bar[['x','y','hour','dayofweek','dayofyear']]





			a = str(round(i,2))

			X.to_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Data_squares\\X_test' + str(counter) + '.csv')



			counter = counter + 1 
			print (counter)
			j = j +2.5
			
		i = i + 0.02









df_train = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\test.csv')


df_train["hour"] = (df_train["time"]%(60*24))/60.
df_train["dayofweek"] = np.ceil((df_train["time"]%(60*24*7))/(60.*24))
df_train["dayofyear"] = np.ceil((df_train["time"]%(60*24*365))/(60.*24))

print ("ola")


make_file(df_train)




