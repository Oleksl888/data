'''Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и
попробуйте загрузить данные из файла.'''

import json
import datetime

dict1 = dict(
    key1=1,
    key2=2,
    key3=3,
    key4=4
    )
dict2 = dict(
    name='Alex',
    lname='SLS',
    time=datetime.datetime.now(),
    pets=['cats', 'dogs', 'fishes'],
    cat=('Usatka', 2)
)


def to_json(data):
    if isinstance(data, datetime.datetime):
        return str(data)
    return data


j1 = json.dumps(dict1)
j2 = json.dumps(dict2, default=to_json)
print(j1, j2, sep='\n')
print('---------------------------------')

with open('j1.json', 'w') as file:
    json.dump(dict1, file)
with open('j2.json', 'w') as another_file:
    json.dump(dict2, another_file, default=to_json)

with open('j1.json') as file:
    print(json.load(file))

with open('j2.json') as another_file:
    print(json.load(another_file))
