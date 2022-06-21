'''Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму.
Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными
файлами.'''
import random
from array import array
import os


def float_to_text(filename):
    my_array = array('f', [random.random()*1000 for _ in range(10000)])
    with open(filename, 'wb') as file:
        file.write(my_array)


def text_to_float(filename):
    size = os.path.getsize('Binary_Randoms.bin')
    unit = array('f').itemsize
    my_array = array('f', [0 for _ in range(size // unit)])

    with open(filename, 'rb') as file:
        file.readinto(my_array)
    return sum(my_array.tolist())


if __name__ == '__main__':
    float_to_text('Binary_Randoms.bin')
    print(text_to_float('Binary_Randoms.bin'))
