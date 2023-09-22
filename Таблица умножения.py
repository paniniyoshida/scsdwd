# -*- coding: cp1251 -*-
n = int(input('Введите размер таблицы умножения: '))
print('Таблица умножения размером', n, 'x', n, ':')
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, end='\t')
    print() 

