'''В созданном в задаче 1 файле написать код программы, которая выполняет следующие действия:
- с клавиатуры ввести значение переменной A типа int и переменной В типа float;
- вывести переменные A и В на экран;
- перемножить переменные А и В и записать результат в переменную С;
- вывести на экран тип данных переменной С.'''
A=int(input('Введите А= '))
B=float(input('Введите В= '))
print('A=',A,'B=',B)
C=A*B
print(C,'тип С ',type(C))

'''Напишите программу, которая вычисляет минимальное целое положительное число
среди введенных значений. Признаком конца ввода является символ «.».
Организовать работу программы через цикл while.'''
a=input('Введите число или "."')
minim=2**20
while a!='.':
    if '.' in a:
        print('число вещественное, а не целое')
    elif int(a)>0:
        if  minim>int(a):
            minim=int(a)
    a=input('Введите число или "."')
print(minim)

#Для введенной произвольной строки выведите(на отдельной строке):
#o	второй символ этой строки;
#o	предпоследний символ этой строки;
#o	первые 3 символа этой строки;
#o	всю строку, кроме последних двух символов;
#o	все символы строки через один в обратном порядке, начиная с последнего;
# o	длину данной строки.
a = input()
print(a[1], a[-2], a[0:3], a[:-2], a[::-1], len(a))

#Пользователь вводит исходную строку в переменную stroka
# и символ в переменную simvol
#Подсчитайте, сколько раз заданный символ
#встречается в исходной строке
stroka = input()
simvol = input()
print(stroka.count(simvol))

# Дан кортеж korteg = (13, 2, 23, 14, 5).
# Вывести на экран все элементы кортежа, значение которых больше 10

korteg = (13, 2, 23, 14, 5)
for i in range(len(korteg)):
    if korteg[i] > 10:
        print(korteg[i])

#Сформируйте список a = [5, -2, 5, 3, 4, 12, 17].
#Вычислите и выведите среднее арифметическое
# значение положительных элементов списка.
a = [5, -2, 5, 3, 4, 12, 17]
b = 0
for i in range(len(a)):
    if a[i] > 0:
        b += a[i]
print(b / len(a))

# Разработайте функцию my_func, суммирующую элементы произвольного списка.

def my_func(list):
    a = 0
    for i in list:
        a += i
    return a
print(my_func([2, 3, 4, 5, 6, 7]))
print(my_func([2, 3, 4]))

#Имеется список названий месяцев: [‘января’, ‘февраля’, ‘марта’, ‘апреля’, ’мая’, ‘июня’, ‘июля’, ‘августа’, ‘сентября’, ‘октября’, ‘ноября’, ‘декабря’].
#Создайте по этому списку словарь, в котором название месяца будет ключом, а номер месяца (от 1 до 12) – значением.
a = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
z = {}
for i in range(1, 13):
    z[a[i-1]] = i
print(z)

#Создайте два множества A и B, добавив в A 10 случайных целых чисел от 1 до 20, а в B добавив 5 случайных чисел.Вывести полученные множества на экран.
import random
A,B=set(),set()
while len(A)!=10:
    A.add(random.randint(1,20))
print(A,'длина А=',len(A))
while len(B)!=5:
    B.add(random.randint(1,20))
print(B,'длина B=',len(B))



