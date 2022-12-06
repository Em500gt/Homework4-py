# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as rnd

def create_num(k):
    lst = [rnd(0, 101) for _ in range(k + 1)]
    return lst

def create_polynomial(lst, k):
    if k == 0:
        return "x = 0" 
    result = ''
    for i in range(len(lst) - 2):
        result += str(lst[i]) + f'*x^{k} + '
        k -= 1
    result += str(lst[-2]) + '*x + ' + str(lst[-1]) + ' = 0'
    return(result)

def write_file(s, name):
    with open(f'{name}.txt', 'w') as data:
        data.write(s)

n = ''

while n != 'n':
    k = int(input("Введите степень: "))
    write_file(create_polynomial(create_num(k), k), input("Введите название файла (без расширения): "))
    n = input('Файл создан. Хотите ещё создать файл? (Enter - Да, n - Нет): ')