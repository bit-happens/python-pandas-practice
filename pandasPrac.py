import pandas as pd

#creating a python dictionary of fruit and customer purchases
data = {
	'apples': [3,2,0,1],
	'oranges': [0,3,7,2]
}
"""
#pass the dictionary to the pandas DataFrame constructor
purchases = pd.DataFrame(data)
print(purchases)
"""
"""
#Use customers names as indexes
purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
print(purchases)
"""
#Read the data from a csv file
df = pd.read_csv('test_data.csv')
print(df)

#Remove auto generated indexes
df = pd.read_csv('test_data.csv',index_col=0)
print(df)
