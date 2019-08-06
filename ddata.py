# -*- coding: UTF-8 -*-
import requests
import json
import csv
file = open('res.csv','a')
header = 'Наименование;адрес;инн;кпп;оквэд'
file.write(header + '\n')
null_variable = None


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
    # json.dump(response, outfile, indent=4)
    array = response['suggestions']
    for val in array:
      try:
        if val['data']['name']['full'] is not None:
          name = val['data']['name']['full']
        else: name = ''

        if val['data']['address']['value'] is not None:
          adress = val['data']['address']['value']
        else: adress = ''

        if val['data']['inn'] is not None:
          inn = val['data']['inn']
        else:               
          inn = ''

        if val['data']['kpp'] is not None:
          kpp = val['data']['kpp']
        else:
          kpp = ''  

        if val['data']['okved'] is not None:
          okved = val['data']['okved']
        else:
          okved = ''
      
        string = name + ';' + adress + ';' + inn + ';' + kpp + ';' + okved + '\n'
        s = val['data']['address']['value']
        # file.write(string.encode('utf8'))
        # if s.lower().find("свердлов") > 0 or s.lower().find("челяб") > 0 or s.lower().find("тюмен") > 0 or s.lower().find("курган") > 0:
        file.write(string)
      except: continue

          
with open('data.csv','r') as fp:
    # reader = csv.reader(fp, delimiter=';', quotechar='"')
    reader = csv.DictReader(fp, delimiter=';', quotechar='"')
    data = [r for r in reader]
    for row in data:
        my_function(row['Name'])
        # print(row['Name'])
file.close()        