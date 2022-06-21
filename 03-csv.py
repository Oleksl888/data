'''Поработайте с созданием собственных диалектов, произвольно выбирая правила для CSV файлов.
Зарегистрируйте созданные диалекты и поработайте, используя их, с созданием/чтением файлом.'''

import csv


class CustomDialect(csv.Dialect):
    delimiter = '+'
    doublequote = False
    escapechar = '-'
    lineterminator = '\n'
    quotechar = "'"
    quoting = csv.QUOTE_NONE
    skipinitialspace = True


csv.register_dialect('mydialect', delimiter=',', doublequote = True, escapechar = '=',
                     lineterminator='\n\n\n', quotechar='/', quoting=csv.QUOTE_MINIMAL)
mydialect = csv.get_dialect('mydialect')

sniffer = csv.Sniffer()
with open('cookbook.csv') as file:
    cook_list = []
    another_list = []
    content = file.read()
    dialect = sniffer.sniff(content)
    file.seek(0)
    reader = csv.reader(file, dialect=dialect)
    for line in reader:
        cook_list.append(line)
    dictreader = csv.DictReader(file, dialect=dialect)
    file.seek(0)
    for line in dictreader:
        another_list.append(line)
print(cook_list)
print(another_list)

dialect = CustomDialect
with open('newfile_book.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=another_list[0].keys(), dialect=dialect)
    writer.writeheader()
    for row in another_list:
        writer.writerow(row)

with open('newfile_book.csv', 'w') as outfile:
    writer = csv.writer(outfile, dialect=mydialect)
    for row in cook_list:
        writer.writerow(row)