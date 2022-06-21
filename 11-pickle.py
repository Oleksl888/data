"""Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON."""
import json
import pickle


class Merch():
    def __init__(self, name=None, price=0):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.price}'

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.name}, {self.price}'

    def jsonize(self):
        return { 'name': self.name, 'price': self.price }

    @classmethod
    def dejsonize(cls, jobject):
        return cls(jobject['name'], jobject['price'])


if __name__ == '__main__':
    merchandise = [
        Merch('shapka', 100),
        Merch('Noski', 50),
        Merch('Shtani', 40)
    ]
    with open('picklized.json', 'wb') as file:
        pickle.dump(merchandise, file)
    with open('jsonized.json', 'w') as file:
        json.dump(merchandise, file, default=Merch.jsonize)
    merchandise = [
        ('Shtani za 40 grn', 100),
        ('Kozhanaya kurtka shob buti vitrivalim do zhari', 1000),
    ]
    picklized = pickle.dumps(merchandise)
    jsonized = json.dumps(merchandise)
    print(picklized)
    print(jsonized)
    print(pickle.loads(picklized))
    print(json.loads(jsonized))
    with open('picklized.json', 'rb') as file:
        data = pickle.load(file)
        print(data)
    with open('jsonized.json') as jfile:
        print(json.load(jfile, object_hook=Merch.dejsonize))
