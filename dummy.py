

import numpy as np
import pandas as pd


a = np.ones((8607230,), dtype=np.int)


y = np.multiply(a,1738433223)

print (y[0])
print (y[8607229])

df = pd.DataFrame(y, columns = ['place_id'])

print ('ola')

df.to_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Results\\data_final3.csv' )