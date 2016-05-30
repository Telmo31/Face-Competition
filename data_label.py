
import pandas as pd

counter = 1


data_final = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Results\\results0.csv', index_col = 0)

while counter < 2000 :

	print (counter)

	y = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Results\\results' + str(counter) + '.csv', index_col = 0)

	
	
	data_final = data_final.append(y)

	

	
	counter = counter + 1

print (data_final.describe())





data_final.to_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Results\\data_final.csv')

print ("adeus")