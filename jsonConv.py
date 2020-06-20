person = {}

person['leo']= {
	'name': 'leo',
	'address': '21 ave, Carlton, CA 908932', 
	'phone_no': '777-9311',
	'email_id': None
	}

import json
s = json.dumps(person)

with open("data.json", "w") as f:
	f.write(s)