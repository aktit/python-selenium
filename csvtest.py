import csv
with open('data.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    data = [row for row in spamreader]
    # var1 = [i for i in data[0]]
    # var2 = [i for i in data[1]]
    #data2 = [i for i in data for j in i]
    test = [i for i in data for j in i]

import pandas
# colnames = ['Question', 'Date']
# var1 = pandas.read_csv('data.csv', names=colnames)
var1 = pandas.read_csv('data.csv')
questions = var1['Questions']
pub_date = var1['Pub_date']
res = dict(zip(questions, pub_date))

