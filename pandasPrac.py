import pandas as pd

#creating a python dictionary of fruit and customer purchases
data = {
	'apples': [3,2,0,1],
	'oranges': [0,3,7,2]
}

#pass the dictionary to the pandas DataFrame constructor
purchases = pd.DataFrame(data)

print(purchases)
