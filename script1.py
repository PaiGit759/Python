#!/usr/bin/env python
import sys  # Загружает библиотечный модуль
from myfile import title
from fractions import Fraction

""" 
M = [[1, 2, 3], # Матрица 3 x 3 в виде вложенных списков
[4, 5, 6], # Выражение в квадратных скобках может
[7, 8, 9]]

print(sys.platform)
print(2 ** 100) # Возводит число 2 в степень 100
x = 'Spam!'
print(x * 8) # Дублирует строку
col2 = [row[1]+1 for row in M]
print(col2)

x = 4
while x > 0:
 print('spam!' * x)
 x -= 1

T = (1, 2, 3, 4, 5, 6, 4, 7, 4)

print(T.index(4))
print(T.count(4))


f = open('TXT/data.txt', 'w') # Создается новый файл для вывода
f.write('Hello\n') # Запись строки байтов в файл
f.write('world\n') # В Python 3.0 возвращает количество записанных байтов
f.close()



f = open('data.txt') # ‘r’ – это режим доступа к файлу по умолчанию
text = f.read() # Файл читается целиком в строку
text = text.split()
print(type(text))

if isinstance(text, list): # Проверка в объектно-ориентированном стиле
 print('yes')

 """

x = Fraction(1, 3)
y = Fraction(4, 6)

print("spam\a")


x = 4
while x > 0:
 print('spam!' * x)
 x -= 1

input()

x = 4
if x == 4 :
    print('****')