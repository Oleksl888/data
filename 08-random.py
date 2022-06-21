'''Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму.'''
import random


def float_to_text(filename):
    with open(filename, 'w') as file:
        for _ in range(10000):
            file.write(str(random.random() * 1000) + '\n')


def text_to_float(filename):
    sum_ = 0
    with open(filename) as file:
        for line in file:
            if line[0].isdigit():
                sum_ += float(line)
    return sum_


if __name__ == '__main__':
    float_to_text('Randoms.txt')
    print(text_to_float('Randoms.txt'))
