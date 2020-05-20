import requests
import json

x = requests.get('https://www.hpb.health.gov.lk/api/get-current-statistical')
y = json.loads(x.text)
print(x.text)
print(y)
print(y['data']['update_date_time'])
