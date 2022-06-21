'''Создайте функцию, которая будет создавать CSV файл на основе данных,
введенных пользователем через консоль. Файл должен содержать следующие колонки:
имена, фамилии, даты рождений и город проживания. Реализовать возможности перезаписи
данного файла, добавления новых строк в существующий файл, построчного чтения из файла
 и конвертацию всего содержимого в форматы XML и JSON.'''


import csv
import json
from xml.etree import ElementTree as ET
import datetime


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_MINIMAL
    lineterminator = '\n'
    delimiter = ','
    quotechar = '"'


def user_input():
    while True:
        name = input('Enter name: ')
        if len(name) < 1:
            continue
        lname = input('Enter last name: ')
        if len(lname) < 1:
            lname = 'LNU'
        while True:
            birthday = input('Enter birthdate in format dd/mm/yyyy: ')
            try:
                datelist = list(map(int, birthday.split('/')))
                datelist.reverse()
                date = datetime.date(*datelist)
                #date = date.strftime('%d %b %Y')
            except (ValueError, TypeError):
                print('Incorrect format, please try again')
                continue
            else:
                break
        while True:
            city = input('Enter city: ')
            if len(city) < 1:
                continue
            else:
                break
        break
    return {'first_name': name, 'last_name': lname, 'birthdate': date, 'city': city}


def user_info_loop():
    data = []
    while True:
        response = input('''
    Press <1> to add info
    Press <2> to quit
''')
        if response == '1':
            data.append(user_input())
            print('Info updated')
        elif response == '2':
            return data
        else:
            continue


def add_to_csv(data):
    if len(data) == 0:
        print("There's nothing to write")
        quit()
    with open('person_data.csv', 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=data[0].keys(), dialect=CustomDialect)
        writer.writeheader()
        for entry in data:
            writer.writerow(entry)


def append_to_csv(data):
    if len(data) == 0:
        print("There's nothing to write")
        quit()
    with open('person_data.csv', 'a') as outfile:
        writer = csv.writer(outfile, dialect=CustomDialect)
        for entry in data:
            writer.writerow(entry.values())


def read_csv_todict(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file, dialect=CustomDialect)
        for row in reader:
            data.append(row)
    return data


def read_csv_tostr(filename):
    data = []
    with open(filename, 'r') as file:
        content = file.read()
        dialect = csv.Sniffer().sniff(content)
        file.seek(0)
        reader = csv.reader(file, dialect=dialect)
        for line in file:
            data.append(line.strip())
    return data


def csv_to_json(data):
    def jsonize(obj):
        if isinstance(obj, datetime.date):
            return obj.strftime('%d %b %Y')
    return json.dumps(data, default=jsonize)


def csv_to_xml(data):
    root = ET.Element('data')
    i = 1
    for elem in data:
        person = ET.SubElement(root, 'person')
        person.set('number', str(i))
        i += 1
        for k,v in elem.items():
            info = ET.SubElement(person, k)
            info.text = v
    print(ET.dump(root))
    tree = ET.ElementTree(root)
    tree.write('person_data.xml', encoding='utf8')


if __name__ == '__main__':
    #person = user_info_loop()
    #add_to_csv(person)
    #append_to_csv(person)
    dic_data = read_csv_todict('person_data.csv')
    str_data = read_csv_tostr('person_data.csv')
    print(csv_to_json(dic_data))
    print(csv_to_json(str_data))
    #print(csv_to_json(person))
    csv_to_xml(dic_data)