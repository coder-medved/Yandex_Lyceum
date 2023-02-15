import argparse
import requests
import csv

parser = argparse.ArgumentParser(description="CheatCode")
parser.add_argument("host")
parser.add_argument("port")
parser.add_argument('--not_mult', default=100, type=int, help='not_mult')
parser.add_argument('--smallest', default=0, type=int, help='smallest')
args = parser.parse_args()

request = 'http://' + args.host + ':' + args.port
response = requests.get(request)
if response:
    json_response = response.json()

result = dict()
for data in json_response:
    for key in data:
        if key not in result:
            result[key] = []
        for num in data[key]:
            if num % args.not_mult != 0 and num >= args.smallest:
                result[key].append(num)

sorted_result = sorted(result.items(), key=lambda x: x[0])

with open('truth.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for dat in sorted_result:
        res = []
        res.append(dat[0])
        res.append(max(dat[1]))
        res.append(min(dat[1]))
        res.append('{:.2f}'.format(sum(dat[1])/len(dat[1])))
        res.append(sum(dat[1]))
        writer.writerow(res)