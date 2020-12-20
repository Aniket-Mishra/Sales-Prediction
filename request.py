import requests
import json

url = 'http://127.0.0.1:5000/results'

data = {'rating': 5, 'sales_in_month_1': 200, 'sales_in_month_2': 400}

data = json.dumps(data)
print(data)