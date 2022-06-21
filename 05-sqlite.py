'''Для таблицы «материала» из дополнительного задания создайте пользовательскую функцию,
которая принимает неограниченное количество полей и возвращает их конкатенацию.'''


import sqlite3


class Concatenate:
    def __init__(self):
        # инициализируем контейнер
        self.entry = []

    def step(self, *value):
        # добавляем элемент в контейнер
        for elem in value:
            self.entry.append(str(elem))

    def finalize(self):
        # завершение агрегации
        return ''.join(self.entry)


db = sqlite3.connect('mydb.sqlite3')
db.create_aggregate('concatenate', -1, Concatenate)
cur = db.cursor()
result = cur.execute('SELECT concatenate(identifier, weight, height, characteristics) FROM materials')
#result = cur.execute('SELECT * FROM materials')
print(result.fetchall())