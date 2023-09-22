# -*- coding: cp1251 -*-
import random

def guess_number():
    number = random.randint(1, 100)
    tries = 0
    
    print("Я загадал число от 1 до 100. Попробуй угадать")
    
    while True:
        guess = int(input("Введите число: "))
        tries += 1
        
        if guess < number:
            print("Слишком маленькое число")
        elif guess > number:
            print("Слишком большое число")
        else:
            print(f"Ты угадал число")
            break

guess_number()

