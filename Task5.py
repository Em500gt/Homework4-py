# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными. Степени многочленов могут отличаться.
import re

def read_file(file):
    with open(file, 'r') as data:
        pol = data.read().replace(' = 0', '')
    return pol

def separation_file(fl):
    dicke = {}
    fl = fl.replace('- ', '+ -')
    fl = re.sub("[*|^|]", " ", fl).split('+')
    fl = [char.split(' ') for char in fl]
    fl = [[i for i in j if i] for j in fl]

    for i in fl:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    
    fl = [[int(x) for x in j if x != 'x'] for j in fl]     

    for i in range(len(fl)):
        dicke[int(fl[i][1])] = int(fl[i][0])
    return dicke

def sum_file(f_first, f_second):
    result = {}
    maxx = max(max(f_first), max(f_second))
    for i in range(maxx, -1, -1):
        f = f_first.get(i)
        s = f_second.get(i)
        if f != None or s != None:
            result[i] = (f if f != None else 0) + (s if s != None else 0)
    return result

def create_polynomial(lst):
    result = ''
    for i in lst.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + '*x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + '*x^' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + '*x^' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + '*x^' + str(abs(i[0]))
    return result.replace('^1', '').replace('*x^0', ' = 0')

def write_file(s, name):
     with open(f'{name}.txt', 'w') as data:
         data.write(s)

first_file = read_file('first.txt')
second_file = read_file('second.txt')
split_first = separation_file(first_file)
split_second = separation_file(second_file)
new_file = create_polynomial(sum_file(split_first, split_second))

write_file(new_file, input("Введите название файла (без расширения): "))
