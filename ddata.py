# -*- coding: UTF-8 -*-
import requests
import json
import csv
file = open('res.log','a')

def my_function(querry):
    
    url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/party'
    headers = {'Content-type': 'application/json',
            'Accept': 'application/json',
            'Authorization':'Token 58cdfc40a1101dbc2ad9977ee896e6fa2c2937f6',
            'Content-Encoding': 'UTF-8'
            }
    data = {'query':querry}

    answer = requests.post(url, data=json.dumps(data), headers=headers)
    response = answer.json()
    # json.dump(response, outfile, indent=4)
    # res = json.dumps(response, ensure_ascii=False)
    # print res
    # json.dump(response, outfile, indent=4)
    # array = json.loads(res)
    # res_string = response['suggestions'][0]['data']['name']['short'] + ';' + response['suggestions'][0]['data']['inn']+ ';' + response['suggestions'][0]['data']['kpp']
    # print response['suggestions'][0]['data']
    # res = json.dumps(response, ensure_ascii=False)
    print response['suggestions'][0]['data']

    array = response['suggestions']
    for val in array:
        string = val['data']['name']['full'] + ';' + val['data']['address']['value'] + ';' + val['data']['inn'] + ';' + val['data']['kpp'] + '\n'
        file.write(string.encode('utf8'))
           

with open('data.csv', 'r') as fp:
    # reader = csv.reader(fp, delimiter=';', quotechar='"')
    reader = csv.DictReader(fp, delimiter=';', quotechar='"')
    data = [r for r in reader]
    for row in data:
        my_function(row['Name'])

file.close()        