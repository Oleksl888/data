'''Создайте таблицу «материалы» из следующих полей: идентификатор, вес, высота и доп.
 характеристики материала. Поле доп. характеристики материала должно хранить в себе массив,
 каждый элемент которого является кортежем из двух значений, первое – название характеристики,
 а второе – её значение.'''

import sqlite3
import json


def to_json(some_tuple):
    return json.dumps(some_tuple)


def from_json(obj):
    return json.loads(obj)


sqlite3.register_adapter(list, to_json)
sqlite3.register_converter('json', from_json)
tables = sqlite3.connect('mydb.sqlite3', detect_types=sqlite3.PARSE_DECLTYPES)
cur = tables.cursor()
cur.execute('DROP TABLE IF EXISTS materials')
cur.execute('CREATE TABLE materials (identifier INTEGER NOT NULL UNIQUE, '
            'weight INTEGER, height INTEGER, characteristics json)')
cur.execute('INSERT INTO materials VALUES (?, ?, ?, ?)',
            (1, 100, 500, [('somecharectiristic', 50), ('another characteristic', 100)]))
cur.execute('INSERT INTO materials VALUES (?, ?, ?, ?)',
            (2, 200, 300, [('somecharectiristic', 11), ('another characteristic', 12)]))
cur.execute('INSERT INTO materials VALUES (?, ?, ?, ?)',
            (3, 2, 55, [('somecharectiristic', 1), ('another characteristic', 'a')]))
tables.commit()
tables.row_factory = sqlite3.Row
data = cur.execute('SELECT * FROM materials').fetchall()
print(data)
