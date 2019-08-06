# -*- coding: UTF-8 -*-
import requests
import json
import csv
file = open('res.csv','a')
# Записать шапку в файл
header = 'ИД;Тип;Запрос;Наименование;адрес;инн;кпп;оквэд' + '\n'
file.write(header)
# забрать ключ
f = open('key','r')
key = f.read()


# функция возврата строки с реквизитами
def my_function(querry, typ, sid):   
    url = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest/party'
    headers = {'Content-type': 'application/json',
            'Accept': 'application/json',
            'Authorization':key,
            'Content-Encoding': 'UTF-8'
            }
    data = {'query':querry , 'locations': [{'kladr_id': '66'},  {'kladr_id': '72'}, {'kladr_id': '74'}, {'kladr_id': '45'}]}
    print(querry)
    answer = requests.post(url, data=json.dumps(data), headers=headers)
    response = answer.json()
    # json.dump(response, outfile, indent=4)
    # res = json.dumps(response, ensure_ascii=False)
    # json.dump(response, outfile, indent=4)
    array = response['suggestions']
    for val in array:
      try:
        # чтоб не ломалось ничего
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
      
        string = sid + ';' + typ + ';' + querry + ';' + name + ';' + adress + ';' + inn + ';' + kpp + ';' + okved + '\n'

        s = val['data']['address']['value']
        # if s.lower().find("свердлов") > 0 or s.lower().find("челяб") > 0 or s.lower().find("тюмен") > 0 or s.lower().find("курган") > 0:
        # беру только нужные регионы - ищу вхождение ( поменял на фильтр в запросе)
        # regions_list = ['66', '72', '74', '45']
        # if inn[:2] in regions_list:
        file.write(string)
      except: continue

# читаем файл - забираем значения в словарь
with open('data.csv','r') as fp:
    print('Чтение файла')
    reader = csv.DictReader(fp, delimiter=';', quotechar='"')
    data = [r for r in reader]
    print('погнали')
    for row in data:
        my_function(row['Name'],row['type'],row['id'])
# закрываем за собой файл
file.close()
print('конец')

