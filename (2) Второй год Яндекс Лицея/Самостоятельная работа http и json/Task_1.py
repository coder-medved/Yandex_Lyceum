import sys
import json

data = list(map(str.strip, sys.stdin))
dict_json = {
    "request": {},
    "response": {}
}

for dat in data:
    wave, num = dat.split(' = ')
    if int(num) > 0:
        dict_json["response"][wave] = num
    elif int(num) < 0:
        dict_json["request"][wave] = num

with open('contact.json', 'w') as ready_file:
    json.dump(dict_json, ready_file)