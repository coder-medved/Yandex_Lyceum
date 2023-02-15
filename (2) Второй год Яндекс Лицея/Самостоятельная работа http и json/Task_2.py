import requests
import json

with open('host_info.json') as address_file:
    data = json.load(address_file)
server = data['server']
port = data['port']
key = data['key']

request = 'http://' + server + ':' + port
response = requests.get(request)
if response:
    json_response = response.json()

data = json_response[key]
data['source'].sort()
data['modified'].sort()
n = len(data['source'])

summa = 0
for i in range(n):
    summa += (data['source'][i] - data['modified'][i]) ** 2
summa = summa / n

print('{:.3f}'.format(summa))