import pandas as pd
"""
data = {
	'apples': [3,2,0,1],
	'oranges': [0,3,7,2]
}

p = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
import json
s = json.dumps(p)

with open("data.json", "w") as f:
	f.write(s)
"""
df = pd.read_csv(r'test_data.csv')
df.to_json(r'data.json')

