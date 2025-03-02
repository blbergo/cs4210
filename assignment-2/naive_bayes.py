#-------------------------------------------------------------------------
# AUTHOR: Bryan Bergo
# FILENAME: naive_bayes.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2
# TIME SPENT: how long it took you to complete the assignment start 9 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#Reading the training data in a csv file
db = []
with open('./data/weather_training.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append(row)

#Transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]
feature_map = {
    'Sunny': 1,
    'Overcast': 2,
    'Rain': 3,
    'Hot': 1,
    'Mild': 2,
    'Cool': 3,
    'High': 1,
    'Normal': 2,
    'Weak': 1,
    'Strong': 2
}

X = []
for row in db:
    # skip 0 because it is the index
    X.append([feature_map[row[1]], feature_map[row[2]], feature_map[row[3]], feature_map[row[4]]])

#Transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
Y = []
for row in db:
    Y.append(feature_map[row[4]])

#Fitting the naive bayes to the data
clf = GaussianNB(var_smoothing=1e-9)
clf.fit(X, Y)

#Reading the test data in a csv file
dbTest = []
with open('./data/weather_test.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            dbTest.append(row)

#Printing the header os the solution
print('PREDICTIONS')
print('-----------')


#Use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
for data in dbTest:
    prediction = clf.predict_proba([[feature_map[data[1]], feature_map[data[2]], feature_map[data[3]], feature_map[data[4]]]])[0]
    print('Probability of No: ' + str(prediction[0]))
    print('Probability of Yes: ' + str(prediction[1]))
    print('-----------')


