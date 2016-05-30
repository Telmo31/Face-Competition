
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV


def run_algorithm():


	counter = 0

	while counter < 2000 :

		print (counter)

		X_train = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Data_squares\\X_train' + str(counter) + '.csv', index_col = 0)
		y_train = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Data_squares\\y_train' + str(counter) + '.csv', index_col = 0, names = ["place_id"])
		X_test = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Data_squares\\X_test' + str(counter) + '.csv', index_col = 0)
		y_train  = np.ravel(y_train)
		

		print ("ola")

		clf = RandomForestClassifier(n_estimators=100,  verbose=3, n_jobs = -1)
		clf = clf.fit(X_train, y_train)

		print ("adeus")


		a = clf.predict(X_test)

		df = pd.DataFrame(data = a, index = X_test.index.values,columns  = ['place_id'])

		df.to_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Results\\results' + str(counter) + '.csv')



		counter = counter + 1






#run_algorithm()

X_train = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Data_squares\\X_train692.csv', index_col = 0)
y_train = pd.read_csv('C:\\Users\\Telmo\\Desktop\\Python\\Face\\Data_squares\\y_train692.csv', index_col = 0, names = ["place_id"])


X_train, X_test, y_train, y_test = train_test_split( X_train, y_train, test_size=0.35)

y_train  = np.ravel(y_train)


#param_grid = {'n_estimators':[100,200,300], "max_depth": [3, None], "max_features": [1, 3, 5], "verbose": [3], "min_samples_split": [1, 3, 10], "min_samples_leaf": [1, 3, 10], "bootstrap": [True, False], "criterion": ["gini", "entropy"]}

print ("ola")

clf = RandomForestClassifier(n_estimators=150,  verbose=3, n_jobs = -1)

clf.fit(X_train, y_train)

print ("adeus")


a = clf.score(X_test,y_test)

print (a)











