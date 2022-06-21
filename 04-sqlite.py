'''Для таблицы «материала» из дополнительного задания создайте пользовательскую
агрегатную функцию, которая считает среднее значение весов всех материалов
результирующей выборки и округляет данной значение до целого.'''
import sqlite3


class Average:
    def __init__(self):
        # инициализируем контейнер
        self.entry = []

    def step(self, value):
        # добавляем элемент в контейнер
        self.entry.append(value)

    def finalize(self):
        # завершение агрегации
        return round(sum(self.entry)/len(self.entry))


db = sqlite3.connect('mydb.sqlite3')
db.create_aggregate('average', 1, Average)
cur = db.cursor()
result = cur.execute('SELECT average(weight) FROM materials')
print(result.fetchall())