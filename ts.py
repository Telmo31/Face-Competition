
import pandas as pd

data_final = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Results\\data_final.csv', index_col = 0 )




sorte = data_final.sort_index()


print(sorte.tail())






# for i in range(8607230):
# 	if b[i+1] == b[i]:
# 		print (b[i])

a = sorte.groupby(sorte.index).first()

b = a.index


count = 0

aux = 0

print (a.describe())

for i in range(8607202):

	if aux == 1:
		aux = 0
		continue

	if b[i+1 ] != i+1+ count :
		aux = 1
		
		print (b[i])


		a.loc[i+1+ count] = 8655834216
		count = count + 1


print(a.loc[13685])
print (a.describe())




a = a.groupby(a.index).first()

print(a.loc[105545])


a.to_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Results\\data_final2.csv' )


# print (a.describe())



# b = sorte.index


# for i in range(8607230):
# 	if i != b[i]:
# 		print (b[i])