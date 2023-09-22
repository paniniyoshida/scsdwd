# -*- coding: cp1251 -*-
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
num = int(input("Введите число: "))
if is_prime(num):
    print(num, "является простым числом")
else:
    print(num, "не является простым числом")

